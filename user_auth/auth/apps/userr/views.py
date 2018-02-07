from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
# Authenticate compares to database info...login adds session info that follows
from django.contrib.auth import authenticate, login
from .forms import UserForm, LoginForm


def Index(request):
    print("came to index")
    return redirect("register")

def Main(request):
    return HttpResponse("main page")

class UserFormView(View):
    form_class = UserForm
    template_name = "userr/registration_form.html"

    
    # Django has built in method to handle both get and post same view
    # Display blank form
    def get(self, request):
        form = self.form_class(None) # none = not bound
        form2 = LoginForm()
        return render(request, self.template_name, {"form":form, "form2":form2})
        
    # Post request can process form information after binding info to it!!!    
    def post(self,request):
        if request.POST["form-type"] == "register":

            form = self.form_class(request.POST)
            # Commit false creates object but does not save to database
            if form.is_valid():
                user = form.save(commit = False)
                # Can have data scrubbed and normalized to correct python code
                # Password is set through built in function that converts to hash
                # first_name = form.cleaned_data["first_name"]
                # username = form.cleaned_data["username"]
                # email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                user.set_password(password)
                user.save()
                print("user created")
                return redirect("register")
            else:
                print("form not valid")
                return redirect("register")

        if request.POST["form-type"] == "login":
            submitted_form = LoginForm(request.POST)
            if submitted_form.is_valid():
                try:
                    # Authenticate and login
                    # If true user becomes actual objects
                    username = submitted_form.cleaned_data["username"]
                    password = submitted_form.cleaned_data["password"]
                    user = authenticate(username = username, password = password)
                    print("user authentic")
                except:
                    print("user not authentic")
                    return render(request, self.template_name, {"form": form, "form2": form2})

                if user is not None:
                    if user.is_active:
                        login(request,user) 
                        print(request.user.email)                    
                        return redirect("main")
                        
            # if user is not in system and active you refer them back to same page
            return redirect("register")

