import os
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreateUserForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import StudentInfo
from django.http import HttpResponse



@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url='login')
def cdc(request):
    return render(request, 'home/cdc.html')


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
                return redirect('cdc')
            # return render(request, 'home/home.html', context)
            return redirect('home')
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




def DataAdder(request):

    if request.method == 'POST':

        # resume file
        resume = request.FILES['resume_file']
        profile = request.FILES['profile']


        # Store Personal Details
        name = request.POST.get('name')
        email = request.POST.get('email')
        degree = request.POST.get('degree')
        branch = request.POST.get('branch')
        degreepercentage = request.POST.get('degreepercentage')
        yop = request.POST.get('yop')
        lin = request.POST.get('lin')
        cno = request.POST.get('cno')
        ps = request.POST.get('ps', False) == 'on'

        details = StudentInfo.objects.create(
                user=User.objects.get(username=request.user.username),
                name=name,
                email=email,
                degree=degree,
                branch=branch,
                degreePercentage=degreepercentage,
                yop=yop,
                linkedin=lin,
                mobno=cno,
                resume=resume,
                profile=profile,
                placementStatus=ps
            )
            
        details.save()
         
        context = {
            'data_added': True
        }
        return render(request, 'home/home.html', context)
    

    else:

        user = request.user
        context = {
            'data_added': False
        }
        if StudentInfo.objects.filter(user=user).exists():
            context = {
            'data_added': True
        }
        
        return render(request, 'home/user.html', context)

def DataEditor(request):


    if request.method == 'POST':
        # Store Personal Details
        name = request.POST.get('name')
        email = request.POST.get('email')
        degree = request.POST.get('degree')
        branch = request.POST.get('branch')
        degreepercentage = request.POST.get('degreepercentage')
        yop = request.POST.get('yop')
        lin = request.POST.get('lin')
        cno = request.POST.get('cno')
        ps = request.POST.get('ps', False) == 'on'

        details = StudentInfo.objects.get(user=User.objects.get(username=request.user.username))

        try:
            resume = request.FILES['resume_file']
            profile = request.FILES['profile']

            details.resume = resume
            details.profile = profile

            print("changing file sorry!!!!!!!!!!!!!")

        except:
            pass

        details.name = name
        details.email = email
        details.degree = degree
        details.branch = branch
        details.degreePercentage = degreepercentage
        details.yop = yop
        details.linkedin = lin
        details.mobno = cno    
        details.placementStatus = ps
        details.save()

        context = {
            'data_updated': True
        }    
        
        return render(request, 'home/edit.html', context)
        # return HttpResponse("Data Updated Successfully")
    
    else:
            
        username = request.user.username
        user = User.objects.get(username = username)
        modelObj = StudentInfo.objects.filter(user = user)

        if len(modelObj) == 0:
            return HttpResponse("No data found")
        
        context = {
            'data': modelObj.values()[0]
        }

        # print("hi this is data", modelObj.values()[0], '\n', "username is: ", username, user, modelObj)
        return render(request, 'home/edit.html', context)


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
        print(context)
        return render(request, 'home/viewer.html', context)
    

def DataFilter(request):

    # get user object
    username = request.user.username
    if username == 'cdc':
        context = {'admin': True}
        print("ture for admin")
    else:
        print("no not the admin")
        context = {'admin': False}

    if request.method == 'POST':

        department = request.POST.get('dept')
        year = request.POST.get('year')
        placedStatus = request.POST.get('ps')

        details = StudentInfo.objects.all()

        if department=="ad":
            details = details.filter(branch="AD")
        elif department=="cse":
            details = details.filter(branch="CSE")
        elif department=="ece":
            details = details.filter(branch="ECE")
        elif department=="eee":
            details = details.filter(branch="EEE")

        if year=="2020":
            details = details.filter(yop="2020")
        elif year=="2021":
            details = details.filter(yop="2021")
        elif year=="2022":
            details = details.filter(yop="2022")
        elif year=="2023":
            details = details.filter(yop="2023")
        elif year=="2024":
            details = details.filter(yop="2024")

        if placedStatus=="placed":
            details = details.filter(placementStatus=True)
        elif placedStatus=="nonplaced":
            details = details.filter(placementStatus=False)
        
        context['details'] = details

        return render(request, 'home/viewer.html', context)

    else:
        pass


    
    return render(request, 'home/viewer.html', context)










        
