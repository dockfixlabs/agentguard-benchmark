# ASI02: Tool Abuse — no rate limit on tool calls
# Vulnerability: max_iterations set to None — unlimited agent loops
# Expected: AgentGuard ASI02-TOOL-ABUSE HIGH + ASI09-AGENT-LOOP HIGH
max_iterations = None
rate_limit = 0
timeout = float("inf")
