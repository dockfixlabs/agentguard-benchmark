# ASI01: Prompt Injection — user input in template string
# Vulnerability: Template string with user-controlled variable
# Expected: AgentGuard ASI01-PROMPT-INJECTION HIGH
template = "Answer this question: {q}"
q = request.args.get("q")
prompt = template.format(q=q)