from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate ,logout

# This function will be exceuted when the user visits the home page
def register_view(request):
    #check if the request is a POST request
    if request.method == 'POST':
        #create a form instance with the submitted data
        form = UserCreationForm(request.POST)
        #check if the form is valid:password matches,username is not taken
        if form.is_valid():
            #save user to db
            user = form.save()
            #log the user in
            login(request,user)
            return redirect('home') #redirect to home page
    else:
        #create a form instance with no data
        form = UserCreationForm()
        #render the form template with the form instance
    return render(request,'accounts/register.html',{'form':form})

#defines a view for the login page
def login_view(request):
    #check if the request is a POST request
    if request.method == 'POST':
        #create a form instance with the submitted data
        form = AuthenticationForm(data = request.POST)
        #check if the form is valid
        if form.is_valid():
            #log in the user
            user = form.get_user()
            #log the user in
            login(request,user)
            #redirect to home page
            return redirect('home')
    else:
        #create a form instance with no data
        form = AuthenticationForm()
        #render the form template with the form instance
    return render(request,'accounts/login.html',{'form':form})

#defines a view for the logout page
def logout_view(request):
    #check if the request is a POST request
    if request.method == 'POST':
        #log the user out
        logout(request)
        return redirect('home') #redirect to home page