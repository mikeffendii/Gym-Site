from django.shortcuts import render

# Create your views here.
def Index(request):
	return render(request, 'index.html')

def AboutUs(request):
	return render(request, 'about-us.html')

def BlogDetails(request):
	return render(request, 'blog-details.html')

def Blog(request):
	return render(request, 'blog.html')

def Contact(request):
	return render(request, 'contact.html')

def Gallery(request):
	return render(request, 'gallery.html')

def Services(request):
	return render(request, 'services.html')

def Team(request):
	return render(request, 'team.html')

def ClassDetails(request):
	return render(request, 'class-details.html')

def ClassTimetable(request):
	return render(request, 'class-timetable.html')
