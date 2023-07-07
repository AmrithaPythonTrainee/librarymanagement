from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    books=Book.objects.all().order_by('-date')
    return render(request,"viewbook.html",{"books":books})
def index1(request):
    return render(request,"loginandregister.html")

def addBookView(request):
    return render(request,"addbook.html")
def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        l=request.POST["lang"]
        a=request.POST["author"]
        print(t,p,l,a)
        book=Book()
        book.title=t
        book.price=p
        book.lang=l
        book.author=a
        book.save()
        return HttpResponseRedirect('/')
def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        l=request.POST["lang"]
        a=request.POST["author"]
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.price=p
        book.lang=l
        book.author=a
        book.save()
        return HttpResponseRedirect('/')

def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    return render(request,"edit-book.html",{"book":book})

def deleteBookView(request):
      book=Book.objects.get(id=request.GET['bookid'])
      book.delete()
      return HttpResponseRedirect('/')


def user_login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username,password = password)
        if user:

            if user.is_active:
                login(request, user)
                print("login success!!!")
                return HttpResponseRedirect(reverse('index'))
        else:
            
            print("No such user")


    return HttpResponseRedirect(reverse('index'))

def user_logout(request):

    logout(request)


    return HttpResponseRedirect(reverse('index'))


def register(request):
    
    
    if request.method == 'POST':
        try:
            user = User.objects.create(username = request.POST.get('username'),email=request.POST.get('email'))
            user.set_password(request.POST.get('password'))
            user.save()
        except:
            pass


    return HttpResponseRedirect(reverse('index'))
