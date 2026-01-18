# RALPH MEMORY LOG

## I. CRITICAL EXECUTION RULES
- **Fail Fast:** Always start bash scripts with `set -e`.
- **Directory Hygiene:** The execution loop persists state. **Always reset directory** (e.g., `cd /workspace`) at the start of a script or loop.
- **Syntax Integrity:** Check for closing keywords (`fi`, `done`).

## II. ENVIRONMENT CONSTRAINTS (The "Wrong Toolbox" Lesson)
- **Current Container:** You run in `ralph-brain` (Python 3.11). **DO NOT** use `npx`, `npm`, or `node` here.
- **Delegation:** Your job is to generate files (`package.json`, `tsconfig.json`, `next.config.mjs`) using `cat`.
- **The Muscle:** The pipeline has a subsequent `node:20` step. Trust it to run `npm install` and `npm run build` based on the files you generate.
- **Project Scaffolding:** Do not use `create-next-app`. Manually generate the config files.
- **Idempotency:** The workspace persists across iterations. Your generated script must explicitly clean up before creating. Always run `rm -rf app src` before scaffolding to prevent conflicts between `app/` and `src/app/`.

## III. API & AUTHENTICATION
- **Model Discovery:** Always read `active_model.txt` to find the correct Model ID.
- **Validation:** Abort if secrets are empty.

## IV. DEPLOYMENT
- **Builder:** Use `gcr.io/bilkobibitkov/firebase`.

## V. DEBUGGING PROTOCOLS
- **Instant Failure:** If a build fails with "Build does not specify logsBucket", it is a YAML Syntax or Secret Definition error. Use 'gcloud builds describe' to identify the validation failure.
