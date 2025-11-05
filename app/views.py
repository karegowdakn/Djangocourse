from django.shortcuts import render #, redirect
from django.urls import reverse_lazy
from .models import Article
# from app.forms import CreateArticleForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "app/home.html"
    context_object_name = "articles"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'twitter_post', 'status']
    template_name = "app/create_article.html"
    success_url = reverse_lazy("home")

    # this will add a created user data to creator column in db
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'content', 'twitter_post', 'status']
    template_name = "app/update_article.html"
    success_url = reverse_lazy("home")
    context_object_name = "article"

    # this will not allow other users to edit an articles other than the creator
    def test_func(self):
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "app/delete_article.html"
    success_url = reverse_lazy("home")
    context_object_name = "article"
    
    # this will not allow other users to delete an articles other than the creator
    def test_func(self):
        return self.request.user == self.get_object().creator
    



# def home(request):
#     articles = Article.objects.all()
#     return render(request, "app/home.html", {"articles": articles})

# def create_article(request):
#     if request.method == "POST":
#         form = CreateArticleForm(request.POST)
#         if form.is_valid():
#             Article.objects.create(
#                 title=form.cleaned_data['title'],
#                 content=form.cleaned_data['content'],
#                 word_count=form.cleaned_data['word_count'],
#                 twitter_post=form.cleaned_data['twitter_post'],
#                 status=form.cleaned_data['status']
#             )
#             return redirect("home")
#     else:
#         form = CreateArticleForm()
    
#     return render(request, "app/create_article.html", {"form": form})


