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
    context = sys.stdin.read().strip()
    
    # PATH NORMALIZATION
    existing_files = set()
    base_dir = os.getcwd()
    for root, dirs, files in os.walk(os.path.join(base_dir, 'src')):
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, base_dir)
            existing_files.add(rel_path)

    # TARGETS
    targets = ["src/app/page.tsx"]
    remaining_tasks = [t for t in targets if t not in existing_files]

    if not remaining_tasks:
        print("<promise>COMPLETE</promise>")
        print("echo 'BILKO VERIFIED: Foundation complete.'")
        return

    next_task = remaining_tasks[0]
    
    # MODEL DISCOVERY
    try:
        all_models = list(client.models.list())
        valid_models = [m.name for m in all_models if 'generateContent' in m.supported_actions]
        valid_models.sort(key=lambda x: ("flash" not in x.lower(), x))
    except:
        valid_models = ['models/gemini-1.5-flash']

    # INSTRUCTION
    system_instr = (
        f"ROLE: Senior Next.js Developer. MISSION: Create {next_task}. "
        "CONTEXT: Minimalist Hello World. Theme: Slate-950/Blue-600. "
        "OUTPUT: Bash command with 'cat << EOF'. No markdown."
    )

    # EXECUTION
    for model_id in valid_models:
        try:
            response = client.models.generate_content(model=model_id, contents=f"{system_instr}\n\n{context}")
            clean_cmd = response.text.strip()
            if "```" in clean_cmd: clean_cmd = clean_cmd.split("```")[1].replace("bash", "").strip()
            
            if clean_cmd:
                print(f"set -e; {clean_cmd} && echo 'SUCCESS: {next_task} built.'")
                return
        except: continue
    print("echo 'FAILURE: All models failed.'")

if __name__ == "__main__":
    run_bridge()
