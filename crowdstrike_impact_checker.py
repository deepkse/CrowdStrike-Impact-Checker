import os
import datetime
import ctypes
import sys

class CrowdStrikeImpactChecker:
    def __init__(self):
        self.crowdstrike_path = r"C:\Windows\System32\drivers\CrowdStrike"
        self.problematic_version = "0409 UTC"
        self.fixed_version = "0527 UTC"

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def check_crowdstrike_installed(self):
        return os.path.exists(self.crowdstrike_path)

    def get_channel_file_version(self):
        for file in os.listdir(self.crowdstrike_path):
            if file.startswith("C-00000291"):
                file_path = os.path.join(self.crowdstrike_path, file)
                timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                return timestamp.strftime("%H%M UTC")
        return None

    def is_system_impacted(self):
        version = self.get_channel_file_version()
        if version == self.problematic_version:
            return True
        elif version >= self.fixed_version:
            return False
        else:
            return "Unknown"

    def provide_remediation_steps(self):
        steps = [
            "1. Reboot your system to attempt downloading the fixed channel file.",
            "2. If the system crashes again:",
            "   a. Boot into Safe Mode or Windows Recovery Environment.",
            "   b. Navigate to C:\\Windows\\System32\\drivers\\CrowdStrike.",
            "   c. Delete the file matching 'C-00000291*.sys'.",
            "   d. Boot the system normally.",
            "3. If issues persist, contact your IT support team."
        ]
        return "\n".join(steps)

    def run_analysis(self):
        print("CrowdStrike Impact Checker")
        print("-------------------------")

        if not self.is_admin():
            print("This script requires administrative privileges.")
            print("Please run it as an administrator.")
            input("Press Enter to exit...")
            sys.exit()

        if not self.check_crowdstrike_installed():
            print("CrowdStrike is not installed on this system.")
            input("Press Enter to exit...")
            return

        impact_status = self.is_system_impacted()

        if impact_status == True:
            print("\nYOUR SYSTEM MAY BE IMPACTED by the problematic update.")
            print("\nRemediation Steps:")
            print(self.provide_remediation_steps())
        elif impact_status == False:
            print("\nYour system has the fixed version and should not be impacted.")
        else:
            print("\nUnable to determine impact status. Please monitor your system for any issues.")

        input("\nPress Enter to exit...")

if __name__ == "__main__":
    checker = CrowdStrikeImpactChecker()
    checker.run_analysis()