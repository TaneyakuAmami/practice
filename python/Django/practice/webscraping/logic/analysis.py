import requests
from bs4 import BeautifulSoup

class Analyser():
    def __init__(self):
        self.name = "instance"

    def analyse(self, url_str):
        html_text = self.webaccess(url_str)
        print("解析開始")
        soup = BeautifulSoup(html_text, "html.parser")
        title = soup.find("h1").text
        print("h1=" + title)
        return title

    def webaccess(self, url_str):
        print("Webアクセス開始")
        print("url=" + url_str)
        response = requests.get(url_str)
        html_text = response.text
        return html_text

