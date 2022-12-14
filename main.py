import os
import requests
import webbrowser
import json
import time
from Config.tokens import *
from Controllers.api_controller import *
from Controllers.notification_controller import send_notify
from Views.build.gui import *

def main(user_input):

    secs = 60
    times = 0

    # print("Which streamer do you want to check?", flush=True)

    twitch_user = user_input

    try:
        userdata = check_user(twitch_user)
    except:
        main()

    if(userdata):
        while True:
            streamer_info = getting_data_from_streamer(userdata, twitch_user)

            if streamer_info == 0:
                time.sleep(5)
            else:
                send_notify(f"{streamer_info['user']} is live on Twitch :)", streamer_info['streamer_url'])
                time.sleep(secs)
                times+=1
                print(times)

                if times > 5:
                    secs = secs * 2

if __name__ == "__main__":
    secs = 60
    times = 0

    while True:
        window_input = principal_window()

        main(window_input)
        # time.sleep(60)