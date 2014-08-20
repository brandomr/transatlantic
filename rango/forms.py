from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="What do you want to call this story?",
    			widget = forms.TextInput(
    			attrs = {'size': '75'}))
    description = forms.CharField(max_length=500, help_text="Give it a brief description.",
    			widget = forms.Textarea(
    			attrs = {'rows': '6', 'cols':'75'}))		
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="What's the title of your note?",
    			widget = forms.TextInput(
    			attrs = {'size': '75'}))
    url = forms.URLField(max_length=200, help_text="Want to link to something?",
    			widget = forms.TextInput(
    			attrs = {'size': '75'}))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    content = forms.CharField(max_length=1000, help_text="Tell the story.",
    			widget = forms.Textarea(
    			attrs = {'rows': '6', 'cols':'75'}))
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('title', 'url', 'content', 'views')


    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data
   

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.",
        		widget = forms.TextInput(
    			attrs = {'size': '75'}))
    email = forms.CharField(help_text="Please enter your email.",
        		widget = forms.TextInput(
    			attrs = {'size': '75'}))
    password = forms.CharField(help_text="Please enter a password.",
        		widget = forms.PasswordInput(
    			attrs = {'size': '75'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    location = forms.CharField(help_text="Please enter your location or post.", required=False,
        		widget = forms.TextInput(
    			attrs = {'size': '75'}))
    bio = forms.CharField(help_text="Tell us about yourself.", required=False,
    			widget = forms.Textarea(
    			attrs = {'rows': '6', 'cols':'75'}))
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ['location', 'bio', 'picture']