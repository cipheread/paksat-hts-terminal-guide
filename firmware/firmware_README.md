# Firmware

This directory contains official firmware releases for the PAKSAT HTS 0.98m User Terminal.

## Directory Structure

```
firmware/
└── releases/
    ├── v1.2.0/
    │   ├── paksat-hts-firmware-v1.2.0.bin
    │   └── release-notes.md
    └── v1.1.3/
        ├── paksat-hts-firmware-v1.1.3.bin
        └── release-notes.md
```

## Updating Firmware

### Via Config Tool (Recommended)
```bash
paksat-config --firmware-update firmware/releases/v1.2.0/paksat-hts-firmware-v1.2.0.bin
```

### Manual via Web UI
1. Navigate to `http://192.168.100.1`
2. Go to **Administration → Firmware Update**
3. Select the `.bin` file and click **Upload**
4. Do not power off during update (~5 minutes)

## Verifying Firmware Integrity

Each release includes a SHA-256 checksum:
```bash
sha256sum -c paksat-hts-firmware-v1.2.0.bin.sha256
```

## ⚠️ Warning

Only flash firmware provided in official releases from this repository or PAKSAT support. Unofficial firmware may damage the terminal and void the warranty.
