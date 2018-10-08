from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'on','class':'form-control', 'placeholder':'Name'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile'}))
	address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))

	class Meta:
		model = Profile
		fields = [
		'name',
		'email',
		'mobile',
		'address',
		]

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if len(name)>30:
			raise forms.ValidationError('Name is longer than 30 characters')
		return name

	def clean_email(self):
		email = self.cleaned_data.get('email')
		pro = Profile.objects.filter(email=email)
		if len(pro)>0:
			raise forms.ValidationError('Email already registered')
		return email

	def clean_mobile(self):
		mobile = self.cleaned_data.get('mobile')
		try:
			a = int(mobile)
		except:
			raise forms.ValidationError('Incorrect Mobile Number')
		if len(mobile)!=10:
			raise forms.ValidationError('Incorrect Mobile Number')
		return mobile


class ProfileUpdateForm(ProfileForm):

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email
