import requests
from lxml import html
import validators
import urllib.request
import os
from concurrent import futures
from itertools import repeat


class ImageDownloader:
    def __init__(self, url):
        if url is None:
            raise ValueError("Url Required")
        self.url = url
        self.max_try = None
        self.timeout = None
        self.save_path = None

    def __repr__(self):
        return "Image Downloader Class"

    def set_max_try(self, value):
        self.max_try = value
        return self

    def set_timeout(self, value):
        self.timeout = value
        return self

    def set_save_path(self, value):
        self.save_path = value
        return self

    def init_path(self):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def normalize_url(self, image_url):
        if not validators.url(image_url):
            return "{}{}".format(self.url, image_url)
        return image_url

    @staticmethod
    def download_image_by_url(image_url, path=os.getcwd()):
        if not validators.url(image_url):
            raise ValueError("Please use valid url")

        url_path = urllib.request.urlparse(image_url).path
        ext = os.path.splitext(url_path)[1]
        hashed_url = str(abs(hash(image_url)))
        title = "{}{}".format(hashed_url, ext)
        title = os.path.join(path, title)

        download_status = False
        try:
            urllib.request.urlretrieve(image_url, title)
            download_status = True
        finally:
            return {
                "status": download_status,
                "image_url": image_url,
                "filename": title,
            }

    def extract_image_urls(self, request_try=1):
        if not validators.url(self.url):
            raise Exception("Url Invalid")

        if request_try == self.max_try:
            raise Exception("You Have Reach The Maximum Request")
        try:
            response = requests.get(self.url, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            print("Url Request Failed", e)
            self.extract_image_urls(request_try + 1)

        if response.status_code != 200:
            raise Exception("Url Requests Failed, Invalid Code ", self.url)
        response_in_html = html.fromstring(response.text)
        universal_image_path = "//img/@src"
        image_list = response_in_html.xpath(universal_image_path)

        return image_list

    def download(self):
        self.init_path()
        image_url_list = self.extract_image_urls()
        image_url_list = [self.normalize_url(url) for url in image_url_list]

        with futures.ThreadPoolExecutor() as executor:
            results = executor.map(
                ImageDownloader.download_image_by_url,
                image_url_list,
                [self.save_path] * len(image_url_list),
            )

            for result in results:
                if result["status"]:
                    print(f"✔ download success : {result['image_url']}")
                else:
                    print(f"✖ download failed : {result['image_url']}")
