# Melopero FAN-HAT
![melopero logo](images/melopero_fan_hat.jpg?raw=true)

## Getting Started
### Prerequisites
You will need:
- a python3 version, which you can get here: [download python3](https://www.python.org/downloads/)
- a Melopero fan-hat: [buy here](https://www.melopero.com/shop/melopero-engineering/melopero-fan-hat-for-raspberry-pi-4/)

### Installing
You can install the melopero-fan-hat module by typing this line in the terminal: 
```python
sudo pip3 install --no-cache melopero-fan-hat
```
And that's it your fan is already set up. Reboot your raspberry and the fan should start all by itself.
The installer will create a new folder inside your /home directory, called melopero-autostart.
Inside melopero-autostart you'll find the fan_controller.py and the uninstaller, under /scripts and /uninstall.

![melopero logo](images/ls_melopero_autostart.JPG?raw=true)

### Uninstalling
To uninstall the melopero-fan-hat module and the melopero-autostart go to /home/melopero-autostart/uniunstall/ 

![melopero logo](images/cd_uninstall.JPG?raw=true)

and type the following command in the terminal: 

```python
sudo ./uninstall.sh
```
You'll be prompted twice to authorize the removal of melopero-autostart and melopero-fan-hat, answer "y" to both:

![melopero logo](images/full_uninstall.JPG?raw=true)




### Notes
The software uses the melopero-autostart module, you can find more about it [here](https://github.com/melopero/Melopero_Autostart) 
