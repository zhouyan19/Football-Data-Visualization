import sys
import cgi
import requests
import json
import mimetypes
from urllib import parse

def formatSource(filename):
    imageList = []
    mime_type = mimetypes.guess_type(filename)[0]
    imageList.append(
        ('source', open(filename, 'rb'))
    )
    return imageList

username = 'Tony' # Your user name.
key = '359ccd4471d8dc7ca7326003f6b2511b' # API V1 Key.
albumID = 16 # Your album ID. If not needed, comment it out.

image_urls = []
post_data = {
    'username': username,
    'format': 'json',
    'key': key
}

if 'albumID' in vars():
    post_data['albumID'] = albumID

data = []
for key, value in post_data.items():
    data.append(key + '=' + parse.quote(str(value)))
query_string = '&'.join(data)

url = 'https://img.wzf2000.top/api/1/upload/?' + query_string

def UP(file_name):
    image_file = file_name
    if "http" == image_file[:4]:
        print(image_file)
        return ''
    res_json = json.loads(requests.post(url = url, files = formatSource(image_file)).text)
    if res_json['status_code'] != 200:
        print('error while uploading file {}'.format(image_file))
        print(res_json)
    else:
        return res_json["image"]["url"]
