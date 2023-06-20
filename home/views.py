from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .models import StudentInfo
from django.http import HttpResponse



@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        context = {'username': username}

        if user is not None:
            login(request, user)
            if user.is_superuser:
                print("Superuser!!!!!!")
                return render(request, 'home/admin.html', context)
            # return render(request, 'home/home.html', context)
            return redirect('viewer')
        else:
            messages.info(request, 'Username or Password is incorrect')

        

    return render(request, 'home/login.html')


def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created successfully")
            return redirect('login')

    context = {'form': form}
    return render(request, 'home/signup.html', context)

def logoutUser(request):
    """
    This view function is responsible for logging out the user and redirecting to the login page.
    """
    logout(request)
    return redirect('login')


def admin_page(request):
    """
    This view function is responsible for rendering the admin page.
    """
    return render(request, 'home/admin.html')


def DataAdder(request):

    if request.method == 'POST':
        # Store Personal Details
        name = request.POST.get('name')
        degree = request.POST.get('degree')
        branch = request.POST.get('branch')
        degreepercentage = request.POST.get('degreepercentage')
        yop = request.POST.get('yop')
        lin = request.POST.get('lin')
        cno = request.POST.get('cno')
        ps = request.POST.get('ps', False) == 'on'

        
        
        
        details = StudentInfo.objects.create(
                name=name,
                degree=degree,
                branch=branch,
                degreePercentage=degreepercentage,
                yop=yop,
                linkedin=lin,
                contact=cno,
                placementStatus=ps
            )
            
        details.save()

        return redirect('success')
    else:

        return render(request, 'home/admin.html')
    
def DataAdded(request):

    return render(request, 'home/added.html')  
    

def DataViewer(request):


    if request.method == 'POST':

        # status = request.POST.get('placement_status', None)

        # if status:
        #     if status == 'Placed':
        #         details = StudentInfo.objects.filter(placementStatus=True)
        #         context = {'details': details}
        #         return render(request, 'home/viewer.html', context)
        #     elif status == 'NotPlaced':
        #         details = StudentInfo.objects.filter(placementStatus=False)
        #         context = {'details': details}
        #         return render(request, 'home/viewer.html', context)
        #     else:
        #         details = StudentInfo.objects.all()
        #         context = {'details': details}
        #         return render(request, 'home/viewer.html', context)
        pass

    else:
        details = StudentInfo.objects.all()
        context = {'details': details}
        return render(request, 'home/viewer.html', context)










        
