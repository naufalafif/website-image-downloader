import requests
from lxml import html
import validators
import urllib.request
import os
from concurrent import futures


def fillUrlDomain(parent_url, image_url):
    return "{}{}".format(parent_url, image_url)

class imageDownloader:
    def __init__(self, url):
        if url is None:
            raise ValueError("Url Required")
        self.url = url
        self.max_try = None
        self.timeout = None
        self.save_path = None

    def set_max_try(self, value):
        self.max_try = value
        return self

    def set_timeout(self, value):
        self.timeout = value
        return self

    def set_save_path(self, value):
        self.save_path = value
        return self

    def initPath(self):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def downloadImageByUrl(self, image_url, title=None):
        url_to_download = image_url
        if not validators.url(image_url):
            url_to_download = fillUrlDomain(self.url, image_url)

        if not title:
            url_path = urllib.request.urlparse(url_to_download).path
            ext = os.path.splitext(url_path)[1]
            hashed_url = str(abs(hash(url_to_download)))
            title = "{}{}".format(hashed_url, ext)

        if self.save_path:
            title = os.path.join(self.save_path, title)

        download_status = False
        try:
            urllib.request.urlretrieve(url_to_download, title)
            download_status = True
        finally:
            return {
                "status": download_status,
                "image_url": image_url
            }



    def extractImageUrls(self, request_try=1):
        if not validators.url(self.url):
            raise Exception("Url Invalid")

        if request_try == self.max_try:
            raise Exception("You Have Reach The Maximum Request")
        try:
            response = requests.get(self.url, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            print("Url Request Failed", e)
            self.extractImageUrls(request_try + 1)

        if response.status_code != 200:
            raise Exception("Url Requests Failed, Invalid Code ", self.url)
        response_in_html = html.fromstring(response.text)
        universal_image_path = "//img/@src"
        image_list = response_in_html.xpath(universal_image_path)

        return image_list

    def download(self):
        self.initPath()
        image_url_list = self.extractImageUrls()

        with futures.ThreadPoolExecutor() as executor:
            results = executor.map(self.downloadImageByUrl, image_url_list)

            for result in results:
                if result["status"]:
                    print(f"✔ download success : {result['image_url']}")
                else:
                    print(f"✖ download failed : {result['image_url']}")

        # for image_url in image_url_list:
        #     try:
        #         self.downloadImageByUrl(image_url)
        #         print("Download Success ", image_url)
        #     except:
        #         print("Download Failed ", image_url)
