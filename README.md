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

Create and change the shell exript file permission that make sure the crontab can run it.
```bash
sudo chmod -R +x /home/robot
```

Create a cron job to check the script is running.
```bash
crontab -l
crontab -e -u ev3 / crontab -e
```

Add the following code.
```bash
*/10 * * * * /home/robot/ev3dev/cronjob_checker.sh
```

## Reference
https://stackoverflow.com/questions/45702887/running-python-process-with-cronjob-and-checking-it-is-still-running-every-minut
https://shian420.pixnet.net/blog/post/350291572-%5Bpython%5D-logging-%E5%B9%AB%E4%BD%A0%E7%B4%80%E9%8C%84%E4%BB%BB%E4%BD%95%E8%A8%8A%E6%81%AF




