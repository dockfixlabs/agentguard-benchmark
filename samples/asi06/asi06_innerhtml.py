# ASI06: Insecure Output Handling -- innerHTML with LLM output
# Vulnerability: LLM output assigned to innerHTML
# Expected: AgentGuard ASI06-UNSAFE-EVAL HIGH
response = agent.generate_response(query)
element.innerHTML = response
