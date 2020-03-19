import logging
import os


def on(ip_addr):
    filename = ip_addr + "-runthrough.log"
    if os.path.exists(filename):
        os.remove(filename)
        print("Old log file deleted.")
    logging.basicConfig(filename=filename,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger("netmiko")

    return logger
