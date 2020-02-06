#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import os
import random

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/72.0'
}


def parse_audio():
    while True:
        num = '6' + str(random.randrange(1111, 9999))
        num2 = str(random.randrange(111, 999)) + ".wav"
        url = "http://static.donationalerts.ru/audiodonations/" + num + '/' + num + num2
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print("connection done! " + url)
            path = os.path.join('audio', f'{num + num2}')
            with open(path, 'wb') as f:
                f.write(r.content)


if __name__ in '__main__':
    if os.path.exists('audio'):
        parse_audio()
    else:
        os.mkdir('audio')
        parse_audio()
