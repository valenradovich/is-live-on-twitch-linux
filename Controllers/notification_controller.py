import time
import requests
import subprocess

def send_notify(title, message):
    subprocess.Popen(['notify-send', title, message])
    return