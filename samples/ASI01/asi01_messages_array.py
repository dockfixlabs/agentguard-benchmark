# ASI01: Prompt Injection -- user input in messages array
# Vulnerability: Raw user input passed as message content
# Expected: AgentGuard ASI01-PROMPT-INJECTION CRITICAL
user_msg = request.json.get("message")
messages = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": user_msg}
]
