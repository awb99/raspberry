#!/bin/bash

# download image from raspbian
# https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

# determine drive id via:
# lsblk

# unzip -p ~/Downloads/2018-11-13-raspbian-stretch.zip | sudo dd of=/dev/sdf bs=4M conv=fsync status=progress

dd bs=4M if=/home/florian/Downloads/2018-11-13-raspbian-stretch-full.img of=/dev/sdf conv=fsync status=progress
