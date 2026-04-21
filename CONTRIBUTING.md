# Contributing to PAKSAT HTS Terminal

Thank you for your interest in contributing! Here's how to get started.

## Code of Conduct

Be respectful and professional. This project serves critical infrastructure.

## How to Contribute

### Reporting Bugs
1. Search [existing issues](../../issues) first.
2. Open a new issue using the **Bug Report** template.
3. Include: terminal firmware version, OS, steps to reproduce, expected vs actual behavior.

### Submitting Pull Requests
1. Fork the repository.
2. Create a branch: `git checkout -b fix/your-fix-name`
3. Make your changes and add tests where applicable.
4. Run the test suite: `pytest tests/ -v`
5. Commit with a clear message: `git commit -m "fix: correct azimuth offset for southern beam"`
6. Push and open a Pull Request against `main`.

### Commit Message Format
Use [Conventional Commits](https://www.conventionalcommits.org/):
```
feat: add SNMP monitoring support
fix: resolve DHCP lease renewal loop
docs: update antenna alignment guide
chore: bump dependency versions
```

## Development Setup

```bash
git clone https://github.com/paksat-hts/terminal.git
cd terminal
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Review Process

All PRs are reviewed by the PAKSAT engineering team. Expect a response within 5 business days.
