# ASI01: Prompt Injection — .format() with user data
# Vulnerability: User input formatted into prompt template
# Expected: AgentGuard ASI01-PROMPT-INJECTION HIGH
template = "System: You are an assistant.\nUser: {query}"
user_query = input("Ask: ")
prompt = template.format(query=user_query)
