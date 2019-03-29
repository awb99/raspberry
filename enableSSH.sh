# https://www.raspberrypi.org/documentation/remote-access/ssh/

# wifi network credentials
cp wpa_supplicant.conf /run/media/florian/boot/

# enable ssh
touch /run/media/florian/boot/ssh

# ssh  credentials are:
# host: raspberrypi
# user: pi
# password: raspberry

# when logged in:
# sudo raspi-config
