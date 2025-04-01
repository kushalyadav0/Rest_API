from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUp_form
from django.contrib import messages
# our browser is accepting cookies, The view function passes a request to the template’s render method.In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.If you are not using CsrfViewMiddleware, then you must use csrf_protect on any views that use the csrf_token template tag, as well as those that accept the POST data.The form has a valid CSRF token. After logging in in another browser tab or hitting the back button after a login, you may need to reload the page with the form, because the token is rotated after a login.
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login

# Create your views here.
def LogIn(request):
    pass


def SignUp(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        # form = SignUp_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
        
    else:
        form = UserCreationForm()
        # form = SignUp_form()
        
    return render(request, 'registration/signup.html', {'form':form})

"""

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "templates/registration/signup.html"

    """
