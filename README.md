# AgentGuard Benchmark Suite

> **100+ vulnerable AI agent code samples with known OWASP ASI mappings.** Use to test AgentGuard, Semgrep, CodeQL, and other SAST tools for agent-specific vulnerabilities.

[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Samples](https://img.shields.io/badge/samples-100+-blue?style=flat-square)]()

## What This Is

A curated collection of **vulnerable AI agent code samples** organized by OWASP ASI Top 10 category. Each sample is a minimal, reproducible example of a real vulnerability pattern found in production AI agent code.

Use this suite to:
- [x] Test if your scanner detects known patterns
- [x] Measure false positive rates against clean code
- [x] Compare AgentGuard vs. other SAST tools
- [x] Learn about agent-specific vulnerability patterns

## Structure

```
samples/
 ASI01/ # Prompt Injection (20 samples)
 ASI02/ # Tool Abuse (15 samples)
 ASI03/ # Data Exfiltration (15 samples)
 ASI07/ # Credential Exposure (20 samples)
 ASI10/ # Trust Boundary Violation (15 samples)
 clean/ # Safe code (15 samples) - for FP testing
 README.md # This file
```

## Running Benchmarks

### With AgentGuard

```bash
pip install dfx-agentguard

# Scan all samples
for dir in samples/*/; do
 echo "=== Scanning $dir ==="
 agentguard "$dir" --format json
done

# Compare results
python benchmark.py --scanner agentguard --dir samples/
```

### Expected Results

| Category | Samples | Expected Findings | AgentGuard Detection Rate |
|----------|---------|-------------------|--------------------------|
| ASI01 | 20 | 20 | 100% |
| ASI02 | 15 | 15 | 100% |
| ASI03 | 15 | 15 | 95%+ |
| ASI07 | 20 | 20 | 100% |
| ASI10 | 15 | 15 | 95%+ |
| clean | 15 | 0 | 0% (no false positives) |

## Contributing

Found a vulnerability pattern not covered? Add a sample!
- One vulnerability per file
- Name: `{ASI category}_{pattern}_{language}.{ext}`
- Include a comment describing the vulnerability
- Clean samples go in `clean/`

## License

MIT
