#!/bin/bash
MAX_ITERS=${1:-1}
echo "Starting Ralph - Max iterations: $MAX_ITERS"

for ((i=1; i<=MAX_ITERS; i++)); do
    echo -e "\n═══════════════════════════════════════════════════════"
    echo "  Ralph Iteration $i of $MAX_ITERS"
    echo "═══════════════════════════════════════════════════════"
    
    # Capture Project Context
    CONTEXT=$(find src -maxdepth 3 \( -name "*.tsx" -o -name "*.css" \) -not -path "*/node_modules/*" -exec grep -l "" {} + 2>/dev/null | xargs cat 2>/dev/null)
    
    # Call Bridge
    cmd=$(echo -e "PRD:\n$(cat prd.json)\n\nCONTEXT:\n$CONTEXT" | python3 bridge.py)
    
    echo "EXECUTING: $cmd"
    eval "$cmd"
    
    if [[ "$cmd" == *"<promise>COMPLETE</promise>"* ]]; then
        echo "Ralph finished all tasks."
        exit 0
    fi
    
    sleep 2
done
echo "Ralph reached max iterations."
