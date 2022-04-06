#!/usr/bin/python
# -*- coding: UTF-8 -*-
import codecs
import hashlib
import io
import json
import os
import subprocess
from datetime import datetime

import requests

import helper


def past_pasteboard_content():
    """
    粘贴剪贴板内容
    :return:
    """
    write_command = (
        'osascript -e \'tell application '
        '"System Events" to keystroke "v" using command down\''
    )
    os.system(write_command)


def set_clipboard_data(data: bytes):
    """
    内容复制到剪贴板
    :param data:
    :return:
    """
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    p.communicate()


class Uploader:
    __file = None

    def __init__(self, file):
        self.__file = file
        self.github_token = os.environ.get('github_token')
        self.github_repo = os.environ.get('github_repo')
        self.custom_date_formate = os.environ.get('custom_date_formate')
        self.github_cdn_url = os.environ.get('github_cdn_url')
        self.run()

    def run(self):
        helper.notify('Uploading', 'Please wait for a while')
        # 图片后缀
        file_path, point, suffix = self.__file.filename.rpartition('.')
        # 图片格式
        file_format = self.__file.format

        img_bytes = io.BytesIO()
        self.__file.save(img_bytes, file_format)
        # Convert bytes to base64
        base64_data = codecs.encode(img_bytes.getvalue(), 'base64')
        # Convert base64 data to a string
        base64_text = codecs.decode(base64_data, 'ascii')
        md5hash = hashlib.md5(base64_data).hexdigest()
        # Get image
        filename = md5hash + '.' + suffix
        self.upload_github(filename, base64_text)

    def upload_github(self, filename, content):
        custom_date_path = datetime.now().strftime(self.custom_date_formate)
        url = "https://api.github.com/repos/{}/contents/{}/".format(self.github_repo, custom_date_path) + filename
        headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + self.github_token}
        data = {
            "message": "upload pictures",
            "content": content
        }
        data = json.dumps(data)
        result = requests.put(url=url, data=data, headers=headers)
        if result.status_code == 201:
            result.encoding = "utf-8"
            markdown_url = self.github_cdn_url.format(filename=filename, github_repo=self.github_repo,
                                                      custom_date_path=custom_date_path)
            helper.notify('Success', markdown_url)

            # 调用系统剪贴板并粘贴
            # set_clipboard_data(bytes(markdown_url, 'utf8'))
            # past_pasteboard_content()

            # 打印结果，由 workflow 复制粘贴
            print(markdown_url)
        else:
            err_msg = result.text
            helper.red(err_msg)
            helper.notify('Error', result.reason)
