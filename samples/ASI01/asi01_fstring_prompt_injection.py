# ASI01: Prompt Injection — f-string with user input
# Vulnerability: User input directly concatenated into LLM prompt via f-string
# Expected: AgentGuard ASI01-PROMPT-INJECTION CRITICAL
user_input = request.form.get("message")
prompt = f"You are a helpful assistant. The user says: {user_input}"
response = llm.chat(prompt)
