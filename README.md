# Non-wearable AI Elderly Home (LEGO Mindstorms EV3)
IVE Final Year Project : Non-wearable AI Elderly Home (LEGO Mindstorms EV3)

## Set up ev3dev
Following the below instructions to set up the basic configuration for ev3.
https://www.ev3dev.org/docs/getting-started/

Connect to the ev3dev and run below command.
```bash
apt-get update
sudo apt-get install cron
```

Change the file permission that make sure the cron job can run it.
```bash
sudo chmod -R +x /home/robot
```

Create a cron job to check the script is running.
```bash
crontab -l
crontab -e
```

Add the following line to create a cron job.
```bash
*/10 * * * * /home/robot/ev3dev/cronjob_checker.sh
```

## Reference
https://www.ev3dev.org/
https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/index.html
https://github.com/aws/aws-iot-device-sdk-python




