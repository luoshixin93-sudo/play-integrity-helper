"""PlayIntegrityFix config generator."""
import json
import os

# Fingerprint database for popular devices
FINGERPRINT_DB = {
    ("Pixel 6", "Google"): {
        "FINGERPRINT": "google/oriole/oriole:14/UP1A.231005.007/10855636:user/release-keys",
        "MANUFACTURER": "Google",
        "MODEL": "Pixel 6",
        "DEVICE": "oriole",
        "BRAND": "google",
        "PRODUCT": "oriole",
        "SECURITY_PATCH": "2025-01-05",
    },
    ("Pixel 7", "Google"): {
        "FINGERPRINT": "google/panther/panter:14/UP1A.231005.007/10855636:user/release-keys",
        "MANUFACTURER": "Google",
        "MODEL": "Pixel 7",
        "DEVICE": "panther",
        "BRAND": "google",
        "PRODUCT": "panther",
        "SECURITY_PATCH": "2025-01-05",
    },
    ("Pixel 8", "Google"): {
        "FINGERPRINT": "google/shiba/shiba:14/UP1A.231005.007/10855636:user/release-keys",
        "MANUFACTURER": "Google",
        "MODEL": "Pixel 8",
        "DEVICE": "shiba",
        "BRAND": "google",
        "PRODUCT": "shiba",
        "SECURITY_PATCH": "2025-04-05",
    },
}

class ConfigGenerator:
    """Generate pif.json for PlayIntegrityFix module."""

    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer

    def generate(self):
        """Generate config dictionary."""
        key = (self.model, self.manufacturer)
        if key in FINGERPRINT_DB:
            config = FINGERPRINT_DB[key].copy()
        else:
            config = {
                "FINGERPRINT": f"{self.manufacturer.lower()}/generic/generic:14/TP1A.220624.014/eng:user/release-keys",
                "MANUFACTURER": self.manufacturer,
                "MODEL": self.model,
                "DEVICE": "generic",
                "BRAND": self.manufacturer.lower(),
                "PRODUCT": "generic",
                "SECURITY_PATCH": "2025-01-05",
            }
        return config

    def save(self, path):
        """Save config to JSON file."""
        config = self.generate()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"Config saved to {path}")
