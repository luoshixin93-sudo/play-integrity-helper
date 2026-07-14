"""ADB device manager for play-integrity-helper."""
import subprocess
import os

class DeviceManager:
    """Manage Android device via ADB."""

    def __init__(self, device):
        self.device = device

    def push_config(self, local_path):
        """Push pif.json to device."""
        remote_path = "/data/adb/PlayIntegrityFix/pif.json"
        print(f"Pushing {local_path} to {self.device}:{remote_path}")
        subprocess.run(
            f"adb -s {self.device} push {local_path} {remote_path}",
            shell=True,
            check=True,
        )
        # Set correct permissions
        subprocess.run(
            f"adb -s {self.device} shell chmod 644 {remote_path}",
            shell=True,
            check=True,
        )

    def reboot(self):
        """Reboot the device."""
        subprocess.run(f"adb -s {self.device} reboot", shell=True, check=True)

    def connect(self):
        """Connect to device via ADB."""
        subprocess.run(f"adb connect {self.device}", shell=True, check=True)
