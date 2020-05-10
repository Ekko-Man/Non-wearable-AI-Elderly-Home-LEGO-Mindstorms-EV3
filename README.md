# fyp-ev3
IVE FYP lego ev3 

## Set up ev3dev
Following the below instructions to set up the basic configuration for ev3.
https://www.ev3dev.org/docs/getting-started/

Connect to the ev3dev and run below command.
```bash
apt-get update
sudo apt-get install cron
```
==

Add a user for crontab.
```bash
sudo adduser ev3
sudo usermod -aG sudo ev3
```
group : ev3
user : ev3
password : ev3-fyp
Full Name : Ekko
Room Number : lwl332
Work Phone : 12345678
Home Phone : 12345678
Other : 
==

Create and change the shell exript file permission that make sure the crontab can run it.
```bash
sudo chmod -R +x /home/robot
```

Create a cron job to check the script is running.
```bash
crontab -l
crontab -e -u ev3
```

