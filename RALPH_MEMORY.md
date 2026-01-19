# RALPH_MEMORY.md (v1.8 - The Kernel)

### I. CORE DIRECTIVES (High Priority)
* **Execution:** Use `set -e` in all scripts. Always `cd /workspace` at start.
* **Safety:** Quoted Heredocs (`cat << 'EOF'`) for code; `safe.directory /workspace` for git.
* **Sovereign:** Use `./service-account.json` (FIREBASE_ADMIN_KEY) for all Admin SDK tasks. 
* **Hygiene:** NEVER commit `.json` keys or `.env.local` to Git. Enforced by `.gitignore`.

### II. ARCHITECTURE & BUILD
* **Stack:** Next.js 14.2.4 + Firebase 10.12.2.
* **Brain:** Python 3.11 (`ralph-brain`). **NO node/npm here.**
* **Pipeline:** Generate files in Step 2; Step 3 (`node:20`) builds; Step 4 deploys.
* **Export:** `output: 'export'` in `next.config.mjs` + `next build` in `package.json`.
* **Targeting:** Hardcode `"site": "bilkobibitkov"` in `firebase.json`.

### III. RESILIENCE PROTOCOLS
* **One-Shot:** Achieve PRD goals (Content + Logic + Config) in Iteration 1. 
* **Failover:** If 503/429 error occurs, EXIT 1. Pipeline will retry/fallback to `gemini-1.5-pro`.
* **Persistence:** `.env.local` MUST contain all `NEXT_PUBLIC_` keys for the build step.

### IV. SCAR TISSUE (Historical Logic)
* **Git:** Diverged history? Use `pulse` local / `pull --rebase` cloud.
* **Next.js:** Avoid `next export` (-o flag). Use `output: 'export'`.
* **Dependencies:** Webpack/Undici errors? Force Next.js 14.2+ to resolve.
* **Auth:** Always preserve existing Firebase logic during surgical overwrites.