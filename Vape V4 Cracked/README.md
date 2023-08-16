# Vape Server

This is a server that emulates Vape's server based on Kangaroo's crack.\
I made this back in december 2020 and never bothered updating/fixing it.

### What works?
- Vape V4 Forge (1.7, 1.8, 1.12)
- Saving configs (that wasn't possible with the Kangaroo crack)

### What doesn't work?
- Vape V4 on vanilla (prob mappings issue)
- Vape Lite (need to fix mappings)

### How to run it?

#### Server-side
- Get Python3
- Clone this git
- Run `pip install -r requirements.txt` to install the requirements
- Run `python server.py` (the first setup might take some time)
- Enjoy!

#### Client-side
- Get the Kangaroo crack
- Change the Websocket url from `ws://vape.sexy:8080` to `ws://localhost:8765` (from the source code or by hex editing the bins)
*(Very ghetto method if you can't do that : add the line `127.0.0.1 vape.sexy` in the hosts file and change the port to 8080 in server.py)*
- Enjoy!

### Is this safe?

I don't know, I just dumped the files from Kangaroo's crack server. If their file is safe, then this is safe.

### Credit
- Manthe for Vape
- The Kangaroo Team for the crack and the server
