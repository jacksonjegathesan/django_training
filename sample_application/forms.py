# import form class from django
from django import forms




# import question from models.py
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"        
        widgets = {
            'published' : forms.DateInput(attrs={'placeholder': "date", "type":"date" })
        }


'''
# create a ModelForm
class QuestionForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Question
        fields = "__all__"
'''