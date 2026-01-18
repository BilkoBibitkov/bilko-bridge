import sys, os, time
from google import genai

def run_bridge():
    # AUTH
    api_key = None
    if os.path.exists(".env"):
        with open(".env") as f:
            for line in f:
                if "GOOGLE_API_KEY=" in line:
                    api_key = line.split("=")[1].strip().strip('"').strip("'")
    
    if not api_key:
        print("echo 'FAILURE: No API Key found.'")
        return

    client = genai.Client(api_key=api_key)
    full_input = sys.stdin.read().strip()

    # --- PARSE INPUT ---
    try:
        # The input format is "USER_PROMPT: <prompt>\n\nPRD:..."
        prompt_part, context_part = full_input.split('\n\n', 1)
        if 'USER_PROMPT:' not in prompt_part:
             raise ValueError("USER_PROMPT not in first part of input")
        user_prompt = prompt_part.replace('USER_PROMPT:', '').strip()
    except ValueError:
        user_prompt = ""
        context_part = full_input 

    if not user_prompt:
        print("echo 'BILKO NOTE: No prompt provided. Foundation is complete.'")
        return

    # --- MODEL DISCOVERY ---
    try:
        all_models = list(client.models.list())
        valid_models = [m.name for m in all_models if 'generateContent' in m.supported_actions]
        valid_models.sort(key=lambda x: ("flash" not in x.lower(), x))
    except:
        valid_models = ['models/gemini-1.5-flash']

    # --- SYSTEM INSTRUCTION ---
    system_instr = (
        f"ROLE: Senior AI Developer Pair-Programmer.\n"
        f"MISSION: Implement the user's request by generating a bash script.\n"
        f"USER REQUEST: '{user_prompt}'\n\n"
        f"INSTRUCTIONS:\n"
        f"1. You are given a PRD (prd.json) and code context.\n"
        f"2. Your output MUST be a single, executable bash script.\n"
        f"3. To modify a file, you MUST overwrite the entire file using `cat << EOF > path/to/file.tsx`. Do NOT use `sed` or `patch`.\n"
        f"4. If the request implies a goal change, also update `prd.json` in your script.\n"
        f"5. Your script must be robust. Use `set -e`.\n"
        f"6. Do NOT include explanations, markdown, or any text other than the bash script itself."
    )

    # --- EXECUTION ---
    for model_id in valid_models:
        try:
            response = client.models.generate_content(model=model_id, contents=f"{system_instr}\n\n{context_part}")
            
            clean_cmd = response.text.strip()
            if clean_cmd.startswith("```bash"): clean_cmd = clean_cmd[7:]
            if clean_cmd.startswith("```"): clean_cmd = clean_cmd[3:]
            if clean_cmd.endswith("```"): clean_cmd = clean_cmd[:-3]
            clean_cmd = clean_cmd.strip()
            
            if clean_cmd:
                success_message = f"SUCCESS: User prompt '{user_prompt[:30]}...' implemented."
                print(f"set -e; {clean_cmd}\n echo '{success_message}'")
                return
        except Exception:
            continue 
            
    print("echo 'FAILURE: All models failed to generate a valid command.'")

if __name__ == "__main__":
    run_bridge()
