# Website Image Downloader
Simple App that download images from url


### Help
```
$ ./app.py -h

usage: app.py [-h] [-m M] [-t T] [-s S] url

Simple App that download all images from url

positional arguments:
  url         Required site url

optional arguments:
  -h, --help  show this help message and exit
  -m M        Maximun number of tries to download url
  -t T        Request timeout time in second
  -s S        Path to save downloaded images
```

### Example
```
$ ./app.py https://www.google.com
Download Success  /images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png
Download Success  /textinputassistant/tia.png
```