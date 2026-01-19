# RALPH_MEMORY.md (v1.9.1 - The Grand Archive)

### I. CRITICAL EXECUTION RULES
* **Fail Fast:** Always start bash scripts with `set -e`.
* **Heredoc Safety:** ALWAYS use quoted delimiters (`cat << 'EOF'`) for source code (JS/TS/CSS). This prevents Bash from interpreting `${...}` as shell variables.
* **Context Probing:** Wrap git commands in `if [ -d .git ]; then ... fi`. Cloud Build manual submissions strip `.git`.
* **Git Safety:** ALWAYS inject `git config --global --add safe.directory /workspace` for manual builds.

### II. ARCHITECTURAL ANCHORS (NO COMPROMISE)
* **App Router Only:** All code lives in `src/app/`. ROOT DIRECTORY `/pages` is FORBIDDEN.
* **Branding:** Hero text MUST be "BILKO BIBITKOV LIVES".
* **Theme:** Bulgarian flag background gradient (White/Green/Red) in `globals.css`.
* **Deployment:** Hardcode `"site": "bilkobibitkov"` in `firebase.json`.
* **Export:** Use `output: 'export'` in `next.config.mjs` and `"next build"` in `package.json`.

### III. SOVEREIGN ADMIN PROTOCOLS
* **Secret Access:** Use `./service-account.json`. This is injected by the pipeline.
* **Admin SDK:** Use `firebase-admin` for server-side logic (API routes).
* **Vault Hygiene:** NEVER commit `.json` files or `.env.local` to Git. (Enforced by .gitignore).

### IV. ENVIRONMENT & DEPENDENCIES
* **Brain Container:** You run in `ralph-brain` (Python). **DO NOT use npx, npm, or node here.**
* **Baseline:** Force `"next": "^14.2.4"` and `"firebase": "^10.12.2"` in `package.json`.
* **Persistence:** You MUST generate a `.env.local` for the Step 3 build to succeed.

### V. SCAR TISSUE (Historical Post-Mortems)
* **Failure [Build 2337e48d]:** Wiped project and installed "Pages Router" with hallucinations. 
  * *Resolution:* Re-enforced Section II (App Router Only).
* **Failure [50ba0535]:** Missing anchors (firebase.json). 
  * *Resolution:* Anchors are mandatory for every iteration.
* **Failure [Iter 3]:** Shell crashed on React syntax. 
  * *Resolution:* Always use quoted Heredocs.
* **Failure [Ambiguous Target]:** Firebase Deploy crashed. 
  * *Resolution:* Hardcode "site" in firebase.json.
* **Failure [503 Overload]:** Gemini was busy, stale code deployed. 
  * *Resolution:* Pipeline now includes 60s retry and 1.5-Pro fallback.

### VI. OPTIMIZATION & RESILIENCE
* **One-Shot Goal:** Fulfill Content + Design + Config in Iteration 1.
* **API Resilience:** If the AI Model returns a 503 or 429, EXIT immediately with error code 1.