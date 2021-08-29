from uiautomator import device as ui
from ..log import *
import time


def login(adb):
    job_title("login")
    ui(text="信箱").set_text("alan.seglem@example.com")
    adb.shell('input text "alan.seglem@example.com"')
    time.sleep(2)
    ui(text="密碼").set_text("sheba1")
    adb.shell('input text "sheba1"')
    time.sleep(2)
    adb.shell('input keyevent 66')
