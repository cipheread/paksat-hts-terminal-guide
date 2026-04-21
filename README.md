# 🛰️ PAKSAT HTS User Terminal

<p align="center">
  <img src="https://paksat.com.pk/hts/assets/images/logo.png" alt="PAKSAT HTS" width="180"/>
</p>

<p align="center">
  <a href="https://github.com/paksat-hts/terminal/releases"><img src="https://img.shields.io/github/v/release/paksat-hts/terminal?color=blue&label=Release" alt="Release"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Proprietary-red.svg" alt="License"/></a>
  <a href="https://paksat.com.pk/hts/"><img src="https://img.shields.io/badge/Satellite-PakSat--MM1-green" alt="Satellite"/></a>
  <img src="https://img.shields.io/badge/Dish-0.98m-orange" alt="Dish Size"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status"/>
</p>

---

## Overview

The **PAKSAT HTS User Terminal** is a compact satellite internet terminal designed for high-speed broadband connectivity via the **PakSat-MM1** High-Throughput Satellite (HTS) — launched in May 2024 to bridge the digital divide across Pakistan, including remote and rural areas.

This repository contains official firmware, configuration tools, diagnostic utilities, hardware documentation, and integration guides for the PAKSAT HTS User Terminal.

---

## 🔑 Key Features

| Feature | Details |
|---|---|
| **Satellite** | PakSat-MM1 (HTS, launched May 2024) |
| **Dish Size** | 0.98m offset reflector |
| **Frequency Band** | Ka-band |
| **Form Factor** | Compact, portable, field-deployable |
| **Use Cases** | Rural broadband, VSAT enterprise, disaster recovery, mobility |
| **Coverage** | Pakistan + regional beam |

---

## 📁 Repository Structure

```
paksat-hts-terminal/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
│
├── firmware/                    # Terminal firmware images & release notes
│   ├── releases/
│   └── README.md
│
├── software/
│   ├── driver/                  # OS-level drivers for modem interface
│   ├── config-tool/             # GUI/CLI terminal configuration utility
│   └── diagnostics/             # Signal, link, and network diagnostics
│
├── hardware/                    # Hardware documentation and schematics
│   ├── installation-guide/
│   ├── antenna-alignment/
│   └── specs/
│
├── docs/                        # Full technical documentation
│   ├── quick-start.md
│   ├── network-setup.md
│   ├── troubleshooting.md
│   └── api-reference.md
│
├── tests/                       # Automated test suites
│
├── scripts/                     # Utility scripts (provisioning, health checks)
│
└── .github/
    ├── workflows/               # CI/CD pipelines
    └── ISSUE_TEMPLATE/          # Bug & feature request templates
```

---

## 🚀 Quick Start

### 1. Physical Installation
See [`hardware/installation-guide/`](hardware/installation-guide/) for full mechanical mounting, cabling, and grounding instructions.

### 2. Antenna Alignment
```bash
# Run alignment assistant (requires USB connection to terminal)
python3 scripts/align_antenna.py --satellite PAKSAT-MM1
```
Refer to [`hardware/antenna-alignment/`](hardware/antenna-alignment/) for azimuth/elevation tables by region.

### 3. Terminal Configuration
```bash
# Install the config tool
pip install paksat-hts-config

# Launch GUI
paksat-config --gui

# Or configure via CLI
paksat-config --set apn=hts.paksat.com --set auth=chap
```

### 4. Verify Connectivity
```bash
python3 scripts/health_check.py --verbose
```

---

## 📡 Technical Specifications

```
Antenna Reflector  : 0.98m offset parabolic
Frequency (Tx)     : 27.5–30.0 GHz (Ka-band)
Frequency (Rx)     : 17.7–20.2 GHz (Ka-band)
EIRP               : ≥ 48 dBW
G/T                : ≥ 12.5 dB/K
Modem Interface    : Ethernet (RJ-45), 100/1000 Mbps
Power Supply       : 90–264 VAC, 50/60 Hz
Operating Temp     : -10°C to +55°C
IP Rating          : IP55 (outdoor unit)
```

---

## 📖 Documentation

- [Quick Start Guide](docs/quick-start.md)
- [Network Setup & IP Configuration](docs/network-setup.md)
- [Troubleshooting Guide](docs/troubleshooting.md)
- [API Reference](docs/api-reference.md)
- [Firmware Changelog](CHANGELOG.md)

---

## 🛠️ Development

### Prerequisites
- Python 3.9+
- Node.js 18+ (for web-based config tool)
- Git

### Setup
```bash
git clone https://github.com/paksat-hts/terminal.git
cd terminal
pip install -r requirements.txt
npm install --prefix software/config-tool
```

### Running Tests
```bash
pytest tests/ -v
```

---

## 🐛 Reporting Issues

Use the [GitHub Issues](../../issues) tracker:
- **Bug Report** → Use the `bug_report.md` template
- **Feature Request** → Use the `feature_request.md` template
- **Security Vulnerability** → See [SECURITY.md](SECURITY.md) (**do not open a public issue**)

---

## 🤝 Contributing

We welcome contributions from the community. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests.

---

## 📄 License

This repository is maintained by **PAKSAT / SUPARCO**. Firmware and hardware documentation are proprietary. Software utilities are released under the terms specified in [LICENSE](LICENSE).

---

## 📞 Support

| Channel | Contact |
|---|---|
| Technical Support | support@paksat.com.pk |
| Sales & Provisioning | hts@paksat.com.pk |
| Website | https://paksat.com.pk/hts/ |
| Address | SUPARCO, Sector 28, Gulzar-e-Hijri, Karachi |

---

<p align="center">
  <sub>© PAKSAT / SUPARCO — Connecting Pakistan from Space 🇵🇰</sub>
</p>
