# ASI10: Trust Boundary — host filesystem access
# Vulnerability: Agent mounts host /etc directory
# Expected: AgentGuard ASI10-TRUST-BOUNDARY CRITICAL
volumes = {
    "/etc": {"bind": "/etc", "mode": "rw"},
    "/var/log": {"bind": "/logs", "mode": "ro"},
    "/root": {"bind": "/agent-root", "mode": "rw"}
}
