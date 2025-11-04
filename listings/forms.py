from django import forms
from .models import Listing, Report, Message

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'category', 'image', 'status', 'slug']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
