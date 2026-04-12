from django.shortcuts import render
from .logic.analysis import Analyser

# Create your views here.
def start(request):
    return render(request, "webscraping/start.html")

def execute(request):
    #参考：https://techplay.jp/column/601
    url_in = request.POST['url']
    print("URLが入力されました")
    print(url_in)

    analyser = Analyser()
    analyser.analyse(url_in)

    return render(request, "webscraping/start.html")
