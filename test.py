#!/usr/bin/env python
# coding: utf-8
"""Test File"""

import unittest
from src.downloader import ImageDownloader
import shutil
import os

IMAGE_URl = "https://images.unsplash.com/photo-1542091607-f2c384a6af13?ixlib=rb-1.2.1&auto=format&fit=crop&w=1352&q=80"


class TestDownloader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = "https://google.com"
        cls.url = url
        cls.downloader = ImageDownloader(url)
        cls.max_try, cls.timeout, cls.save_path = 3, 10, "test/download"

    def test_downloader_object(self):
        self.assertTrue("downloader" in repr(self.downloader).lower())
        self.assertTrue(isinstance(self.downloader, ImageDownloader))

    def test_downloder_method(self):
        max_try, timeout, save_path = self.max_try, self.timeout, self.save_path
        self.downloader.set_max_try(max_try).set_save_path(save_path).set_timeout(
            timeout
        )

        self.assertEqual(self.downloader.max_try, max_try)
        self.assertEqual(self.downloader.timeout, timeout)
        self.assertEqual(self.downloader.save_path, save_path)

    def test_init_path(self):
        try:
            self.downloader.init_path()
        except:
            self.fail("Fail to initialize save directory")
        finally:
            shutil.rmtree(self.save_path)

    def test_success_get_image_urls(self):
        download_result_file = None
        try:
            download_result = self.downloader.download_image_by_url(IMAGE_URl)
            download_result_file = download_result["filename"]
            self.assertTrue(download_result["status"])
        except:
            self.fail("Fail To Download Image")
        finally:
            if download_result_file is not None:
                os.remove(download_result_file)

    def test_normalize_url(self):
        image_path = "/assets/img"
        normalized_url = self.downloader.normalize_url(image_path)
        self.assertEqual(normalized_url, f"{self.url}{image_path}")

    def test_download(self):
        try:
            self.downloader.set_save_path(self.save_path).download()
        except:
            self.fail("Fail To Download Images")
        finally:
            if os.path.exists(self.save_path):
                self.assertGreater(len(os.listdir(self.save_path)), 0)
                shutil.rmtree("test")


if __name__ == "__main__":
    unittest.main()
