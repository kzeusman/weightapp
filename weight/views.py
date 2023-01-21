from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login , logout, authenticate
from .forms import WeightForm
from .models import Weight
from django.utils import timezone
from django.contrib.auth.decorators import login_required




def home(request):
	return render(request, 'weight/home.html')


def signupuser(request):
	if request.method == "GET":

		return render(request, 'weight/signupuser.html', {'form':UserCreationForm()})
	else:
		# Create a new user (POST)
		if request.POST["password1"] == request.POST["password2"]:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('currentweights')
			except IntegrityError:
				return render(request, 'weight/signupuser.html', {'form':UserCreationForm(), 'error':"That username has already been taken Please select a new username"})
		else:
			#send a password doent match
			return render(request, 'weight/signupuser.html', {'form':UserCreationForm(), 'error':"Passwords did not match"})

def loginuser(request):
	if request.method == "GET":

		return render(request, 'weight/loginuser.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'weight/loginuser.html', {'form':AuthenticationForm(), 'error':'Username or password did not match'})
		else:
			login(request, user)
			return redirect('currentweights')

@login_required
def logoutuser(request):
	if request.method == "POST":
		logout(request)
		return redirect('home')
@login_required
def createweight(request):
	if request.method == "GET":
		return render(request, 'weight/createweight.html', {'form':WeightForm()})

	else:
		try:
			form = WeightForm(request.POST)
			newweight = form.save(commit=False)
			newweight.user = request.user
			newweight.save()
			return redirect('currentweights')
		except ValueError:
			return render(request, 'weight/createweight.html', {'form':WeightForm(),'error':'bad data'})

@login_required
def currentweights(request):
	weights = Weight.objects.filter(user=request.user, datecompletes__isnull=True).order_by('created')
	return render(request, 'weight/currentweights.html',{'weights':weights})

@login_required
def completedweights(request):
	weights = Weight.objects.filter(user=request.user, datecompletes__isnull=False).order_by('-datecompletes')
	return render(request, 'weight/completedweights.html',{'weights':weights})


@login_required
def viewweights(request, weight_pk):
	weight = get_object_or_404(Weight, pk=weight_pk, user=request.user)
	if request.method == "GET":
		form = WeightForm(instance=weight)
		return render(request, 'weight/viewweight.html',{'weight':weight, 'form':form})
	else:
		try:
			form = WeightForm(request.POST,instance=weight)
			form.save()
			return redirect('currentweights')

		except ValueError:
			return render(request, 'weight/viewweight.html',{'weight':weight, 'form':form, 'error':'Bad Data'})

@login_required
def completeweights(request,weight_pk):	
	weight = get_object_or_404(Weight, pk=weight_pk, user=request.user)
	if request.method == "POST":
		weight.datecompletes = timezone.now()
		weight.save()
		return redirect('currentweights')

@login_required
def deleteweights(request,weight_pk):	
	weight = get_object_or_404(Weight, pk=weight_pk, user=request.user)
	if request.method == "POST":
		
		weight.delete()
		return redirect('currentweights')
