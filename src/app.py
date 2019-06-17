#!/usr/bin/env python
# coding: utf-8

from downloader import imageDownloader
import argparse

# REQUESTS_TIMEOUT = 2
# MAX_TRY = 5
# WEB_URL = 'https://www.google.com/'
# SAVE_PATH = '/home/naufalafif/Temp/download'

# app = imageDownloader(url='https://www.google.com')
# app.download()

parser = argparse.ArgumentParser(description='Simple App that download images')

parser.add_argument('-m', type=int,
                    help='Optional maximun number of tries to download url')

parser.add_argument('-t', type=int,
                    help='Optional request timeout time')

parser.add_argument('-s', type=int,
                    help='Optional path to save downloaded images')

args = parser.parse_args()

print(args)