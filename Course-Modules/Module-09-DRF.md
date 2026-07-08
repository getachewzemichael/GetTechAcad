# Module 09 — Django REST Framework (API)
**Duration: 1.5 Weeks | Get.TechAcad**

---

## Learning Objectives
- [ ] Understand REST API concepts
- [ ] Install and configure DRF
- [ ] Write serializers for data conversion
- [ ] Build API views using generics and ViewSets
- [ ] Apply authentication and permissions
- [ ] Test APIs with Postman

---

## 9.1 What is a REST API?

A **REST API** (Representational State Transfer) is a way for your Django backend to communicate with other systems (mobile apps, React frontend, third-party services) using HTTP.

| HTTP Method | Action | Example |
|-------------|--------|---------|
| GET | Read data | Get list of posts |
| POST | Create data | Create new post |
| PUT/PATCH | Update data | Update a post |
| DELETE | Delete data | Delete a post |

---

## 9.2 Setup
```bash
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

---

## 9.3 Serializers
```python
# portfolio/serializers.py
from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'slug']


class PostSerializer(serializers.ModelSerializer):
    category      = CategorySerializer(read_only=True)
    category_id   = serializers.IntegerField(write_only=True)
    author        = serializers.StringRelatedField(read_only=True)
    tags_count    = serializers.SerializerMethodField()

    class Meta:
        model  = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt',
            'category', 'category_id', 'author',
            'published', 'tags_count', 'created_at'
        ]
        read_only_fields = ['id', 'slug', 'created_at']

    def get_tags_count(self, obj):
        return obj.tags.count()

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters.")
        return value
```

---

## 9.4 API Views (Generic Views)
```python
# portfolio/api_views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class PostListCreateAPI(generics.ListCreateAPIView):
    queryset           = Post.objects.filter(published=True)
    serializer_class   = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields      = ['title', 'content']
    ordering_fields    = ['created_at', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset           = Post.objects.all()
    serializer_class   = PostSerializer
    lookup_field       = 'slug'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryListAPI(generics.ListAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


# Custom APIView example
class PostStatsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        data = {
            'total_posts':     Post.objects.count(),
            'published_posts': Post.objects.filter(published=True).count(),
            'draft_posts':     Post.objects.filter(published=False).count(),
            'categories':      Category.objects.count(),
        }
        return Response(data, status=status.HTTP_200_OK)
```

---

## 9.5 URL Configuration
```python
# portfolio/urls.py
from .api_views import (
    PostListCreateAPI, PostRetrieveUpdateDestroyAPI,
    CategoryListAPI, PostStatsAPI
)

urlpatterns += [
    path('api/posts/',                   PostListCreateAPI.as_view(),            name='api-posts'),
    path('api/posts/<slug:slug>/',       PostRetrieveUpdateDestroyAPI.as_view(), name='api-post-detail'),
    path('api/categories/',             CategoryListAPI.as_view(),              name='api-categories'),
    path('api/stats/',                  PostStatsAPI.as_view(),                 name='api-stats'),
]
```

---

## 9.6 Token Authentication
```bash
python manage.py migrate  # creates authtoken table
```

```python
# urls.py
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns += [
    path('api/token/', obtain_auth_token, name='api-token'),
]
```

**Getting a token with Postman:**
- POST to `/api/token/`
- Body (JSON): `{"username": "admin", "password": "yourpassword"}`
- Response: `{"token": "abc123..."}`
- Use in header: `Authorization: Token abc123...`

---

## 9.7 ViewSets and Routers (Advanced)
```python
# api_views.py
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset           = Post.objects.filter(published=True)
    serializer_class   = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field       = 'slug'

# urls.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
urlpatterns += router.urls
# Generates: /api/posts/, /api/posts/{slug}/, etc.
```

---

## 9.8 Testing with Postman

| Action | Method | URL | Auth |
|--------|--------|-----|------|
| List posts | GET | /api/posts/ | None |
| Get post | GET | /api/posts/slug/ | None |
| Create post | POST | /api/posts/ | Token |
| Update post | PUT | /api/posts/slug/ | Token |
| Delete post | DELETE | /api/posts/slug/ | Token |
| Get token | POST | /api/token/ | None |
| Get stats | GET | /api/stats/ | None |

---

## Mini-Project: Todo REST API
Build a complete Todo API with:
- Todo model (title, completed, created_at, user)
- List, Create, Update, Delete endpoints
- Token authentication
- Tested fully in Postman

---

## Quiz
1. What is the difference between `ListAPIView` and `ListCreateAPIView`?
2. What does a serializer do?
3. How does token authentication work?
4. What HTTP method is used to partially update a resource?
5. What does `perform_create()` allow you to do?

---
*Get.TechAcad | Module 09 of 12*
