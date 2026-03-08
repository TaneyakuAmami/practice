from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def commentView(request):
    comments = Comment.objects.order_by("-post_date")[:5]
    context = {"comments": comments}
    return render(request, "commentapps/index.html", context)

def commentSubmit(request):
    comment_text_val = request.POST["comment"]
    post_date_val = timezone.now()
    Comment.objects.create(comment_text=comment_text_val, post_date=post_date_val)
    return HttpResponseRedirect(reverse("commentapps:commentview"))
#    return commentView(request)
#    return HttpResponse(request.POST["comment"])