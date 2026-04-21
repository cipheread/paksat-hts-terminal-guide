<div align="center">

<img src="https://img.shields.io/badge/Cedar-C3%205G%20Router-0066CC?style=for-the-badge&logo=router&logoColor=white" />

# Cedar C3 5G Aggregation Router

### Complete Technical Guide & Configuration Reference

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![5G Ready](https://img.shields.io/badge/5G-Ready-brightgreen?style=flat-square)](docs/connectivity.md)
[![Multi-WAN](https://img.shields.io/badge/Multi--WAN-3%20Links-blue?style=flat-square)](docs/load-balancing.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange?style=flat-square)](CONTRIBUTING.md)

**[📡 Connectivity](docs/connectivity.md) · [⚡ Load Balancing](docs/load-balancing.md) · [🔄 Failover](docs/failover.md) · [⚙️ Setup](docs/setup.md) · [❓ FAQ](docs/faq.md)**

</div>

---

## What is the Cedar C3?

The **Cedar C3** is an enterprise-grade **5G Aggregation Router** that bonds up to **3 simultaneous internet connections** — one wired Ethernet WAN and two cellular SIM cards — into a single reliable, high-throughput connection.

```
┌──────────────────────────────────────────────────────┐
│                  Cedar C3 5G Router                  │
│                                                      │
│   SIM 1 [5G/LTE] ──┐                                │
│   SIM 2 [5G/LTE] ──┼──► Aggregation Engine ──► LAN  │
│   WAN  [Ethernet] ──┘                                │
│                                                      │
│   Load Balance · Failover · Traffic Steering         │
└──────────────────────────────────────────────────────┘
```

> **"Aggregation"** means it combines all links — not just switches between them.

---

## ✨ Feature Highlights

| Feature | Details |
|---|---|
| 🔀 **Multi-WAN Aggregation** | Combine WAN + SIM1 + SIM2 simultaneously |
| 🔁 **Auto Failover** | Switches to SIM in ~10s if WAN drops |
| 📶 **Dual 5G SIM** | Two active SIM slots, different carriers supported |
| 🚦 **QoS & Traffic Priority** | Prioritize VoIP, video, or critical apps |
| 🔒 **VPN Support** | IPSec, L2TP, OpenVPN passthrough |
| 🌍 **VLAN** | Network segmentation support |
| 📊 **Live Monitoring** | Real-time bandwidth per WAN link |
| 🌐 **SD-WAN-like Steering** | Policy-based routing per IP/protocol |

---

## 📂 Documentation

| Document | Description |
|---|---|
| [📡 Connectivity Guide](docs/connectivity.md) | SIM vs WAN — types, speeds, use cases |
| [🔄 Failover Guide](docs/failover.md) | What happens when WAN goes down |
| [⚡ Load Balancing Guide](docs/load-balancing.md) | How traffic aggregation works |
| [⚙️ Setup Guide](docs/setup.md) | Step-by-step configuration |
| [🔧 Troubleshooting](docs/troubleshooting.md) | Common issues & fixes |
| [❓ FAQ](docs/faq.md) | Frequently asked questions |
| [📐 Specifications](docs/specifications.md) | Full technical specs |

---

## 🚀 Quick Start

```bash
# 1. Access the router web UI
Open browser → http://192.168.1.1

# 2. Login
Username: admin
Password: admin  ← Change immediately!

# 3. Go to
Network → Multi-WAN → Enable Load Balancing
```

Full setup walkthrough → [docs/setup.md](docs/setup.md)

---

## 🤝 Contributing

Found an error or want to add carrier APN settings for your country? Contributions are welcome!  
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

⭐ **If this guide helped you, please star the repo!** ⭐

</div>
