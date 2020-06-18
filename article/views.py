from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm


# Create your views here.


class ArticleUpdateView(UpdateView):
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # model = Article
    template_name = "article_create.html"


class ArticleCreateView(CreateView):
    queryset = Article.objects.all()
    form_class = ArticleModelForm
    success_url = '/articles'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # model = Article
    template_name = "article_create.html"


class ArticleListView(ListView):
    queryset = Article.objects.all()
    # model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    # queryset = Article.objects.all()
    # model = Article
    template_name = "article_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    # queryset = Article.objects.all()
    # model = Article
    template_name = "article_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    def get_success_url(self):
        return reverse('article:article-list')

