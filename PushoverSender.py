#!/usr/bin/env python
# coding:utf8

import httplib,urllib,sys

class PushoverSender:
    def __init__(self, user_key="******************************", api_key="******************************"):
        self.user_key = user_key
        self.api_key = api_key

    def send_notification(self, text):
        conn = httplib.HTTPSConnection("api.pushover.net:443")
        post_data = {'user': self.user_key, 'token': self.api_key, 'message': text}
        conn.request("POST", "/1/messages.json",urllib.urlencode(post_data), {"Content-type": "application/x-www-form-urlencoded"})
        # print(conn.getresponse().read())

def main():
    push_obj=PushoverSender()
    sendstr="PushoverSender Demo For Ali-srv"

    # send parameters if exist
    if len(sys.argv)>1:
        sendstr=""
        for each in sys.argv[1:]:
            sendstr+=each+" "
        if len(sendstr)>0 and sendstr[-1]==" ":
            sendstr=sendstr[:-1]

    push_obj.send_notification(sendstr)

if '__main__'==__name__:
        main()
