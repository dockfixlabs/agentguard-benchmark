# ASI10: Trust Boundary — self-modifying agent
# Vulnerability: Agent can write to its own source file
# Expected: AgentGuard ASI10-TRUST-BOUNDARY CRITICAL
import os
def update_self(new_code):
    with open(__file__, 'w') as f:
        f.write(new_code)
    os.system(f"python {__file__}")
