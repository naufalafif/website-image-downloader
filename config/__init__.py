import configparser
import os
config = configparser.ConfigParser()
config.read('config/config.ini')

RequestTimeout = int(config["DEFAULT"]["RequestTimeout"])
RequestMaxRetries = int(config["DEFAULT"]["RequestMaxRetries"])
SaveDirectory = os.getcwd()

CONFIGS = {
    "RequestTimeout": RequestTimeout,
    "RequestMaxRetries": RequestMaxRetries,
}