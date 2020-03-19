"""
Script: gather_4G_stats.py
By: Matt Hannan
Date: 3/14/2020

Need a way to see poor 4G signal performance.
Gathering details from an active ssh session is only a snapshot in time.
The goal of his script is to gather the stats on a minute-by-minute basis
so that a chart can be generated.

For this I am using my netmiko scripts.
I would have liked to drop this into Pandas and generate the charts in Numpy,
but not everyone has those tools available to them.
Excel cvs files it is.

Basic outline:
* Prompt user for IP                                    Done
* Prompt user for how long to gather data               Done
* Start netmiko ssh session through Linux jump box      Done
* Issue "show cellular 0 radio" in loop                 Done
* Process output                                        Done
* Save to cvs file                                      Done

"""

# import buildList
from time import sleep
import os
import csv
import userInput
import enableLogging
import turnNetmiko


# Gather details from user
ip_addr = userInput.getTargetIP()
timespan = int(userInput.getLengthOfTime())

# Get Linux jumpserver details and other user input
jumpserver = userInput.getJumpServer()
rsa_pwd = userInput.getRSAandToken()

# Enable logging
logger = enableLogging.on(ip_addr)

# Fire up Netmiko, connect to jumpbox, connect to target
net_connect = turnNetmiko.on(jumpserver, ip_addr, rsa_pwd)

# Open the csv file
filename = ip_addr + "_4G_stats.csv"
# Check to see if it exists.
# If it does, delete the old one.
if os.path.exists(filename):
    os.remove(filename)
    print("Old report deleted.")

# Open the csv file and start building the sucker.
with open(filename, "w", newline="") as csv_file:
    fieldnames = ["Timestamp", "RSSI", "RSRP", "RSRQ", "SNR"]
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(fieldnames)

    # Loop through list of ports for SHOW
    minute = 0
    for minute in range(timespan):
        clock = net_connect.send_command("sh clock")[1:]
        print(clock)
        stats = net_connect.send_command("sh cel 0 radio")
        # print(stats)

        # Carve it up
        for line in stats.splitlines():
            # print("Line is =", line)
            if "RSSI" in line:
                rssi = line.split('=')[1].split()[0]
                # print(rssi)
            if "RSRP" in line:
                rsrp = line.split('=')[1].split()[0]
                # print(rsrp)
            if "RSRQ" in line:
                rsrq = line.split('=')[1].split()[0]
                # print(rsrq)
            if "SNR" in line:
                snr = line.split('=')[1].split()[0]
                # print(snr)

        # Write the data to file
        csv_writer.writerow([clock, rssi, rsrp, rsrq, snr])

        # Sleep for 60 seconds
        sleep(60.0)
        minute += 1
    # Close monitoring    
    print("Monitoring complete.")

# Exit the switch
print(net_connect.send_command_timing("exit"))

# Exit the jump box
turnNetmiko.off(net_connect)
print("Session closed.")
net_connect.disconnect()
