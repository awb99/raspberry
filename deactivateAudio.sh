# 1. The audio output must be deactivated. For this we edit the file
sudo nano /etc/modprobe.d/snd-blacklist.conf
# Here we add the following line:
# blacklist snd_bcm2835


# 2. We also need to edit the configuration file:
sudo nano /boot/config.txt
# comment out the dtparam=audio=on with a #
# dtparam=audio=on
