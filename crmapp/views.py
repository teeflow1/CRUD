from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from crmapp.forms import UserRegisterForm, AddRecordForm
from crmapp.models import School
def home(request):
    record = School.objects.all()
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in Successfully!!")
            return redirect('home')
        
    else:
        return render(request, 'apps/home.html', {'record':record})
    
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfuly!!")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have been logged in Successfully")
            return redirect('home')
        else:
            messages.success(request, "There is an Error in your form")
            return redirect('register')
        
    else:
        form=UserRegisterForm()
        return render(request, 'apps/register.html', {'form':form})
    
    
    
def detail_record(request, pk):
    if request.user.is_authenticated:
        record = School.objects.get(id=pk)
        return render(request, 'apps/detail_record.html', {'record':record})
    
    else:
        messages.success(request, "You must be eligible to view this")
        return redirect('register')
    
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = School.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Your record has been deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be eligible to view this")
        return redirect('register')
    
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid:
                form.save()
                messages.success(request, "Your post have been added successfully")
                return redirect('home')
        return render(request, 'apps/add_record.html', {'form': form})
    
    else:
        messages.success(request, "You must be eligible to view this")
        return redirect('register')
    
    
def update_user(request, pk):
    if request.user.is_authenticated:
        update_record = School.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=update_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post have been Updated Successfully!!")
            return redirect('home')
        return render(request, 'apps/update_record.html', {'form': form})
    
    else:
        messages.success(request, "You are not eligible to View this")
        return redirect('register')
        
        
        
        
            
            
        
        
        
    
            
        
        
    
        
        
            
            
        

    
            
    
        
        
    
    
    
    

            
            
            
    
