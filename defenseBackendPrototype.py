import os
import logging
import time
import socket
import scapy # importing necessary modules

# Setting up logger, handler and formatting for the log
def attackLogger():
    logger = logging.GetLogger("detector")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatting = logging.Formatter('%(levelname)s: %(message)s [%(asctime)s]')
    handler.setFormatter(formatting)
    logger.addHandler(handler)
    return

