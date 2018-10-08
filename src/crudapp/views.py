from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ProfileForm, ProfileUpdateForm
from .models import Profile

def create_view(request):
	form = ProfileForm(request.POST or None)
	if request.method=='POST':
		if form.is_valid():
			print(form.cleaned_data)

			# First method to save

			# name = form.cleaned_data.get('name')
			# email = form.cleaned_data.get('email')
			# mobile = form.cleaned_data.get('mobile')
			# address = form.cleaned_data.get('address')

			# Profile.objects.create(
			# 	name=name,
			# 	email=email,
			# 	mobile=mobile,
			# 	address=address,
			# 	)

			# second method to save
			# form.save() automatically saves the data into that model which is specified in the forms.py file
			form.save()

			# reverse is used here because we are using dynamic urls
			# if we have to use static url there is no need of reverse
			# in HttpResponseRedirect we pass a url 

			new_email = form.cleaned_data.get("email")
			instance = get_object_or_404(Profile, email=new_email)

			# we pass kwargs which is a python dictionary to send information using urls
			return HttpResponseRedirect(reverse('crudapp:detail', kwargs={'id':instance.id}))

	context = {

		'title':'Create a new profile',
		'btntitle':"Submit",
		'form':form,

	} 

	return render(request, 'crudapp/form.html', context)


def list_view(request):

	all_profiles = Profile.objects.all()
	context = {
		'profile_list':all_profiles,
	}

	return render(request, 'crudapp/list.html', context)


def detail_view(request, id=None):
	profile = get_object_or_404(Profile, id=id)
	context = {
		'profile':profile,
	}
	return render(request, 'crudapp/detail.html', context)

def update_view(request, id=None):
	instance = get_object_or_404(Profile, id=id)
	# here instance is passed in the form because we have to show the form details in the frontend
	form = ProfileUpdateForm(request.POST or None, instance=instance)
	if request.method=='POST':
		if form.is_valid():
			form.save()

			new_email = form.cleaned_data.get("email")
			instance = get_object_or_404(Profile, email=new_email)

			return HttpResponseRedirect(reverse('crudapp:detail', kwargs={'id':instance.id}))

	context = {

		'title':'Update profile',
		'btntitle':"Update",
		'form':form,

	} 

	return render(request, 'crudapp/form.html', context)

def delete_view(request, id=None):
	instance = get_object_or_404(Profile, id=id)
	if request.method=='POST':
		instance = get_object_or_404(Profile, id=id)
		print(instance)
		instance.delete()

		return HttpResponseRedirect(reverse('crudapp:list'))

	context = {
		'profile':instance
	}

	return render(request, 'crudapp/delete.html', context)