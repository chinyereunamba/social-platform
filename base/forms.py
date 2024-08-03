from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    post = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write your post here...",
                "rows": 10,
                "cols": 40,
                "style": "resize: none;",
            }
        )
    )

    class Meta:
        model = Post
        fields = ["post"]


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write your post here...",
                "rows": 10,
                "cols": 40,
                "style": "resize: none;",
            }
        )
    )
    class Meta:
        model = Comment
        fields = ["comment"]
