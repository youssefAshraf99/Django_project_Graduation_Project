from django import forms
from .models import *


# Default form for this app

class HomeForm(forms.Form):			

	# Text input field for this form
	post = forms.CharField()
