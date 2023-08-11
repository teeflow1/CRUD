from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import School

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
        
        
class AddRecordForm(forms.ModelForm):
    first_name=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    last_name= forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    address=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    country=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    state=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    #city=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    mobile=forms.CharField( required = True, max_length=100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    
    
    class Meta:
        model = School
        exclude = ("user",)
    