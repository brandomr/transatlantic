import os

def populate():
	
	python_cat = add_cat('Python', 128, 64)
	
	add_page(cat=python_cat,
		title="Official Python Tutorial",
		url="http://docs.python.org/2/tutorial/",
		content="this is the official python tutorial",
		views=10)
	
	add_page(cat=python_cat,
		title="How to think like a computer scientist",
		url="http://www.greenteapress.com/thinkpython/",
		content="have you ever wanted to think like a computer scientist?",
		views=20)
	
	add_page(cat=python_cat,
		title="Learn Python in 10 minutes",
		url="http://www.korokithakis.net/tutorials/python/",
		content="Can you really learn this stuff in just ten minutes? Maybe.",
		views=20)
	
	django_cat = add_cat("Django", 64, 32)
	
	add_page(cat=django_cat,
		title="Official Django Tutorial'",
		url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
		content="This fantastic resource for learning Django is all yours!",
		views=15)
		
	add_page(cat=django_cat,
		title="Django Rocks",
		url="http://docs.djangorocks.com/",
		content="Yes, it does appear that Django rocks...",
		views=50)
		
	add_page(cat=django_cat,
		title="How to Tango with Django",
		url="http://www.tangowithdjango.com/",
		content="In actuality, this is the website that I am using to learn all about how to tango with da djangoman",
		views=42)
	
	frame_cat = add_cat("Other Frameworks", 32, 16)
	
	add_page(cat=frame_cat,
		title="Bottle",
		url="http://bottlepy.org/docs/dev/",
		content="Check out the bottle framework (whatever that is).",
		views=3)
		
	add_page(cat=frame_cat,
		title="Flask",
		url="http://flask.pocoo.org",
		content="what the heck is flask!",
		views=5)
	
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(p))
	
def add_page(cat, title, url, content, views=0):
	p = Page.objects.get_or_create(category=cat, title=title, url=url, content=content, views=views)[0]
	return p

def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
	return c

#start execution here!
if __name__ == '__main__':
	print "Starting Rango population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
	from rango.models import Category, Page
	populate()