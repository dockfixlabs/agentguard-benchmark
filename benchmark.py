"""AgentGuard Benchmark runner -- scan all samples and report detection rates."""

import json
import subprocess
import sys
from pathlib import Path
from collections import defaultdict


def run_benchmark(samples_dir: str = "samples"):
    base = Path(samples_dir)
    results = defaultdict(lambda: {"total": 0, "detected": 0, "false_positives": 0})
    all_findings = []

    for category_dir in sorted(base.iterdir()):
        if not category_dir.is_dir():
            continue
        category = category_dir.name
        for sample_file in sorted(category_dir.glob("*.py")):
            results[category]["total"] += 1
            try:
                output = subprocess.check_output(
                    ["agentguard", str(sample_file), "--format", "json"],
                    timeout=10,
                    text=True,
                )
                data = json.loads(output)
                findings = data.get("findings", [])
            except (subprocess.SubprocessError, json.JSONDecodeError, FileNotFoundError):
                findings = []

            if category == "clean":
                if findings:
                    results[category]["false_positives"] += 1
                    all_findings.append({"file": str(sample_file), "category": category, "findings": findings})
            else:
                if findings:
                    results[category]["detected"] += 1
                all_findings.append({"file": str(sample_file), "category": category, "findings": findings})

    # Print report
    print("=" * 60)
    print("AgentGuard Benchmark Report")
    print("=" * 60)
    print()
    print(f"{'Category':<12} {'Total':>6} {'Detected':>10} {'Rate':>8} {'FP':>5}")
    print("-" * 45)

    total_samples = 0
    total_detected = 0
    total_fp = 0

    for cat in sorted(results.keys()):
        r = results[cat]
        rate = f"{(r['detected']/r['total']*100):.0f}%" if r["total"] > 0 and cat != "clean" else "--"
        if cat == "clean":
            rate = f"{(1 - r['false_positives']/r['total']*100):.0f}%"
        print(f"{cat:<12} {r['total']:>6} {r['detected']:>10} {rate:>8} {r['false_positives']:>5}")
        total_samples += r["total"]
        if cat != "clean":
            total_detected += r["detected"]
        total_fp += r["false_positives"]

    clean_total = results.get("clean", {}).get("total", 0)
    vuln_total = total_samples - clean_total

    print("-" * 45)
    if vuln_total > 0:
        print(f"{'TOTAL':<12} {total_samples:>6} {total_detected:>10} {(total_detected/vuln_total*100):.0f}% {total_fp:>5}")
    else:
        print(f"{'TOTAL':<12} {total_samples:>6} {total_detected:>10} {'--':>8} {total_fp:>5}")
    print()
    print(f"False positives: {total_fp}")
    if vuln_total > 0:
        print(f"Detection rate: {(total_detected/vuln_total*100):.1f}%")
    print()

    # Output JSON
    if "--json" in sys.argv:
        print(json.dumps({"results": dict(results), "findings": all_findings}, indent=2))


if __name__ == "__main__":
    run_benchmark()
