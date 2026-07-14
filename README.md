# play-integrity-helper

**One-click Play Integrity helper for cloud phones.**  
Run your Android cloud phones on [qtphone.com](https://www.qtphone.com) and pass Google Play Integrity checks without manual configuration.

[![GitHub stars](https://img.shields.io/github/stars/luoshixin93-sudo/play-integrity-helper)](https://github.com/luoshixin93-sudo/play-integrity-helper)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](LICENSE)

---

## What is this?

`play-integrity-helper` is a Python CLI tool + helper script that automates the process of configuring a cloud phone to pass **Google Play Integrity API** checks. It works alongside [PlayIntegrityFix](https://github.com/chiteroman/PlayIntegrityFix) and [Universal SafetyNet Fix](https://github.com/kdrag0n/safetynet-fix).

Instead of manually editing Magisk modules and JSON configs, just run one command and the helper does it for you.

---

## Features

- Automatic device fingerprint configuration for Play Integrity
- One-command Magisk module setup for cloud phones
- Compatible with Zygisk-based environments
- JSON config generator for PlayIntegrityFix `pif.json`
- Health check: verify your device passes Play Integrity after setup
- Works on: Android 8.0 - Android 15
- Built-in support for popular cloud phone platforms

---

## Prerequisites

Before using play-integrity-helper, you need:

1. **Root access** on your cloud phone (Magisk or KernelSU)
2. **Zygisk** enabled in Magisk settings
3. **PlayIntegrityFix module** installed ([Download](https://github.com/chiteroman/PlayIntegrityFix/releases))
4. **Python 3.8+** on your local machine (not on the phone)
5. **ADB access** to your cloud phone

---

## Installation

### Via pip

```bash
pip install play-integrity-helper
```

### Manual

```bash
git clone https://github.com/luoshixin93-sudo/play-integrity-helper.git
cd play-integrity-helper
pip install -r requirements.txt
```

---

## Usage

### Quick Start

```bash
# Connect your cloud phone via ADB, then:
python -m play_integrity_helper setup --device <device-ip>:5555
```

### Full Workflow

```bash
# Step 1: Check current integrity status
python -m play_integrity_helper check --device 192.168.1.100:5555

# Step 2: Generate config for your device model
python -m play_integrity_helper config --model "Pixel 6" --manufacturer "Google"

# Step 3: Push config to device
python -m play_integrity_helper push --device 192.168.1.100:5555 --config pif.json

# Step 4: Reboot and verify
python -m play_integrity_helper verify --device 192.168.1.100:5555
```

### Configuration File

The helper generates a `pif.json` based on your target device profile:

```json
{
  "FINGERPRINT": "google/oriole/oriole:14/UP1A.231005.007/10855636:user/release-keys",
  "MANUFACTURER": "Google",
  "MODEL": "Pixel 6",
  "DEVICE": "oriole",
  "BRAND": "google",
  "PRODUCT": "oriole",
  "SECURITY_PATCH": "2025-01-05",
  "BUILD_INFO": "google/oriole/oriole:14/UP1A.231005.007/10855636:user/release-keys"
}
```

---

## Cloud Phone Compatibility

Tested on cloud phone platforms including:

| Platform | Status | Notes |
|----------|--------|-------|
| qtphone.com | ✅ Full Support | Pre-tested images available |
| Custom cloud phones | ✅ Manual config | Use `config` command |

---

## Architecture

```
play-integrity-helper/
├── play_integrity_helper/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── checker.py          # Integrity status checker
│   ├── config_gen.py       # pif.json generator
│   ├── device.py           # ADB device manager
│   └── constants.py        # Fingerprint database
├── scripts/
│   ├── install_deps.sh     # Install Magisk module helper
│   └── adb_helper.sh       # ADB convenience scripts
├── requirements.txt
└── setup.py
```

---

## Troubleshooting

### Still failing Play Integrity after setup?

1. Make sure **Zygisk** is enabled in Magisk settings
2. Clear Google Play Services data: `adb shell pm clear com.google.android.gms`
3. Re-run verification: `python -m play_integrity_helper verify`
4. Check [PlayIntegrityFix Issues](https://github.com/chiteroman/PlayIntegrityFix/issues)

### ADB connection issues?

```bash
# Enable wireless ADB on your cloud phone
adb tcpip 5555
adb connect <device-ip>:5555
```

---

## References & Credits

This project works alongside these amazing open-source projects:

- [PlayIntegrityFix](https://github.com/chiteroman/PlayIntegrityFix) - Core Magisk module
- [Universal SafetyNet Fix](https://github.com/kdrag0n/safetynet-fix) - SafetyNet bypass
- [YASNAC](https://github.com/RikkaApps/YASNAC) - Integrity checker

---

## License

**GPL-3.0** - This project is open source under GPL-3.0 license.  
Note: The PlayIntegrityFix and Universal SafetyNet Fix modules it interacts with are also GPL-3.0.

---

## Cloud Phone Infrastructure

Deploy and manage your own cloud phone fleet at scale:

👉 **[qtphone.com](https://www.qtphone.com)** - Cloud phone platform for developers and automation engineers.

Run Android apps at scale, automate testing, manage fleets — all from your browser.
