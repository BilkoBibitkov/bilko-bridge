# RALPH_MEMORY.md (v1.9.8 - The Sovereign Guard)

### I. CRITICAL EXECUTION RULES
* **Fail Fast:** Always start bash scripts with `set -e`.
* **Circuit Breaker (MANDATORY):** If a model response returns "503 UNAVAILABLE" or any generation error, you MUST `exit 1` immediately. NEVER proceed to build or deploy if the plan is an error message. It is better to fail the build than to deploy stale or empty code.
* **Heredoc Safety:** ALWAYS use quoted delimiters (e.g., `cat << 'EOF'`) for source code (JS/TS/CSS). This prevents the shell from interpreting `${...}` or backticks as shell variables.
* **Context Probing:** Wrap git commands in `if [ -d .git ]; then ... fi`. Cloud Build manual submissions strip `.git`.
* **Git Safety:** ALWAYS inject `git config --global --add safe.directory /workspace` for manual builds to resolve ownership issues.

### II. ARCHITECTURAL ANCHORS (NO COMPROMISE)
* **App Router Only:** All application code lives in `src/app/`. Use of the ROOT DIRECTORY `/pages` is STRICTLY FORBIDDEN.
* **Branding:** The primary hero text MUST be "BILKO BIBITKOV LIVES".
* **Theme:** Background must be the Bulgarian flag gradient (White, Green, Red) configured in `src/app/globals.css`.
* **Deployment Anchors:** Hardcode `"site": "bilkobibitkov"` in `firebase.json` and ensure `.firebaserc` points to the `bilkobibitkov` project.
* **Export Protocol:** Use `output: 'export'` in `next.config.mjs` and ensure `images: { unoptimized: true }` is set for static compatibility.

### III. SOVEREIGN ADMIN PROTOCOLS
* **Vault Assets:**
  * `./service-account.json`: Primary Firebase Admin access (injected from `FIREBASE_ADMIN_KEY`).
  * `./ralph-key.json`: General Project Admin access (injected from `ralph-key`).
  * `process.env.AMP_API_KEY`: API access for AMP/Mobile analytics services.
* **Admin SDK:** Use `firebase-admin` for server-side logic (API routes). Do not use client-side `firebase` SDK for administrative tasks.
* **Vault Hygiene:** NEVER commit `.json` keys or `.env.local` to Git. Ensure they are added to `.gitignore`.

### IV. ENVIRONMENT & DEPENDENCIES (HARD-BLOCK)
* **Brain Container:** You are running in the `ralph-brain` (Python 3.11) container.
* **FORBIDDEN COMMANDS:** `npm`, `npx`, `node`, `yarn`. Using these inside this container will CRASH the build (Error 127).
* **Delegation:** Your ONLY job is to generate `.ts`, `.tsx`, `.css`, and `.json` files. Step 3 in the pipeline (the Node container) will handle the `npm install` and `npm run build`.

### V. SCAR TISSUE (Historical Post-Mortems)
* **Failure [Build 2337e48d]:** Ralph wiped the project and tried to use the old Pages Router. 
  * *Resolution:* App Router is the only permitted architecture. No root `/pages` directory.
* **Failure [Build a3e86414]:** Git Race Condition. Local and Cloud histories diverged.
  * *Resolution:* Use `pulse` command locally to stash, rebase, and pop before launching.
* **Failure [Build 951dde91]:** Imported missing `./page.module.css`, crashing Webpack.
  * *RESOLUTION (HARD RULE):* NEVER use CSS Modules (`.module.css`). ALL styling must be done via Tailwind utility classes directly in the JSX `className` prop. Never import a file you did not explicitly create in the same script.
* **Failure [Webpack Undici]:** Dependency version conflict.
  * *Resolution:* Lock Next.js to exactly `14.2.4` and Firebase to `10.12.2`.

### VI. OPTIMIZATION & RESILIENCE (COOLING PROTOCOL)
* **One-Shot Goal:** Fulfill Branding + Design + Content + Admin Config in Iteration 1.
* **Patience:** If the API returns a 503 error, the system will now sleep for 60 seconds. Do not panic.
* **Circuit Breaker:** If 503 persists after 3 "Cooled" attempts, the build must terminate to prevent stale deployments.

### VII. SOVEREIGN IDENTITY
* **Language:** Respect Bulgarian heritage. 
* **Facts:** When requested, include verified historical facts regarding the Cyrillic alphabet, the 681 AD establishment, and Rose Oil production.