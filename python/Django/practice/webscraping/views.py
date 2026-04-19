from django.shortcuts import render
from .logic.analysis import Analyser

# Create your views here.
def start(request):
    template_name = "webscraping/start.html"

    return render(request, template_name)

def execute(request):
    template_name = "webscraping/start.html"

    #参考：https://techplay.jp/column/601
    url_in = request.POST['url']
    print("URLが入力されました")
    print(url_in)

    analyser = Analyser()
    html_text = analyser.analyse(url_in)
    print("answer:" + html_text)
    context = {"contents": html_text}

    return render(request, template_name, context)
