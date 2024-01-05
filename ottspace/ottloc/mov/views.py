from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render, redirect
from .form import RegistrationForm, UserProfileForm, LoginForm

# views.py

from django.shortcuts import render

from .models import Register, Membership


def ott_home_view(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if registration_form.is_valid() and profile_form.is_valid():
            register_instance = registration_form.save(commit=False)
            register_instance.save()

            user_instance = profile_form.save(commit=False)
            user_instance.register = register_instance
            user_instance.save()

            # You can redirect to a success page or another view after registration
            return redirect('membership')  # Replace 'success' with your URL name

    else:
        registration_form = RegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'user/registration.html', {'registration_form': registration_form, 'profile_form': profile_form})


def login_user(request):
    error_message = None

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = Register.objects.get(username=username)
                if user.password == password:
                    # Login successful, redirect to 'home.html'
                    return render(request, 'account/welcome.html')  # Redirect to the home page
                else:
                    # Password mismatch
                    error_message = 'Invalid username or password.'
            except Register.DoesNotExist:
                # User does not exist
                error_message = 'Invalid username or password.'
        else:
            error_message = 'Invalid form data. Please check the entered values.'
    else:
        login_form = LoginForm()

    return render(request, 'account/login.html', {'login_form': login_form, 'error_message': error_message})

def membership(request):
    membership_plans = Membership.objects.all()

    return render(request, 'user/membership.html', {'membership_plans': membership_plans})

def select_user_type(request):
    return render(request, 'select_user_type.html')

def adult_user_page(request):
    # Logic for adult user page
    return render(request, 'adult_user_page.html')

def child_user_page(request):
    # Logic for child user page
    return render(request, 'child_user_page.html')

def create_new_profile(request):
    # Logic to create a new profile
    # For example, create a new entry in your database

    # Return a JSON response indicating success
    return JsonResponse({'success': True})