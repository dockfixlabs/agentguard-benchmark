# ASI01: Prompt Injection -- template string with user-controlled variable
# Vulnerability: Template string with user-controlled variable
# Expected: AgentGuard ASI01-PROMPT-INJECTION HIGH
template = "Answer this question: {q}"
q = request.args.get("q")
prompt = template.format(q=q)
