#!/bin/bash
set -e
echo "--- 🧠 Probing Sovereign Intelligence Tiers ---"
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "❌ ERROR: GOOGLE_API_KEY is empty. Build halted."
    exit 1
fi
# Defaulting to 2.0 Flash for 2026 speed
CHOSEN="gemini-2.0-flash" 
echo "$CHOSEN" > active_model.txt
echo "✅ SELECTION: $CHOSEN"
