pulse() {
  local msg="${1:-evolutionary update}"
  echo "--- 🫀 Syncing with Ralph's Brain ---"
  git add .
  # Pull Ralph's latest work and put your changes on top
  git pull origin main --rebase
  
  echo "--- 💾 Saving manual updates ---"
  git commit -m "$msg" || echo "No manual changes to commit"
  git push origin main
  
  echo "--- 🚀 Launching App Pipeline ---"
  gcloud builds submit --config cloudbuild.yaml .
}
