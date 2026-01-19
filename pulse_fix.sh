pulse() {
  local msg="${1:-evolutionary update}"
  echo "--- 🫀 [1/4] Stashing local edits ---"
  git add .
  git stash
  
  echo "--- 🫀 [2/4] Syncing with Ralphs Brain (Rebase) ---"
  git pull origin main --rebase
  
  echo "--- 🫀 [3/4] Re-applying local edits ---"
  git stash pop || echo "No stashed changes to apply"
  
  echo "--- 💾 [4/4] Saving to GitHub ---"
  git add .
  git commit -m "$msg" || echo "Nothing new to commit"
  git push origin main
  
  echo "--- 🚀 Launching App Pipeline ---"
  gcloud builds submit --config cloudbuild.yaml .
}
