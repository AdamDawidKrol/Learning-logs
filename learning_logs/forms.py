from django import forms
from .models import Topic, Entry, MainTopic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        
class MainTopicForm(forms.ModelForm):
    class Meta:
        model = MainTopic
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text:' ''}
        widget = {'text': forms.Textarea(attrs={'cols': 80})}
        
