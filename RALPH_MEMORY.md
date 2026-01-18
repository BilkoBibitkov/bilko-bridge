# RALPH MEMORY LOG

## I. CRITICAL EXECUTION RULES
- **Fail Fast:** Always start bash scripts with `set -e`.
- **Directory Hygiene:** The execution loop persists state. **Always reset directory** (e.g., `cd /workspace`) at the start of a script or loop.
- **Syntax Integrity:** Check for closing keywords (`fi`, `done`).
- **Heredoc Safety:** When generating source code (JS/TS/CSS), **ALWAYS use quoted delimiters** (`cat << 'EOF'`) to prevent Bash from interpreting `${...}` as shell variables. Only use unquoted delimiters (`cat << EOF`) for files that specifically require shell variable injection (like `.env.local`).

## II. ENVIRONMENT CONSTRAINTS (The "Wrong Toolbox" Lesson)
- **Current Container:** You run in `ralph-brain` (Python 3.11). **DO NOT** use `npx`, `npm`, or `node` here.
- **Delegation:** Your job is to generate files (`package.json`, `tsconfig.json`, `next.config.mjs`) using `cat`.
- **The Muscle:** The pipeline has a subsequent `node:20` step. Trust it to run `npm install` and `npm run build`.
- **Project Scaffolding:** Do not use `create-next-app`. Manually generate the config files.
- **Evolutionary State (CRITICAL):** Do **NOT** wipe the entire project (`rm -rf src` or `rm -rf node_modules`). We are evolving, not restarting.
  - **Overwrite** existing files with the new version containing ALL requirements (Old + New).
  - **Clean Conflicts:** Explicitly delete specific files *only* if you are changing file extensions (e.g., `rm src/app/page.js` before creating `src/app/page.tsx`).
  - **Preserve Dependencies:** Keep `node_modules` and `package-lock.json` to make the build faster.

## III. API & AUTHENTICATION
- **Model Discovery:** Always read `active_model.txt` to find the correct Model ID.
- **Validation:** Abort if secrets are empty.

## IV. DEPLOYMENT
- **Builder:** Use `gcr.io/bilkobibitkov/firebase`.

## V. DEBUGGING PROTOCOLS
- **Instant Failure:** If a build fails with "Build does not specify logsBucket", it is a YAML Syntax or Secret Definition error. Use 'gcloud builds describe' to identify the validation failure.

## VI. SECRET MANAGEMENT (STRICT LIMITS)
- **Available Secrets:** The pipeline **ONLY** provides `NEXT_PUBLIC_FIREBASE_API_KEY`, `NEXT_PUBLIC_FIREBASE_PROJECT_ID`, and `NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN`.
- **Persistence (CRITICAL):** You **MUST** generate a `.env.local` file containing these values.
- **Forbidden Validations:** Do **NOT** check for `STORAGE_BUCKET`, `MESSAGING_SENDER_ID`, or `APP_ID`.
- **Type Safety:** For optional fields in `firebaseConfig`, assign the primitive `undefined`.
