# ASI09: Agent Loop Exploitation -- recursive call without depth limit
# Vulnerability: Agent calls itself recursively with no depth limit
# Expected: AgentGuard ASI09-AGENT-LOOP HIGH
def run_agent(query):
    result = llm.generate(query)
    if "need_more" in result:
        return run_agent(result)
    return result
