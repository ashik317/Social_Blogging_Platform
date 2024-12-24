from django import forms
from .models import Friendship, Post

class FriendshipForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ['status', 'blocked']
        widgets = {
            'status': forms.HiddenInput(),
            'blocked': forms.HiddenInput(),
        }
    def clean_status(self):
        status = self.cleaned_data['status']
        if status not in ['sent', 'accepted', 'rejected']:
            raise forms.ValidationError('Invalid status')
        return status

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title',}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your post here...',
                'rows': 5,}),
        }