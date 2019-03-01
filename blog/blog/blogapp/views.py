from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    details=get_object_or_404(Blog,pk=blog_id)
    return render(request,"detail.html",{'details':details})

def new(request):
    return render(request,'new.html')

def create(request):  #입력받은 함수를 데이터 베이스에 넣기
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) #str을 쓰는이유 url은 무조건 str인대 우리 blog_id를 int로 선언했기때문에 str을 써줘야 한다

