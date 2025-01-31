Note: I will not update the script further, feel free to fork the project and send push requests, ill read them and thanks for the help in advance 
- Major modifications will be done in an other repository, this piece of code is really fragile and precious, i keep it more as an archive.
- Know that this repo has been saved in the archive many times, to make sure this piece of code, this precious, never get lost.
- Also saved in a self hosted [Gitea](https://github.com/go-gitea/gitea), that is also saved on the archive <br>
😇 feel free to get check on your own -> [Archive](https://web.archive.org/web/*/https://github.com/Kolhax/Vape-V4-Crack), (The self hosted domain name will not be revealed for now, as the server is maybe not powerfull enought to take much requests and more for private uses for now)
 
# Vape Cracked

Vape offers an advanced cheating solution for Minecraft that integrates seamlessly into Forge versions of the game. Renowned for its simplicity and robust stealth capabilities, Vape ensures secure and undetectable injection of cheats, providing a significant edge in gameplay.

## Official Vape Website
For purchases, visit the official website:
[https://www.vape.gg/](https://www.vape.gg/)

## UPDATE MESSAGES

### 12/22/2024
Launcher.py has been created, 
` FAR OF BEING PERFECT, IK IT DOSENT START VAPE PROPERLY JUST START IT YOUR SELF IF IT DOSENT START AUTOMATICALLY, AT LEAST YOU WILL HAVE THE SERVER RUNNING `
+
Newer Video: https://archive.org/details/vape-v-4.mp-4
### 12/21/2024
New Server: https://discord.gg/jFg7quHz
+
I know I said I wouldn’t update this project anymore, but recently, I’ve received many friend requests reporting a new issue. I even encountered the same problem myself. The only reliable solution so far has been to use the exact environment (ENV) I had in my first version/backup.

To help with this, I’ll try to create a better tutorial or guide. In the meantime, I recommend using the `env` folder as specified in the "VENV" instructions.  

**Quick Start**  
If you simply want to run the script without setting up a new environment, you can execute:  
```bash
env\Scripts\python.exe server.py
```

**Environment Files**  
Check the releases section for two downloadable files:  
- `env.zip`: Contains only the environment files (a copy of Python and all dependencies).  
- `full.zip`: A complete backup with the `venv` and everything pre-configured, ready to start.  

Due to repository size and code clarity, the `env` folder is not included in the repository. You’ll need to create your own virtual environment if you don’t use the provided files.

**Future Plans**  
I’m considering making a simple launcher to help users start Vape more easily. Even with this "EZ crack," it seems some users still find the setup process challenging. Unfortunately, I can’t help everyone individually. I’ve already spent countless nights talking with users and even providing remote support via TeamViewer.  

**What I’ve Learned**  
1. The **Python version** is critical.  
2. Some dependencies must be updated or installed with the correct versions.  

For reference, I’ve included a `freeze.txt` file (the result of running `pip freeze` in my environment) in both the `vape-v4` and `Lite` folders. This should help you identify the exact dependencies and versions required for the setup.

Thank you for your patience and understanding.


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

## Instructional Video
Watch the setup video here:
[Instructional Video](https://web.archive.org/web/20231211230047/https://cdn.discordapp.com/attachments/1127981561820754011/1127982978388201472/2023-07-10_11-13-30.mp4)
[Newer Instructional Video](https://archive.org/details/vape-v-4.mp-4)

## Frequently Asked Questions (FAQ)

- **Issue: 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'**
- **OR: DLL load failed while importing _rust**
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
- ~kepardev~ (BANNED) -> `kolhaxdev`
- https://discord.gg/jFg7quHz

## Donations
If you appreciate my work and would like to support me, even a small contribution of just one dollar would make a difference. Thank you so much in advance for your generosity!
- BTC: `bc1qup9zrl9z94agmxjth4kqvyevdd6tysmf5th6hz`
- ETH: `0x88229297934Dea144783188262268E36b5C8205b`
- Paypal: https://paypal.me/keparMC
