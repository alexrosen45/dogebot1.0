import time
from prices import json_data
from dogebot import Dogebot
import csv

doge_keys_tokens = [
    "vzpBzTMrS5C62VN2BpDQwRZOd",
    "sFcRWsEOrofF7aMnsYs53z4P2LJFZftO7FAdz95IPZuRswqR2V",
    "1395390371358814210-fzlssXKC5tWMYB74ZQjxSgMHYPTqfX",
    "bO2WvOFZ6qdZrT91IF97HXQlEdhUJuFNSkAi7WMVSj3BI"
]

timer = 0
skip = True

while True:

    if timer == 0:
        dogebot = Dogebot(doge_keys_tokens, "elonmusk")
        dogebot.get_last_tweet()
        dogebot.doge_scan()

        if dogebot.new_order == True and dogebot.doge_present == True:
            print("buying doge...")
            dogebot.buy()
            timer += 1
        else:
            print("not buying doge")
        time.sleep(10)

    if timer != 0 and timer != 360:
        time.sleep(10)
        timer += 1

    # 360 10s time period in 1hr
    if timer == 360:
        data = json_data['data']
        for cryptocurrency in data:
            if cryptocurrency['symbol'] == 'DOGE':
                hr_percent_change = [cryptocurrency['quote']['CAD']['percent_change_1h']]
                with open('C:/Users/alexa/Documents/Programming/fintech/dogebot/historical_data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    print("% gain: "+str(hr_percent_change[0]))
                    writer.writerow(hr_percent_change)
                file.close()

        timer = 0