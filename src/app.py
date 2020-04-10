#!/usr/bin/env python
# coding: utf-8

from .downloader import imageDownloader
from config import RequestTimeout, RequestMaxRetries, SaveDirectory
import argparse

class Cli:
    def __init__(self):
        self.arguments = None
        self.init_parser()

    def init_parser(self):
        parser = argparse.ArgumentParser(
            description="Simple App that download all images from url"
        )
        parser.add_argument(
            "-m", type=int, help="Maximun number of tries to download url. default {}".format(RequestMaxRetries)
        )
        parser.add_argument("-t", type=int, help="Request timeout time in second. default {} seconds".format(RequestTimeout))
        parser.add_argument("-s", type=str, help="Path to save downloaded images")
        parser.add_argument("url", help="Required site url")
        self.arguments = parser.parse_args()

    def run(self):
        url = self.arguments.url
        max_try = self.arguments.m if self.arguments.m else RequestMaxRetries
        timeout = self.arguments.t if self.arguments.t else RequestTimeout
        save_path = self.arguments.s if self.arguments.s else SaveDirectory

        app = imageDownloader(url)
        app .set_max_try(max_try)\
            .set_timeout(timeout)\
            .set_save_path(save_path)

        app.download()
