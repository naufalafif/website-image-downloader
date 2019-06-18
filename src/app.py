#!/usr/bin/env python
# coding: utf-8

from downloader import imageDownloader
import argparse
import sys
sys.tracebacklimit=0

parser = None
class Cli:
  def __init__(self):
    self.arguments = None
    self.init_parser()
    self.execute()
  
  def  init_parser(self):
    parser = argparse.ArgumentParser(description='Simple App that download all images from url')
    parser.add_argument('-m', type=int,
                        help='Maximun number of tries to download url')
    parser.add_argument('-t', type=int,
                        help='Request timeout time in second')
    parser.add_argument('-s', type=str,
                        help='Path to save downloaded images')
    parser.add_argument('url',
                        help='Required site url')
    self.arguments = parser.parse_args()

  def execute(self):
    url = self.arguments.url
    max_try = self.arguments.m
    timeout = self.arguments.t
    save_path = self.arguments.s

    app = imageDownloader(url)

    if max_try:
      app.set_max_try(max_try)
    if timeout:
      app.set_timeout(timeout)
    if save_path:
      app.set_save_path(save_path)

    app.download()
    
cli_app = Cli()