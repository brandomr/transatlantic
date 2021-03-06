from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from transatlantic.models import Category
from transatlantic.models import Page
from transatlantic.models import UserProfile
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User


def encode_url(url):
	encoded_url = url.replace(' ','_')
	return encoded_url


def decode_url(url):
	decoded_url = url.replace('_',' ')
	return decoded_url



################### Category Listing ###############

def get_category_list():
	cat_list = Category.objects.all()
	
	for cat in cat_list:
		cat.url = encode_url(cat.name)
	
	return cat_list



def index(request):
    context = RequestContext(request)
    cat_list = get_category_list()

    category_list = Category.objects.all()
    context_dict = {'categories': category_list}
    context_dict['cat_list'] = cat_list

    for category in category_list:
        category.url = encode_url(category.name)

    page_list = Page.objects.order_by('-views')[:5]
    context_dict['pages'] = page_list

    #### NEW CODE ####
    if request.session.get('last_visit'):
        # The session has a value for the last visit
        last_visit_time = request.session.get('last_visit')
        visits = request.session.get('visits', 0)

        if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).seconds > 5:
            request.session['visits'] = visits + 1
            request.session['last_visit'] = str(datetime.now())
    else:
        # The get returns None, and the session does not have a value for the last visit.
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = 1
    #### END NEW CODE ####

    # Render and return the rendered response back to the user.
    return render_to_response('transatlantic/index.html', context_dict, context)
    
   
def about(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
	context = RequestContext(request)
	cat_list = get_category_list()

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

	# If the visits session varible exists, take it and use it.
	# If it doesn't, we haven't visited the site so set the count to zero.
	if request.session.get('visits'):
		count = request.session.get('visits')
	else:
		count = 0

	if count == 1:
		visit_language = str("time")
	else:
		visit_language = str("times")
	
	context_dict = {'boldmessage': "Sup my curious one!",
    				'visits': count,
    				'visit_language': visit_language}
    


	context_dict['cat_list'] = cat_list
	
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	return render_to_response('transatlantic/about.html', context_dict, context)
  
    
def category(request, category_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)
    cat_list = get_category_list()

    # Change underscores in the category name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    category_name = category_name_url.replace('_', ' ')	
		
    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.

    
    context_dict = {'category_name': category_name,
    				'category_name_url': category_name_url,
    				'cat_list': cat_list}
    


	
    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(name=category_name)

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category).order_by('-date')
		
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass


    # Go render the response and return it to the client.
    return render_to_response('transatlantic/category.html', context_dict, context)


##################### Category Form ########################
from transatlantic.forms import CategoryForm

@login_required
def add_category(request):
    # Get the context from the request.
    context = RequestContext(request)
    cat_list = get_category_list()


    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('transatlantic/add_category.html', {'form': form, 'cat_list': cat_list}, context)



##################### Page Form ########################
from transatlantic.forms import PageForm
from django.contrib.auth.models import User

@login_required
def add_page(request, category_name_url):
    context = RequestContext(request)
    cat_list = get_category_list()

    category_name = decode_url(category_name_url)
    print request.method	

    if request.method == 'POST':
        print "success"	

        form = PageForm(request.POST)

        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            page = form.save(commit=False)
            
			
            # Retrieve the associated Category object so we can add it.
            # Wrap the code in a try block - check if the category actually exists!
            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            except Category.DoesNotExist:
                # If we get here, the category does not exist.
                # Go back and render the add category form as a way of saying the category does not exist.
                return render_to_response('transatlantic/add_category.html', {}, context)
				
            # Also, create a default value for the number of views.
            page.views = 0
            
            page.date = datetime.now()
            
            page.drafter =  request.user
                        


            # With this, we can then save our new model instance.
            page.save()

            # Now that the page is saved, display the category instead.
            return category(request, category_name_url)
        else:
            print form.errors
    else:
    	form = PageForm()
    	print "failyo!"

    return render_to_response( 'transatlantic/add_page.html',
            {'category_name_url': category_name_url,
             'category_name': category_name, 'form': form, 'cat_list': cat_list},
             context)
             


################### User Profile Form ##########################

from transatlantic.forms import UserForm, UserProfileForm

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    cat_list = get_category_list()

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        print "it's a POST!"
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors
	
	
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'transatlantic/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'cat_list': cat_list},
            context)
            
            
            
################### Login Form ##########################
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)
    cat_list = get_category_list()

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
    	print "a post, it is"
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/transatlantic/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your transatlantic account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied. Make sure you put in the right things!")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('transatlantic/login.html', {'cat_list': cat_list}, context)
        

################## Login #################        

@login_required
def restricted(request):
    context = RequestContext(request)
    return render_to_response('transatlantic/restricted.html', {}, context)
    
    

################## Logout #################    
from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    context = RequestContext(request)
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/transatlantic/')
    
    
    
################### Profile View ##############



@login_required
def profile(request, userlink):
	context = RequestContext(request)
	cat_list = get_category_list()
	u = User.objects.get(username=userlink)
	curr_user = User.objects.get(username=request.user)
	notes = Page.objects.filter(drafter=u).order_by('-date')

	if curr_user == u:
		user_test = True
	else:
		user_test = False
	
	cat_link = []
	
	for i in range(0, len(notes)):
		new_link = encode_url(str(notes[i].category))
		cat_link.append(new_link)
		i+=1
	
	print cat_link
	
	notes_cat = [(notes[i], cat_link[i]) for i in range(len(notes))]
	
	try:
		up = UserProfile.objects.get(user=u)
	except:
		up = None
	
	context_dict = {'cat_list': cat_list,
					'userprofile': up,
					'user': curr_user,
					'prof_lookup': u,
					'notes_cat': notes_cat,
					'user_test': user_test}
					
	return render_to_response('transatlantic/profile.html', context_dict, context)
    
    
################### User Profile EDIT Form ##########################

from transatlantic.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User

def edit(request):
	context = RequestContext(request)
	cat_list = get_category_list()	
	
	u = User.objects.get(username=request.user)	

	userlink = str(request.user.username)
	
	try:
		up = UserProfile.objects.get(user=u)
	except UserProfile.DoesNotExist:
		up = None
	print request.method	
	
	if request.method == 'POST':
		print "it's a POST!"
		profile_form = UserProfileForm(data=request.POST, instance=up)
		if profile_form.is_valid():
			editprof = profile_form.save(commit=False)
			editprof.user = u
			if 'picture' in request.FILES:
				editprof.picture = request.FILES['picture']
			
			editprof.save()
			
			return profile(request, userlink)
		else:
			print profile_form.errors
	else:
		profile_form = UserProfileForm(instance=up)
	
	return render_to_response('transatlantic/edit_profile.html', 
            {'profile_form': profile_form, 'cat_list': cat_list, 'u': u},
            context)
  
            