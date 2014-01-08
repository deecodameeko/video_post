from django import forms

class VideoForm(forms.Form):
	file  = forms.FileField()