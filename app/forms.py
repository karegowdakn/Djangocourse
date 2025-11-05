from django import forms
from app.models import Article

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'word_count', 'twitter_post', 'status']


# the following is the manual form definition, now replaced by the ModelForm above
# class CreateArticleForm(forms.Form):
#     title = forms.CharField(max_length=200, required=True)
#     content = forms.CharField(widget=forms.Textarea, required=False)
#     word_count = forms.IntegerField(required=True)
#     twitter_post = forms.CharField(widget=forms.Textarea, required=False)
#     status = forms.ChoiceField(
#         choices=[
#             ("draft", "Draft"),
#             ("published", "Published"),
#             ("in_progress", "In Progress"),
#         ],
#         required=True
#     )
