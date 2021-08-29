from system.log import *
from ppadb.device import Device
import time
from uiautomator import device as ui


class pre_setting:
    l = None

    def __init__(self, adb: Device):
        self.adb = adb

    def open_buffer(self):
        job_title("start pre setting")
        job_title("go home")
        self.adb.shell('input keyevent 3')
        time.sleep(2)
        job_title("if setting running, stop it")
        self.adb.shell('am force-stop com.android.settings')
        time.sleep(2)
        job_title("open setting and go dev setting")
        self.adb.shell(
            'am start -a com.android.settings.APPLICATION_DEVELOPMENT_SETTINGS')
        time.sleep(2)
        job_title("drop down setting list")
        for i in range(24):
            self.adb.shell(
                'input keyevent 20')
        job_title("set buffer siez")
        ui(textMatches="Logger buffer sizes").click()
        ui(textMatches="16M").click()
        job_title("go home")
        self.adb.shell('input keyevent 3')
        job_title("if group chat running, stop it")
        self.adb.shell('am force-stop com.rayyuan.group_chat')
        job_title("open group chat")
        self.adb.shell(
            'am start -n com.rayyuan.group_chat/com.rayyuan.group_chat.MainActivity')
