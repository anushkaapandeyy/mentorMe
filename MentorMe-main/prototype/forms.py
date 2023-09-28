from django import forms
from .models import User, Skill, Question
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("email", 'password')

class SignUpForm(UserCreationForm):
    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all())
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "user_type", "skills", 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        if commit:
            user.save()
            self.save_m2m()
        return user
    
class QuestionForm(forms.ModelForm):
    title = forms.CharField()
    class Meta:
        model = Question
        fields = ['title']