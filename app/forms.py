from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    
CustomUser = get_user_model()

class StaffUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('phone', 'address')    
