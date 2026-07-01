# ASI06: Insecure Output Handling -- LLM output rendered as HTML
# Vulnerability: Agent output rendered in HTML without escaping
# Expected: AgentGuard ASI06-UNSAFE-EVAL HIGH
response = llm.generate(user_input)
return f"<div>{response}</div>"
