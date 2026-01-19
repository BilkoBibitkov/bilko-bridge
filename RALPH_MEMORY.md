# RALPH_MEMORY.md (v1.9.2 - The Sovereign Master)

### I. CRITICAL EXECUTION RULES
* **Fail Fast:** Always start bash scripts with `set -e`.
* **Heredoc Safety:** ALWAYS use quoted delimiters (`cat << 'EOF'`) for source code (JS/TS/CSS). Prevents Bash from interpreting `${...}`.
* **Context Probing:** Wrap git commands in `if [ -d .git ]; then ... fi`. Cloud Build manual submissions strip `.git`.
* **Git Safety:** ALWAYS inject `git config --global --add safe.directory /workspace` for manual builds.

### II. ARCHITECTURAL ANCHORS (NO COMPROMISE)
* **App Router Only:** All code lives in `src/app/`. ROOT DIRECTORY `/pages` is STRICTLY FORBIDDEN.
* **Branding:** Hero text MUST be "BILKO BIBITKOV LIVES".
* **Theme:** Bulgarian flag background gradient (White/Green/Red) in `globals.css`.
* **Deployment:** Hardcode `"site": "bilkobibitkov"` in `firebase.json`.
* **Export:** Use `output: 'export'` in `next.config.mjs` and `"next build"` in `package.json`.

### III. SOVEREIGN ADMIN PROTOCOLS
* **Vault Assets:**
  * `./service-account.json`: Primary Firebase Admin access (from `FIREBASE_ADMIN_KEY`).
  * `./ralph-key.json`: General Project Admin access (from `ralph-key`).
  * `process.env.AMP_API_KEY`: API access for AMP/Mobile analytics.
* **Admin SDK:** Use `firebase-admin` for server-side logic (API routes). Do not confuse with client-side `firebase` SDK.
* **Vault Hygiene:** NEVER commit `.json` files or `.env.local` to Git. (Enforced by `.gitignore`).

### IV. ENVIRONMENT & DEPENDENCIES (HARD-BLOCK)
* **Brain Container (Python):** You are running in a Python 3.11 environment. 
* **FORBIDDEN COMMANDS:** `npm`, `npx`, `node`, `yarn`. Using these will CRASH the build.
* **Delegation:** Your ONLY job is to write `.ts`, `.tsx`, and `.json` files. Step 3 (the Node container) will handle the installation and building.

### V. SCAR TISSUE (Historical Post-Mortems)
* **Failure [Build 2337e48d]:** Wiped project and attempted "Pages Router" conversion. 
  * *Resolution:* App Router is the only permitted architecture. No root `/pages` directory.
* **Failure [Build a3e86414]:** Git Race Condition. User and Ralph drifted.
  * *Resolution:* Use `pulse` command locally to stash, rebase, and pop before launching.
* **Failure [503 Overload]:** Model congestion. 
  * *Resolution:* Pipeline now uses 60s retry + fallback to `gemini-1.5-pro`.
* **Failure [Webpack Undici]:** Dependency version conflict.
  * *Resolution:* Lock Next.js to exactly `14.2.4`.

### VI. OPTIMIZATION & RESILIENCE
* **One-Shot Goal:** Fulfill Branding + Logic + Admin Config in Iteration 1.
* **API Resilience:** If the AI Model returns 503/429, EXIT immediately with code 1. Do not deploy stale/empty code.

