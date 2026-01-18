# RALPH MEMORY LOG

## I. CRITICAL EXECUTION RULES
- **Fail Fast:** Always start bash scripts with `set -e`.
- **Syntax Integrity:** Check for closing keywords. Pair `if` with `fi`, `do` with `done`.
- **Variable Safety:** In Cloud Build YAML, use `$$VAR` (double dollar) for environment variables, never backslashes.

## II. ENVIRONMENT CONSTRAINTS (The "Wrong Toolbox" Fix)
- **Current Container:** You run in `python:3.11`. **DO NOT use `npx`, `npm`, or `node` commands.**
- **Project Scaffolding:** Do not use `create-next-app`. Instead, manually generate `package.json`, `tsconfig.json`, and `next.config.mjs` using `cat << EOF`.
- **Delegation:** The pipeline has a subsequent `node:20` step. Trust it to run `npm install` and `npm run build` based on the files you generate.
- **System Tools:** Base images are minimal. If you need `curl` or `git` in a script, `apt-get install` them first.

## III. API & AUTHENTICATION
- **Validation:** Check `gcloud` auth before accessing secrets. Abort if variables are empty.
- **Hygiene:** Always `.strip()` whitespace from API Keys.
- **Model Discovery:** Never guess model names. Read `active_model.txt` (from the Probe step).
- **Error Handling:** A 404 on `generateContent` means "Wrong Model ID", not "Invalid Key".

## IV. DEPLOYMENT
- **Builder:** Use the custom `gcr.io/bilkobibitkov/firebase` builder.