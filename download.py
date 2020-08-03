# -*- coding: utf-8 -*-
import os
import subprocess

url_file = 'url.txt'
url_file_path = os.path.abspath(url_file)

with open(url_file_path, encoding='utf-8') as f:
    content = f.readlines()
    print(content)

resource_dict = {}
for n in content:
    if n != '\n':
        split_ls = n.split()
        url = split_ls[0]
        name = ''
        for i in range(1, len(split_ls)):
            name += split_ls[i]
        resource_dict[url] = name + '.mp4'
print(resource_dict)


def download(url, name):
    cmd = 'ffmpeg -i ' + url + ' -vcodec copy -acodec copy ' + name
    print('执行命令：', cmd)
    subprocess.check_output(cmd)


for k, v in resource_dict.items():
    download(url=k, name=v)
