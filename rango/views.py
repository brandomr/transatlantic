from django.http import HttpResponse

def index(request):
    return HttpResponse("<p>Rango says hello world!</p></br><a href='/rango/about'>Check out the about page</a>")
    
def about(request):
	return HttpResponse("<p>Rango Says: Here is the about page!</p></br><a href='/rango/'>Go home!</a>")