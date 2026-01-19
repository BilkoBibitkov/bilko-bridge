# RALPH_MEMORY.md (v1.7 - The Sovereign Standard)

### I. CRITICAL EXECUTION RULES (How to Run)
* **Fail Fast:** Always start bash scripts with `set -e`.
* **Directory Hygiene:** Always reset directory (e.g., `cd /workspace`) at the start of a script or loop.
* **Heredoc Safety:** ALWAYS use quoted delimiters (`cat << 'EOF'`) for source code (JS/TS/CSS).
* **Self-Documentation:** Before any file generation, echo the **Intent** and the **Specific Changes**.
* **Context Probing:** Wrap git commands in `if [ -d .git ]; then ... fi`.
* **Git Safety Protocol:** Inject `git config --global --add safe.directory /workspace` for manual builds.

### II. EVOLUTIONARY STATE (How to Grow)
* **Scorched Earth Forbidden:** Do NOT wipe the project; evolve existing files.
* **Regression Checklist:** Ensure new versions contain code for previous requirements (e.g., Auth).
* **Surgical Overwrites:** Overwrite files with ALL requirements (Old + New).
* **Preserve Dependencies:** Keep `node_modules` and `package-lock.json` for build speed.

### III. ENVIRONMENT CONSTRAINTS (Toolbox Limits)
* **Current Container:** Step 2 runs in `ralph-brain` (Python 3.11). **DO NOT use npx, npm, or node here.**
* **Delegation:** Generate files in Step 2; let Step 3 (`node:20`) handle the heavy lifting.
* **Next.js Export Protocol:** Use `output: 'export'` in `next.config.mjs` and `next build`.
* **Dependency Baseline:** Explicitly set `"next": "^14.2.4"` and `"firebase": "^10.12.2"`.

### IV. SECRET & CONFIG MANAGEMENT
* **Persistence (CRITICAL):** You MUST generate a `.env.local` file containing the Firebase secrets.
* **Type Safety:** For optional Firebase fields, assign the primitive `undefined`.
* **Sovereign Access:** You have a Service Account key at `./service-account.json`. Use this for all Firebase Admin SDK tasks.

### V. DEPLOYMENT & ANCHORS
* **Anchor Files:** Every deployment REQUIRES `firebase.json` and `.firebaserc`.
* **Explicit Targeting:** Hardcode `"site": "bilkobibitkov"` in `firebase.json`.

### VI. DEBUGGING & FAILURES
* **Model Discovery:** Always read `active_model.txt` to find the correct Model ID.
* **Identity Check:** Ensure Service Accounts have `secretAccessor` permissions.

### VII. SCAR TISSUE (Historical Post-Mortems)
* **Failure [50ba0535]:** Missing anchors. Resolution: Section V "Anchor Files" rule.
* **Failure [Iter 3]:** Shell crashed on React syntax. Resolution: Section I "Heredoc Safety".
* **Failure [Git Ownership]:** Dubious ownership error. Resolution: Section I "Git Safety Protocol".
* **Failure [Next.js Export]:** `unknown option -o`. Resolution: Section III "Export Protocol".
* **Failure [Node in Brain]:** Step 2 crashed with "node: command not found". Fixed in Section III.
* **Failure [503 Overload]:** Gemini was busy and stale code was deployed. Resolution: Section VIII "API Resilience".

### VIII. OPTIMIZATION & RESILIENCE
* **One-Shot Goal:** Fulfill Content + Design + Config in Iteration 1.
* **API Resilience:** If the AI Model returns a 503 (Overloaded) or 429 (Rate Limit), EXIT immediately with error code 1. Do not proceed to build/deploy stale code.
* **Model Fallback:** If auto-selection fails, Ralph should attempt to fallback to 'gemini-1.5-pro'.

### IX. SOVEREIGN PROTOCOLS
* **Vault Hygiene:** NEVER commit `service-account.json` or `.env.local` to Git. (Enforced by .gitignore).
* **Admin Logic:** When writing server-side code (Actions/APIs), initialize `firebase-admin` using the JSON provided in the `FIREBASE_ADMIN_KEY` environment variable.