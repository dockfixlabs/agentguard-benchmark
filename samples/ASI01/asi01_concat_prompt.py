# ASI01: Prompt Injection — concatenation with raw user input
# Vulnerability: String concatenation to build prompt
# Expected: AgentGuard ASI01-PROMPT-INJECTION CRITICAL
user_input = input("Enter your question: ")
system_prompt = "You are a banking assistant. "
full_prompt = system_prompt + user_input
