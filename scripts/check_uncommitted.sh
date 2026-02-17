#!/usr/bin/env bash
# ============================================================
# check_uncommitted.sh
# IonWave — Session commit guard
#
# PURPOSE: Detect uncommitted changes and alert the operator.
# RUN AT:  Session start AND session end (or on demand).
# USAGE:   bash scripts/check_uncommitted.sh
#          bash scripts/check_uncommitted.sh --quiet   (exit code only, no output)
#          bash scripts/check_uncommitted.sh --report  (write report file)
# EXIT:    0 = clean, 1 = uncommitted changes found
# ============================================================

set -e

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$REPO_ROOT" ]; then
  echo "ERROR: Not inside a git repository." >&2
  exit 2
fi

cd "$REPO_ROOT"

QUIET=false
REPORT=false
for arg in "$@"; do
  case "$arg" in
    --quiet)  QUIET=true ;;
    --report) REPORT=true ;;
  esac
done

# ── Gather stats ─────────────────────────────────────────────
STAGED=$(git diff --cached --name-only | wc -l | tr -d ' ')
MODIFIED=$(git diff --name-only | wc -l | tr -d ' ')
UNTRACKED=$(git ls-files --others --exclude-standard | wc -l | tr -d ' ')
TOTAL=$((STAGED + MODIFIED + UNTRACKED))

LAST_COMMIT_DATE=$(git log -1 --format="%ci" 2>/dev/null || echo "never")
LAST_COMMIT_MSG=$(git log -1 --format="%s" 2>/dev/null || echo "none")
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
NOW=$(date -u +"%Y-%m-%d %H:%M UTC" 2>/dev/null || date +"%Y-%m-%d %H:%M UTC")

# ── Output ────────────────────────────────────────────────────
if [ "$QUIET" = "false" ]; then
  echo "========================================"
  echo " IonWave Commit Guard"
  echo "========================================"
  echo " Branch:      $BRANCH"
  echo " Checked at:  $NOW"
  echo " Last commit: $LAST_COMMIT_DATE"
  echo "             \"$LAST_COMMIT_MSG\""
  echo "----------------------------------------"
  if [ "$TOTAL" -eq 0 ]; then
    echo " STATUS: CLEAN — nothing to commit"
  else
    echo " STATUS: UNCOMMITTED CHANGES FOUND"
    echo ""
    echo "   Staged:    $STAGED file(s)"
    echo "   Modified:  $MODIFIED file(s)"
    echo "   Untracked: $UNTRACKED file(s)"
    echo "   TOTAL:     $TOTAL file(s)"
    echo ""
    echo " MODIFIED FILES:"
    git status --short | head -30
    if [ "$TOTAL" -gt 30 ]; then
      echo "   ... and $((TOTAL - 30)) more"
    fi
    echo ""
    echo " ACTION REQUIRED:"
    echo "   cd \"$REPO_ROOT\""
    echo "   git add <files>"
    echo "   git commit -m \"Session N: <description>\""
    echo "   git push origin main"
  fi
  echo "========================================"
fi

# ── Write report file ─────────────────────────────────────────
if [ "$REPORT" = "true" ]; then
  REPORT_FILE="$REPO_ROOT/tracking/commit_status.txt"
  {
    echo "IonWave Commit Status Report"
    echo "Generated: $NOW"
    echo "Branch: $BRANCH"
    echo "Last commit: $LAST_COMMIT_DATE — $LAST_COMMIT_MSG"
    echo "Staged: $STAGED | Modified: $MODIFIED | Untracked: $UNTRACKED | Total: $TOTAL"
    echo ""
    if [ "$TOTAL" -gt 0 ]; then
      echo "UNCOMMITTED FILES:"
      git status --short
    else
      echo "STATUS: CLEAN"
    fi
  } > "$REPORT_FILE"
  if [ "$QUIET" = "false" ]; then
    echo "Report written to: $REPORT_FILE"
  fi
fi

# ── Exit code ─────────────────────────────────────────────────
if [ "$TOTAL" -gt 0 ]; then
  exit 1
else
  exit 0
fi
