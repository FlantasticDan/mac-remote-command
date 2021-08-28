# mac-remote-command
Client for embedded systems to facilitate remote configuration.

MAC Remote Command facilitates the configuration of embedded remote and local systems by connecting to an remote web service.  A reference implementation is available and free to use at [https://mac-commander.deta.dev/](https://mac-commander.deta.dev/).  The source code for the web service is available on GitHub at [FlantasticDan/mac-commander](https://github.com/FlantasticDan/mac-commander).  MAC Remote Command optionally includes support to display it's detect Local IP and MAC Address via an [OLED Status Display](https://github.com/FlantasticDan/oled-status).

## Installation
For standard use:
```bash
pip install mac-remote-command
```

For optional use with an OLED Status Display:
```bash
pip install mac-remote-command[oled]
```
**Note** OLED Status Display is only compatiable on Linux devices with an I<sup>2</sup>C bus.

## Use
Currently the remote command functionality of the package is undeveloped.  Right now it only offers a pinging service to publically broadcast it's local and public IP address as referenced by it's MAC Address:
```bash
python -m mac_remote.ping
```