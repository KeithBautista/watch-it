from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
# Here you are calling the category object and get the values inside it
choice_list = []

for item in choices:
    choice_list.append(item)
    # This will loop through the choices in the choices list


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'title_tag',
            'author',
            'body',
            'snippet',
            'header_image')
        # Contains the fields that you have in your form in your models.py
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={
                'class':
                'form-control',
                'value': '',
                'id': 'postFormAuthor',
                'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            }


class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')
        # Contains the fields that you have in your form in your models.py
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            }
