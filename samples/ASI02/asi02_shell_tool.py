# ASI02: Tool Abuse — shell tool exposed to agent
# Vulnerability: Agent has access to shell/terminal tool
# Expected: AgentGuard ASI02-TOOL-ABUSE CRITICAL
tool_name = "shell"
tool_config = {"command": "bash", "args": ["-c"], "timeout": 30}
agent.register_tool(tool_name, tool_config)
