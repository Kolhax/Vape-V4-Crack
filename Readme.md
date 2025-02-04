# Vape Cracked

![Vape_V4](images/Vape_V4.png)    ![Vape_Lite](images/Vape_lite.png)

Vape offers an advanced cheating solution for Minecraft that integrates seamlessly into Forge versions of the game. Renowned for its simplicity and robust stealth capabilities, Vape ensures secure and undetectable injection of cheats, providing a significant edge in gameplay.

## Official Vape Website
For purchases, visit the official website:
[https://www.vape.gg/](https://www.vape.gg/)

---

## Project Status

- **This repository is no longer actively maintained.**  
  Major updates and modifications will be done in a separate repository. This repository is kept as an archive for historical and reference purposes.  
- **Feel free to fork the project and submit pull requests.** I will review them and appreciate any contributions.  
- **This repository has been archived multiple times** to ensure the code is preserved and never lost.  
- **A self-hosted [Gitea](https://github.com/go-gitea/gitea) instance** is also used for backup purposes. The domain is private for now due to server limitations.  
- **Check the [Archive](https://web.archive.org/web/*/https://github.com/Kolhax/Vape-V4-Crack)** for historical snapshots of this repository.
--> PS: if you pass by here, mind saving it too?, it take ~10s and it make keep our repo alive 😊 -> [SAVE IT](https://web.archive.org/save/https://github.com/Kolhax/Vape-V4-Crack)

---

## Update Messages

### 12/22/2024
- **Launcher.py** has been created.  
  - It’s far from perfect and may not start Vape properly. If it doesn’t start automatically, you can manually start it. At least the server will be running.  
- **Newer Video**: [Watch Here](https://archive.org/details/vape-v-4.mp-4)

### 12/21/2024
- **New Discord Server**: [Join Here](https://discord.gg/jFg7quHz)  
- **Environment Fixes**:  
  - Many users reported issues with the environment setup. The only reliable solution is to use the exact environment (ENV) from the first version/backup.  
  - A better tutorial or guide is in the works. For now, use the `env` folder as specified in the "VENV" instructions.  

**Quick Start**  
If you simply want to run the script without setting up a new environment, you can execute:  
```bash
env\Scripts\python.exe server.py
```

**Environment Files**  
Check the releases section for two downloadable files:  
- `env.zip`: Contains only the environment files (a copy of Python and all dependencies).  
- `full.zip`: A complete backup with the `venv` and everything pre-configured, ready to start.  

**Future Plans**  
- A simple launcher is being considered to make starting Vape easier.  
- The setup process has proven challenging for some users, and individual support is no longer feasible.  

**Key Learnings**  
1. The **Python version** is critical.  
2. Some dependencies must be updated or installed with the correct versions.  

For reference, a `freeze.txt` file (the result of running `pip freeze` in my environment) is included in both the `vape-v4` and `Lite` folders. This should help you identify the exact dependencies and versions required for the setup.

---

## Installation Tutorial

### Prerequisites
1. **Install Python 3.11**:  
   - Ensure you tick the "Add to path" checkbox at the bottom of the installation window before clicking "Install Now".  

2. **Disable Real-Time Protection**:  
   - Temporarily disable real-time protection in your antivirus software to prevent any installation conflicts.  

3. **Install Minecraft Forge**:  
   - Download and install Forge for the desired version of Minecraft and launch the game to complete the Forge setup.  

### Setup Instructions
Execute the following commands in your terminal to set up the environment:

```bash
# Clone the repository to your desired folder
git clone https://github.com/Kolhax/Vape-V4-Crack

# Install the virtual environment
pip install pyvenv
cd "Vape V4 Cracked"
py -m venv env
env\Scripts\activate.bat
pip install -r requirements.txt

# Start the server
py server.py
```

To Start The Server, After First Installation:
```bash
env\Scripts\activate.bat
py server.py
```

### Starting the Software
After the server is set up, proceed with the following steps to start the software:  
- Navigate to the "Vape_V4" folder, which should contain:  
  - `kangaroo patcher.exe`  
  - `Kangaroo.dll`  
  - `Vape.exe`  

- With the server running, drag and drop `Vape.exe` onto `Kangaroo patcher.exe`. Allow a few seconds for the process to complete. The software is now ready for use.

---

## Instructional Videos
- [Older Video](https://web.archive.org/web/20231211230047/https://cdn.discordapp.com/attachments/1127981561820754011/1127982978388201472/2023-07-10_11-13-30.mp4)  
- [Newer Video](https://archive.org/details/vape-v-4.mp-4)  

---

## Frequently Asked Questions (FAQ)

- **Issue: 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'**  
  **OR: DLL load failed while importing _rust**  
  - Solution: Upgrade OpenSSL using the following command:  
    ```bash
    pip install pyopenssl --upgrade --force-reinstall
    ```

- **Issue: No module named 'websockets'**  
  - Solution: Install or upgrade the 'websockets' module:  
    ```bash
    pip install websockets --upgrade
    ```

---

## Support
For additional support, contact us via Discord:  
- **KolhaxDev**: `kolhaxdev`  
- **Discord Server**: [Join Here](https://discord.gg/jFg7quHz)  

---

## Donations
If you appreciate my work and would like to support me, even a small contribution of just one dollar would make a difference. Thank you so much in advance for your generosity!  
- **BTC**: `bc1qup9zrl9z94agmxjth4kqvyevdd6tysmf5th6hz`  
- **ETH**: `0x88229297934Dea144783188262268E36b5C8205b`  
- **Paypal**: [Donate Here](https://paypal.me/keparMC)  

---

**Note**: This repository is no longer actively maintained. Feel free to fork and contribute! 😇
