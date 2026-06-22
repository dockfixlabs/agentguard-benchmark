# ASI02: Tool Abuse — unrestricted tool registration
# Vulnerability: Agent can use any tool with wildcard
# Expected: AgentGuard ASI02-TOOL-ABUSE HIGH
agent.register_tool(name="*", scope="all")