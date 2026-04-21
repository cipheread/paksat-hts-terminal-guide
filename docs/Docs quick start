# Quick Start Guide — PAKSAT HTS User Terminal

## Prerequisites

- 0.98m PAKSAT HTS dish + ODU (Outdoor Unit)
- Coaxial cable (RG-6 or equivalent, max 30m recommended)
- Indoor Modem Unit (IDU)
- Ethernet cable (Cat5e or better)
- Compass and inclinometer (for manual alignment)
- Laptop/PC for configuration

---

## Step 1: Mount the Antenna

1. Select a mounting location with **clear southern sky view** (Pakistan coverage: ~162°E azimuth for PakSat-MM1).
2. Secure the mast mount to a rigid surface.
3. Attach the 0.98m reflector to the mount arm.
4. Do **not** fully tighten azimuth/elevation bolts yet — leave adjustable.

---

## Step 2: Cable the System

```
[Dish/ODU] ──── Coax (F-connector) ──── [IDU/Modem] ──── Ethernet ──── [Router/PC]
```

- Use weatherproof F-connectors on the outdoor end.
- Ground the coax at the entry point per local electrical code.

---

## Step 3: Power On

1. Connect IDU to AC power (90–264 VAC).
2. IDU LEDs sequence: **POWER → BOOT → ACQUIRE**
3. Wait 2–3 minutes for full initialization.

---

## Step 4: Point the Antenna

### Automatic (Recommended)
```bash
python3 scripts/align_antenna.py --satellite PAKSAT-MM1 --location "30.3753,69.3451"
```
Follow the audio/visual feedback on signal strength.

### Manual
Use the lookup table in [`hardware/antenna-alignment/azimuth-elevation-table.md`](../hardware/antenna-alignment/azimuth-elevation-table.md) for your city.

**Target:** Signal quality ≥ 75%, SNR ≥ 9 dB

---

## Step 5: Configure Network

```bash
# Default IDU IP
http://192.168.100.1

# Or via CLI
paksat-config --set mode=dhcp
paksat-config --apply
```

Default credentials:
- **Username:** `admin`
- **Password:** `paksat123` ← Change immediately!

---

## Step 6: Verify

```bash
python3 scripts/health_check.py --verbose
```

Expected output:
```
[OK] Satellite lock: PakSat-MM1
[OK] Signal quality: 82%
[OK] SNR: 11.4 dB
[OK] IP assigned: 203.x.x.x
[OK] Ping to 8.8.8.8: 650ms
```

---

## ✅ You're Online!

For advanced configuration, see [network-setup.md](network-setup.md).  
For issues, see [troubleshooting.md](troubleshooting.md).
