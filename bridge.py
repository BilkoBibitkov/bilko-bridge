import sys, os
from google import genai

def run_bridge():
    # The SDK automatically detects GOOGLE_API_KEY or GEMINI_API_KEY
    try:
        client = genai.Client()
    except Exception as e:
        print(f"echo 'FAILURE: GenAI Client initialization failed: {e}'")
        return

    full_input = sys.stdin.read().strip()

    # --- PARSE INPUT ---
    # Expecting: PRD: <json>\n\nCONTEXT: <files>
    try:
        if '\n\n' in full_input:
            prd_part, context_part = full_input.split('\n\n', 1)
        else:
            prd_part, context_part = full_input, ""
    except ValueError:
        print("echo 'FAILURE: Could not split PRD and Context.'")
        return

    # --- SYSTEM INSTRUCTION ---
    system_instr = (
        "ROLE: Senior AI Developer Pair-Programmer.\n"
        "MISSION: Implement the user's request found in prd.json by generating a bash script.\n"
        "INSTRUCTIONS:\n"
        "1. Your output MUST be a single, executable bash script.\n"
        "2. To modify a file, you MUST overwrite the entire file using 'cat << EOF > path/to/file.tsx'.\n"
        "3. Your script must be robust. Use 'set -e'.\n"
        "4. Do NOT include explanations, markdown, or any text other than the bash script itself."
    )

    # --- EXECUTION ---
    try:
        # Using Gemini 2.0 Flash for speed and high context window
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=f"PRD AND CONTEXT:\n{full_input}",
            config={'system_instruction': system_instr}
        )
        
        clean_cmd = response.text.strip()
        if clean_cmd.startswith("\`\`\`bash"): clean_cmd = clean_cmd[7:]
        if clean_cmd.startswith("\`\`\`"): clean_cmd = clean_cmd[3:]
        if clean_cmd.endswith("\`\`\`"): clean_cmd = clean_cmd[:-3]
        
        if clean_cmd.strip():
            print(f"set -e; {clean_cmd.strip()}\n echo 'SUCCESS: Ralph evolution iteration complete.'")
        else:
            print("echo 'FAILURE: Model returned empty command.'")
    except Exception as e:
        print(f"echo 'FAILURE: AI generation error: {e}'")

if __name__ == "__main__":
    run_bridge()