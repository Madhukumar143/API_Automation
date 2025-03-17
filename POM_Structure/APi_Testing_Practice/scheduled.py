import schedule
import time
import os

def run_script():
    os.system("python D:\\Api_Automation\\APi_Testing_Practice\\HROS_timesheet_automation.py")

# Schedule it to run at 4 PM
schedule.every().day.at("09:18").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(80)  # Wait for 60 seconds before checking again