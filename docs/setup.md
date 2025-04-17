# Setup

This describes the setup of new robots based on a raspberry pi.

All the steps were tested with a raspberry pi 5.

## 1. Install the operating system
### 1.1 Download the image and install it on the SD card
Download the respberry pi imager and install it on your computer. You can find the imager here:
https://www.raspberrypi.com/software/

Use the latest version of the Raspberry Pi OS, preferably the 64 bit version.
Contiue with the installer and activate Wifi, and SSH during the process.

By convention, the hostname should be 'cv-[color]' where [color] is the color for identifying the robot. 
For example, 'cv-red' for a red robot.

The username should be 'pi'. Make sure the set a strong password for the user pi and note it.

### 1.2 Boot the raspberry pi
Insert the SD card into the raspberry pi and boot it. Make sure you have a monitor connected or use SSH to connect to the raspberry pi when wifi is available.


### 1.3 Update the system