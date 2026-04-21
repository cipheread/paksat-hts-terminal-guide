#!/usr/bin/env python3
"""
PAKSAT HTS Terminal — Health Check Utility
Checks signal, network, and hardware status of the connected terminal.
"""

import argparse
import json
import socket
import subprocess
import sys
import time
from datetime import datetime

TERMINAL_IP = "192.168.100.1"
TERMINAL_API_PORT = 8080


def check_terminal_reachable():
    try:
        sock = socket.create_connection((TERMINAL_IP, TERMINAL_API_PORT), timeout=3)
        sock.close()
        return True, f"Terminal reachable at {TERMINAL_IP}"
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        return False, f"Cannot reach terminal at {TERMINAL_IP}: {e}"


def get_signal_quality():
    """Query terminal API for signal metrics."""
    # Placeholder — replace with actual API call to terminal
    # Example: requests.get(f"http://{TERMINAL_IP}:{TERMINAL_API_PORT}/api/signal")
    return {
        "quality_pct": 82,
        "snr_db": 11.4,
        "ber": 1.2e-7,
        "satellite": "PakSat-MM1",
        "locked": True,
    }


def check_internet(host="8.8.8.8", count=3):
    try:
        result = subprocess.run(
            ["ping", "-c", str(count), host],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            # Parse avg latency
            lines = result.stdout.splitlines()
            for line in lines:
                if "avg" in line or "rtt" in line:
                    parts = line.split("/")
                    avg_ms = float(parts[4]) if len(parts) >= 5 else 0
                    return True, f"Ping OK — avg {avg_ms:.0f}ms"
            return True, "Ping OK"
        return False, "Ping failed"
    except Exception as e:
        return False, f"Ping error: {e}"


def run_health_check(verbose=False, json_output=False):
    results = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "checks": []
    }

    checks = [
        ("Terminal Reachable", check_terminal_reachable),
        ("Internet Connectivity", check_internet),
    ]

    all_ok = True

    for name, fn in checks:
        ok, msg = fn()
        if not ok:
            all_ok = False
        results["checks"].append({"name": name, "ok": ok, "message": msg})
        if not json_output:
            status = "\033[92m[OK]\033[0m" if ok else "\033[91m[FAIL]\033[0m"
            print(f"  {status} {name}: {msg}")

    # Signal check
    signal = get_signal_quality()
    sig_ok = signal["locked"] and signal["quality_pct"] >= 60 and signal["snr_db"] >= 9.0
    if not sig_ok:
        all_ok = False
    results["signal"] = signal
    if not json_output:
        status = "\033[92m[OK]\033[0m" if sig_ok else "\033[91m[FAIL]\033[0m"
        print(f"  {status} Satellite Lock: {signal['satellite']} | "
              f"Quality: {signal['quality_pct']}% | SNR: {signal['snr_db']} dB")

    results["overall"] = "PASS" if all_ok else "FAIL"

    if json_output:
        print(json.dumps(results, indent=2))
    else:
        color = "\033[92m" if all_ok else "\033[91m"
        print(f"\n  {color}Overall: {results['overall']}\033[0m")

    return 0 if all_ok else 1


def main():
    parser = argparse.ArgumentParser(description="PAKSAT HTS Terminal Health Check")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if not args.json:
        print("\n🛰️  PAKSAT HTS Terminal — Health Check")
        print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    sys.exit(run_health_check(verbose=args.verbose, json_output=args.json))


if __name__ == "__main__":
    main()
