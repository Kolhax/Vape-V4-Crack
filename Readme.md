Note: I will not update the script further, feel free to fork the project and send push requests, ill read them and thanks for the help in advance

# Vape Cracked

Vape offers an advanced cheating solution for Minecraft that integrates seamlessly into Forge versions of the game. Renowned for its simplicity and robust stealth capabilities, Vape ensures secure and undetectable injection of cheats, providing a significant edge in gameplay.

## Official Vape Website
For purchases, visit the official website:
[https://www.vape.gg/](https://www.vape.gg/)

## Installation Tutorial

### Prerequisites
1. **Install Python 3.9**:
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

## Instructional Video
Watch the setup video here:
[Instructional Video](https://web.archive.org/web/20231211230047/https://cdn.discordapp.com/attachments/1127981561820754011/1127982978388201472/2023-07-10_11-13-30.mp4)

## Frequently Asked Questions (FAQ)

- **Issue: 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'**
  - Solution: Upgrade OpenSSL using the following command:
    ```bash
    pip install pyopenssl --upgrade --force-reinstall
    ```

- **Issue: No module named 'websockets'**
  - Solution: Install or upgrade the 'websockets' module:
    ```bash
    pip install websockets --upgrade
    ```

## Support
For additional support, contact us via Discord:
`kepardev`
