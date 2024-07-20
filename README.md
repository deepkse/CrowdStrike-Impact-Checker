# CrowdStrike Impact Checker

This tool helps you determine if your system is impacted by the CrowdStrike update issue from July 19, 2024.

## Download and Use

1. Go to the [Releases](https://github.com/deepkse/CrowdStrike-Impact-Checker/releases) page.
2. Download the latest `CrowdStrikeImpactChecker.exe`.
3. Right-click the downloaded file and select "Run as administrator".
4. Follow the on-screen instructions.

![CrowdStrike Impact Checker](https://github.com/deepkse/CrowdStrike-Impact-Checker/blob/main/public/images/CrowdStrikeImpactChecker.png?raw=true)

## Building from Source

If you prefer to build the executable yourself:

1. Clone this repository.
2. Install pyinstaller: `pip install pyinstaller`
3. Run: `pyinstaller --onefile --name CrowdStrikeImpactChecker crowdstrike_impact_checker.py`
4. The executable will be in the `dist` folder.

## Output Interpretation

- "YOUR SYSTEM MAY BE IMPACTED": Your system has the problematic update. Follow the provided remediation steps provided by [Crowdstrike](https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/).
- "Your system has the fixed version": Your system should not be affected.
- "Unable to determine impact status": The tool couldn't conclusively determine your system's status. Monitor for any issues.

## Disclaimer

Always consult with your IT department before making system changes.