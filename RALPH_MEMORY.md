I. CRITICAL EXECUTION RULES (How to Run)
Fail Fast: Always start bash scripts with set -e.

Directory Hygiene: The execution loop persists state. Always reset directory (e.g., cd /workspace) at the start of a script or loop.

Heredoc Safety: When generating source code (JS/TS/CSS), ALWAYS use quoted delimiters (cat << 'EOF') to prevent Bash from interpreting ${...} as shell variables. Only use unquoted delimiters (cat << EOF) for files that specifically require shell variable injection (like .env.local).

Syntax Integrity: Check for closing keywords (fi, done).

Self-Documentation: Before any file generation step, the script must echo the Intent and the Specific Changes being made. This creates a searchable audit trail in the Cloud Build logs.

Context Probing: Never assume git history exists. Cloud Build Manual Submissions (gcloud builds submit) upload a ZIP file, stripping .git. Always wrap git commands in checks: `if [ -d .git ]; then ... fi`.

Git Safety Protocol: When running manually (gcloud builds submit), the workspace user often differs from the container user (root). ALWAYS inject `git config --global --add safe.directory /workspace` before running git commands.

II. EVOLUTIONARY STATE (How to Grow)
Scorched Earth Forbidden: Do NOT wipe the entire project (rm -rf src or rm -rf node_modules). We are evolving, not restarting.

Regression Checklist: Before "Evolutionary" overwrites, explicitly check: "Does this new file still contain the code for previous requirements (e.g., Firebase Auth)?" If a new file version is significantly smaller than the old one, double-check for accidental logic deletion.

Surgical Overwrites: Overwrite existing files with the new version containing ALL requirements (Old + New).

Clean Conflicts: Explicitly delete specific files only if you are changing file extensions (e.g., rm src/app/page.js before creating src/app/page.tsx).

Preserve Dependencies: Keep node_modules and package-lock.json to make the build faster.

III. ENVIRONMENT CONSTRAINTS (Toolbox Limits)
Current Container: You run in ralph-brain (Python 3.11). DO NOT use npx, npm, or node here.

Delegation: Your job is to generate files (package.json, tsconfig.json, next.config.mjs) using cat. The pipeline has a subsequent node:20 step to handle the heavy lifting.

Project Scaffolding: Do not use create-next-app. Manually generate the config files.

Next.js Export Protocol: In Next.js 14+, do NOT use `next export`. Configure `output: 'export'` in `next.config.mjs` and simply run `next build`. The `build` script in `package.json` must be `"next build"`.

IV. SECRET & CONFIG MANAGEMENT
Available Secrets: The pipeline ONLY provides NEXT_PUBLIC_FIREBASE_API_KEY, NEXT_PUBLIC_FIREBASE_PROJECT_ID, and NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN.

Persistence (CRITICAL): You MUST generate a .env.local file containing these values. The build step cannot see the secrets unless they are written to this file.

Forbidden Validations: Do NOT check for STORAGE_BUCKET, MESSAGING_SENDER_ID, or APP_ID.

Type Safety: For optional fields in firebaseConfig, assign the primitive undefined.

V. DEPLOYMENT & ANCHORS
Builder: Use gcr.io/bilkobibitkov/firebase.

Anchor Files: Every deployment REQUIRES firebase.json and .firebaserc.

Explicit Targeting: Do NOT rely on default site resolution. In firebase.json, you MUST hardcode the "site" property (e.g., "site": "bilkobibitkov") to avoid "Assertion failed" or "Site not found" errors.

API Readiness: Ensure `firebasehosting.googleapis.com` is enabled before attempting deployment.

VI. DEBUGGING & FAILURES
Model Discovery: Always read active_model.txt to find the correct Model ID.

Validation: Abort if secrets are empty.

Instant Failure: If a build fails with "Build does not specify logsBucket", it is a YAML Syntax or Secret Definition error. Use gcloud builds describe to identify the validation failure.

Identity Check: Manual builds often use the Compute Engine Service Account, while Triggers use the Cloud Build Service Account. Ensure BOTH have `secretAccessor` permissions.

VII. SCAR TISSUE (Historical Post-Mortems)
Failure [50ba0535]: Firebase Deploy failed with exit code 2.
Cause: Missing firebase.json and .firebaserc because the "Wipe" rule was removed without adding a "Validation of Anchors" rule.
Resolution: Created Section V "Anchor Files" rule.

Failure [Iter 3 - Bad Substitution]: Shell crashed on ${inter.className}.
Cause: Unquoted Heredoc interpreted React/JS syntax as Bash variables.
Resolution: Section I "Heredoc Safety" rule.

Failure [Manual Build - Missing Git]: Step 1 crashed with "fatal: not a git repository".
Cause: `gcloud builds submit` uploads a zip file and ignores .git by default.
Resolution: Added Section I "Context Probing". For manual debugs, created .gcloudignore allowing .git.

Failure [Ghost Build]: Build marked SUCCESS, but nothing changed.
Cause: The "Docker Image" trigger fired (creating the brain), but the "App Pipeline" trigger was missing.
Resolution: Always verify the Build Trigger Name/ID in logs to ensure the correct pipeline is running.

Failure [Git Ownership]: Step 0 crashed with "fatal: detected dubious ownership".
Cause: User ID mismatch in manual builds.
Resolution: Added "Git Safety Protocol" (safe.directory) to Section I.

Failure [Self-Copy]: Step 0 crashed with "cp: 'prd.json' and 'prd.json' are the same file".
Cause: Redundant file copy logic.
Resolution: Removed the bad line. Lesson: Don't copy files to themselves.

Failure [Ambiguous Target]: Firebase Deploy crashed with "Assertion failed".
Cause: CLI couldn't map the config to a specific site.
Resolution: Added "Explicit Targeting" rule to Section V (must set "site" in firebase.json).

Failure [Next.js Export]: Build failed with `error: unknown option '-o'`.
Cause: Used deprecated `next export` command in package.json.
Resolution: Added "Next.js Export Protocol" to Section III.