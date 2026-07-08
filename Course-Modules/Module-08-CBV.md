# Module 08 — Class-Based Views (CBV)
**Duration: 4 Days | Get.TechAcad**

---

## Learning Objectives
- [ ] Understand FBV vs CBV and when to use each
- [ ] Use ListView, DetailView, CreateView, UpdateView, DeleteView
- [ ] Customize CBVs by overriding methods
- [ ] Apply LoginRequiredMixin for authentication

---

## 8.1 FBV vs CBV

| Feature | Function-Based View | Class-Based View |
|---------|--------------------|--------------------|
| Simplicity | Simpler for small views | More structured |
| Reusability | Manual | Built-in mixins |
| CRUD boilerplate | Write manually | Built-in generics |
| Best for | Simple logic, APIs | Standard CRUD pages |

---

## 8.2 Common Generic CBVs
```python
# views.py
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(published=True).count()
        return context


class PostListView(ListView):
    model               = Post
    template_name       = 'portfolio/post_list.html'
    context_object_name = 'posts'
    paginate_by         = 10

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-created_at')


class PostDetailView(DetailView):
    model               = Post
    template_name       = 'portfolio/post_detail.html'
    context_object_name = 'post'
    slug_field          = 'slug'
    slug_url_kwarg      = 'slug'


class PostCreateView(LoginRequiredMixin, CreateView):
    model         = Post
    form_class    = PostForm
    template_name = 'portfolio/post_form.html'
    success_url   = reverse_lazy('post-list')
    login_url     = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model         = Post
    form_class    = PostForm
    template_name = 'portfolio/post_form.html'
    success_url   = reverse_lazy('post-list')
    login_url     = '/login/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model       = Post
    template_name = 'portfolio/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    login_url   = '/login/'
```

---

## 8.3 URL Patterns for CBVs
```python
# urls.py
urlpatterns = [
    path('',                          HomeView.as_view(),           name='home'),
    path('posts/',                    PostListView.as_view(),        name='post-list'),
    path('posts/<slug:slug>/',        PostDetailView.as_view(),      name='post-detail'),
    path('posts/new/',                PostCreateView.as_view(),      name='post-create'),
    path('posts/<int:pk>/edit/',      PostUpdateView.as_view(),      name='post-update'),
    path('posts/<int:pk>/delete/',    PostDeleteView.as_view(),      name='post-delete'),
]
```

---

## 8.4 Pagination in Template
```html
<!-- templates/portfolio/post_list.html -->
{% for post in posts %}
  <div class="post-card">
    <h3><a href="{% url 'post-detail' post.slug %}">{{ post.title }}</a></h3>
    <p>{{ post.content|truncatewords:30 }}</p>
  </div>
{% endfor %}

<!-- Pagination controls -->
{% if is_paginated %}
  <div class="pagination">
    {% if page_obj.has_previous %}
      <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}
    <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
    {% if page_obj.has_next %}
      <a href="?page={{ page_obj.next_page_number }}">Next</a>
    {% endif %}
  </div>
{% endif %}
```

---

## Mini-Project: Refactor Blog with CBVs
Take your Module 04 blog and rewrite all views using CBVs. Add pagination to the post list.

---

## Quiz
1. What does `LoginRequiredMixin` do?
2. How do you override `get_queryset()` in a ListView?
3. What is `reverse_lazy()` and why use it instead of `reverse()`?
4. What is the difference between `CreateView` and `UpdateView`?

---
*Get.TechAcad | Module 08 of 12*
