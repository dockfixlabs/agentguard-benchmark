# ASI09: Agent Loop Exploitation -- while True without exit
# Vulnerability: Infinite loop with agent call, no max iterations
# Expected: AgentGuard ASI09-AGENT-LOOP HIGH
while True:
    response = agent.run(user_input)
    if response.is_complete:
        break
