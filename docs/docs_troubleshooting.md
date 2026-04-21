# Troubleshooting Guide

## Common Issues

### No Satellite Lock

**Symptoms:** IDU `ACQUIRE` LED blinking, no signal quality reading.

**Checks:**
1. Verify dish points south (~162° azimuth for most of Pakistan).
2. Check for physical obstructions (trees, buildings, walls).
3. Inspect coax connectors for moisture or damage.
4. Run: `python3 scripts/align_antenna.py --scan`

---

### Low Signal Quality (< 60%)

**Causes & Fixes:**
| Cause | Fix |
|---|---|
| Misaligned dish | Re-run alignment wizard |
| Rain fade | Wait — signal recovers automatically |
| Dirty reflector | Clean dish surface |
| Faulty LNB | Replace ODU LNB |

---

### No IP Address Assigned

```bash
# Check DHCP status
paksat-config --status dhcp

# Force renew
paksat-config --dhcp-renew
```

If static IP is required, contact your provisioner for correct APN settings.

---

### High Latency (> 1000ms)

Geostationary satellite latency is **inherently ~600–700ms** round-trip. Values above 900ms indicate:
- Network congestion on beam
- Modem processing overhead — try firmware update
- Incorrect QoS settings

---

### Config Tool Won't Connect to IDU

1. Confirm PC is on `192.168.100.0/24` subnet.
2. Try: `ping 192.168.100.1`
3. Check Ethernet cable and port LEDs.
4. Factory reset IDU: hold reset button 10s (warning: erases config).

---

## Diagnostic Commands

```bash
# Full system health report
python3 scripts/health_check.py --verbose --json > report.json

# Live signal monitor
python3 scripts/signal_monitor.py --interval 5

# Firmware version
paksat-config --version

# Export logs
paksat-config --export-logs ./logs/
```

---

## Contact Support

If issues persist:  
📧 support@paksat.com.pk  
🌐 https://paksat.com.pk/hts/support
