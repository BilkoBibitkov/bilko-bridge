#!/bin/bash
set -e

# Configuration
MAX_ITERS=${1:-1}
echo "Starting Ralph - Max iterations: $MAX_ITERS"

# Validation
if [ ! -f "prd.json" ]; then
    echo "ERROR: prd.json not found."
    exit 1
fi

for ((i=1; i<=MAX_ITERS; i++)); do
    echo -e "\n═══════════════════════════════════════════════════════"
    echo "  Ralph Iteration $i of $MAX_ITERS"
    echo "  Model: $(cat active_model.txt 2>/dev/null || echo 'Auto-Detect')"
    echo "═══════════════════════════════════════════════════════"
    
    # 1. Prepare Context (Lightweight)
    # We send the file structure so the AI knows where things are, 
    # but not the full content (to avoid token overflow).
    FILE_TREE=$(find . -maxdepth 3 -not -path '*/.*' -not -path './node_modules*' | sort)
    
    # 2. Call Bridge
    # We pipe the PRD and the File Tree into the python script
    echo "--- Generating Plan ---"
    
    # Construct the input payload
    {
        echo "CURRENT_PRD:"
        cat prd.json
        echo -e "\n\nCURRENT_FILE_STRUCTURE:"
        echo "$FILE_TREE"
    } | python3 bridge.py > execution_plan.sh

    # 3. Verify & Execute
    if [ -s execution_plan.sh ]; then
        echo "--- Plan Generated (Preview) ---"
        head -n 5 execution_plan.sh
        echo "..."
        
        echo "--- Executing Plan ---"
        chmod +x execution_plan.sh
        ./execution_plan.sh
    else
        echo "CRITICAL FAILURE: Bridge produced empty plan."
        exit 1
    fi
    
    # 4. Cleanup
    rm execution_plan.sh
    
    sleep 2
done

echo "Ralph finished cycle."