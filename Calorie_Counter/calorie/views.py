from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import CalorieProfile



@login_required
def dashboard(request):

    profile = CalorieProfile.objects.get(user=request.user)
    return render(request,'calorie/dashboard.html',{'profile': profile })



def calculate_calories(age, gender, weight, height_cm):
    """
    Calculate BMR using the Mifflin-St Jeor equation.

    Male: BMR = 10W + 6.25H - 5A + 5
    Female: BMR = 10W + 6.25H - 5A - 161
    """

    if gender == 'Male':
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

    # Sedentary activity multiplier
    daily_calories = bmr * 1.2

    return round(bmr, 2), round(daily_calories, 2)


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')

    return render(request, 'calorie/home.html')


def register_view(request):

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                username=username,
                password=password
            )

            profile = form.save(commit=False)
            profile.user = user

            bmr, daily_calories = calculate_calories(
                profile.age,
                profile.gender,
                profile.weight,
                profile.height_cm
            )

            profile.bmr = bmr
            profile.daily_calories = daily_calories

            profile.save()

            login(request, user)

            return redirect('profile')

    else:
        form = RegisterForm()
    return render(request,'calorie/register.html',{'form': form})


def login_view(request):

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('profile')

        return render( request,'calorie/login.html',{'error': 'Invalid username or password.'})
    
    return render(request, 'calorie/login.html')


@login_required
def profile(request):

    profile = CalorieProfile.objects.get(user=request.user)

    return render(
        request,
        'calorie/profile.html',
        {'profile': profile}
    )


@login_required
def result(request):

    profile = CalorieProfile.objects.get(user=request.user)

    bmr, daily_calories = calculate_calories(
        profile.age,
        profile.gender,
        profile.weight,
        profile.height_cm
    )

    profile.bmr = bmr
    profile.daily_calories = daily_calories
    profile.save()

    return render(
        request,
        'calorie/result.html',
        {
            'profile': profile,
            'bmr': bmr,
            'daily_calories': daily_calories
        }
    )


def logout_view(request):
    logout(request)
    return redirect('login')