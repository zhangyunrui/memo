- References: How do I fix the GPG error "NO_PUBKEY"?
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3C962022012520A0 
sudo apt-get update
```
> You need to replace the key (3C962022...) with the one that is displayed in the error message in the terminal.

- gdebi
- aptitude