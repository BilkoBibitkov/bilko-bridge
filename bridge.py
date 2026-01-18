import sys, os
from google import genai

def run_bridge():
    # 1. Setup Client
    raw_key = os.environ.get("GOOGLE_API_KEY", "").strip()
    if not raw_key:
         print("echo 'FAILURE: API Key is empty.'"); return
    
    try:
        client = genai.Client(api_key=raw_key)
    except Exception as e:
        print(f"echo 'FAILURE: Client init failed: {e}'"); return

    # 2. Read "The Secret" (Memory)
    memory_content = ""
    if os.path.exists("RALPH_MEMORY.md"):
        with open("RALPH_MEMORY.md", "r") as f:
            memory_content = f.read().strip()

    # 3. Read Input
    full_input = sys.stdin.read().strip()

    # 4. Construct System Instruction with Memory
    system_instr = (
        "ROLE: Senior AI Developer Pair-Programmer.\n"
        f"PERSISTENT MEMORY/RULES:\n{memory_content}\n"  # <--- Memory Injected Here
        "MISSION: Implement the user's request found in prd.json by generating a bash script.\n"
        "INSTRUCTIONS:\n"
        "1. Output MUST be a single, executable bash script.\n"
        "2. Use 'cat << EOF' to overwrite files.\n"
        "3. Script must use 'set -e'.\n"
        "4. NO markdown, NO explanations. Just code."
    )

    # 5. Execute
    try:
        # We use the specific -001 version to avoid 404 errors
        response = client.models.generate_content(
            model='gemini-1.5-flash-001', 
            contents=f"PRD AND CONTEXT:\n{full_input}",
            config={'system_instruction': system_instr}
        )
        
        clean_cmd = response.text.strip()
        if clean_cmd.startswith("```bash"): clean_cmd = clean_cmd[7:]
        if clean_cmd.startswith("```"): clean_cmd = clean_cmd[3:]
        if clean_cmd.endswith("```"): clean_cmd = clean_cmd[:-3]
        
        if clean_cmd.strip():
            print(f"set -e; {clean_cmd.strip()}\n echo 'SUCCESS: Ralph evolution iteration complete.'")
        else:
            print("echo 'FAILURE: Model returned empty command.'")
    except Exception as e:
        safe_error = str(e).replace("'", "").replace('"', "")
        print(f"echo 'FAILURE: AI generation error: {safe_error}'")

if __name__ == "__main__":
    run_bridge()