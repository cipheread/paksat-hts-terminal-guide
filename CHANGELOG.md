# Changelog

All notable changes to the PAKSAT HTS User Terminal software are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Planned
- Web-based configuration portal
- Remote firmware OTA update support
- SNMP v3 monitoring integration

---

## [1.2.0] - 2025-03-10

### Added
- Antenna alignment wizard with live signal strength meter
- Support for static IP provisioning via CLI
- Detailed link quality diagnostics (SNR, BER, MER)

### Changed
- Improved modem initialization time by ~18%
- Updated Ka-band frequency tables for PakSat-MM1 new transponders

### Fixed
- Fixed rare boot loop when DHCP lease renewal failed
- Corrected azimuth calculation bug for northern Pakistan regions

---

## [1.1.3] - 2024-11-20

### Fixed
- Fixed IP conflict during dual-NIC configuration
- Resolved config tool crash on Windows 11 22H2

---

## [1.1.0] - 2024-08-05

### Added
- Initial public release of `paksat-hts-config` CLI tool
- Health check script with JSON output support
- Hardware installation guide (PDF + Markdown)

### Changed
- Firmware v1.1.0 with improved rain fade recovery algorithm

---

## [1.0.0] - 2024-06-01

### Added
- Initial release following PakSat-MM1 satellite launch (May 2024)
- Base firmware for 0.98m user terminal
- Basic configuration and diagnostic utilities
