from uiautomator import device as ui
from ppadb.client import Client as adb
from system.pre_setting import pre_setting
from system.app_test import *


class autoTest:
    def __init__(self):

        self.device = self.find_device()
        self.start_testing()

    def start_testing(self):
        pre_setting(self.device).open_buffer()
        time.sleep(8)
        login(self.device)

    def find_device(self):
        client = None
        try:
            client = adb(host="127.0.0.1", port=5037)
        except:
            raise "can't find any device"
        devices = client.devices()
        if len(devices) == 0:
            print('No devices')
            raise "can't find any device"

        device = devices[0]
        return device


if __name__ == '__main__':
    # Default is "127.0.0.1" and 5037
    autoTest()
