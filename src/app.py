#!/usr/bin/env python
# coding: utf-8

from downloader import imageDownloader

# REQUESTS_TIMEOUT = 2
# MAX_TRY = 5
# WEB_URL = 'https://www.google.com/'
# SAVE_PATH = '/home/naufalafif/Temp/download'

app = imageDownloader(url='https://www.google.com')
app.download()
