from django.shortcuts import render

# Create your views here.
def index(request):
	if request.method=="POST":
		name=request.POST["username"]
		mail=request.POST["usermail"]
		number=request.POST["usernumber"]
		message=request.POST["message"]
		print(name)
		print(mail)
		print(number)
		print(message)
	return render(request,"index.html")

def about(request):
	return render(request,"about.html")

def service(request):
	return render(request,"service.html")

def contact(request):
	if request.method=="POST":
		name=request.POST["username"]
		mail=request.POST["usermail"]
		number=request.POST["usernumber"]
		message=request.POST["message"]
		print(name)
		print(mail)
		print(number)
		print(message)
	return render(request,"contact.html")