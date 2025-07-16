from django.shortcuts import render
from Home.models import Contact
from django.contrib import messages 
from Home.models import Post
# Create your views here.
def index(request):
    allPosts = Post.objects.all()
    context = {"allPosts":allPosts}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, 'index.html',context)