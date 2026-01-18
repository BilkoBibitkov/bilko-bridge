#!/bin/bash
set -e

# 1. Ask Google for the list of models available to YOUR specific key
echo "Probing Google API for available models..."
RAW_JSON=$(curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=${GOOGLE_API_KEY}")

# 2. Check for errors
if echo "$RAW_JSON" | grep -q "\"error\":"; then
    echo "CRITICAL FAILURE: API returned an error."
    echo "$RAW_JSON"
    exit 1
fi

# 3. Select the best model (Preference: 1.5-Flash -> 1.5-Pro -> 1.0-Pro)
if echo "$RAW_JSON" | grep -q "gemini-1.5-flash"; then
  CHOSEN_MODEL="gemini-1.5-flash"
elif echo "$RAW_JSON" | grep -q "gemini-1.5-pro"; then
  CHOSEN_MODEL="gemini-1.5-pro"
elif echo "$RAW_JSON" | grep -q "gemini-1.0-pro"; then
  CHOSEN_MODEL="gemini-1.0-pro"
else
  # Emergency Fallback
  CHOSEN_MODEL=$(echo "$RAW_JSON" | grep -o "models/gemini-[^\"]*" | head -n 1 | sed 's/models\///')
fi

# 4. Save result
if [ -z "$CHOSEN_MODEL" ]; then
    echo "CRITICAL FAILURE: No Gemini models found."
    echo "Raw Response: $RAW_JSON"
    exit 1
else
    echo "$CHOSEN_MODEL" > active_model.txt
    echo "SUCCESS: Auto-selected model: $CHOSEN_MODEL"
fi