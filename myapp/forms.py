from django import forms
from models import UserModel,PostModel,LikeModel,CommentModel
#creating forms

#creating signup form
class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['email','username','name','password']

#creating login form
class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

#creating post form
class PostForm(forms.ModelForm) :
    class Meta:
        model = PostModel
        fields = ['image', 'caption']

#creating like form
class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']

#creating comment form
class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']