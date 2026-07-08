# Module 10 — Frontend Integration and AJAX
**Duration: 1 Week | Get.TechAcad**

---

## Learning Objectives
- [ ] Consume Django APIs from JavaScript using Fetch
- [ ] Implement live search without page refresh
- [ ] Load dynamic content from Django views
- [ ] Pass Django context data to JavaScript

---

## 10.1 Passing Django Data to JavaScript

```html
<!-- In template -->
{% load static %}
<script>
  // Pass Django variable to JavaScript safely
  const SITE_NAME   = "{{ site_name|escapejs }}";
  const API_BASE    = "{{ request.scheme }}://{{ request.get_host }}";
  const IS_AUTH     = {{ user.is_authenticated|yesno:"true,false" }};
</script>
```

---

## 10.2 AJAX Live Search

**Django view:**
```python
# views.py
from django.http import JsonResponse
from .models import Post

def search_api(request):
    query = request.GET.get('q', '').strip()
    if len(query) < 2:
        return JsonResponse({'results': []})

    posts = Post.objects.filter(
        title__icontains=query,
        published=True
    ).values('title', 'slug', 'content')[:8]

    results = [
        {
            'title':   p['title'],
            'slug':    p['slug'],
            'excerpt': p['content'][:120] + '...' if len(p['content']) > 120 else p['content'],
        }
        for p in posts
    ]
    return JsonResponse({'results': results})
```

**URL:**
```python
path('api/search/', views.search_api, name='search-api'),
```

**JavaScript (Fetch API):**
```javascript
// static/js/main.js
const searchInput = document.getElementById('search-input');
const resultsBox  = document.getElementById('search-results');

if (searchInput) {
    let debounceTimer;

    searchInput.addEventListener('input', function () {
        clearTimeout(debounceTimer);
        const query = this.value.trim();

        if (query.length < 2) {
            resultsBox.innerHTML = '';
            resultsBox.style.display = 'none';
            return;
        }

        debounceTimer = setTimeout(async () => {
            try {
                const response = await fetch(`/api/search/?q=${encodeURIComponent(query)}`);
                const data = await response.json();

                if (data.results.length === 0) {
                    resultsBox.innerHTML = '<div class="search-no-result">No results found.</div>';
                } else {
                    resultsBox.innerHTML = data.results.map(post => `
                        <a href="/posts/${post.slug}/" class="search-result-item">
                            <div class="search-result-title">${post.title}</div>
                            <div class="search-result-excerpt">${post.excerpt}</div>
                        </a>
                    `).join('');
                }
                resultsBox.style.display = 'block';
            } catch (error) {
                console.error('Search error:', error);
            }
        }, 300); // debounce 300ms
    });

    // Hide results when clicking outside
    document.addEventListener('click', function (e) {
        if (!searchInput.contains(e.target)) {
            resultsBox.style.display = 'none';
        }
    });
}
```

**HTML:**
```html
<div class="search-wrapper">
  <input type="text" id="search-input" placeholder="Search posts..." class="form-control">
  <div id="search-results" class="search-dropdown" style="display:none;"></div>
</div>
```

---

## 10.3 AJAX Form Submission

**Django view:**
```python
import json
from django.views.decorators.csrf import csrf_exempt

def like_post(request, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        post.views_count += 1
        post.save()
        return JsonResponse({'views': post.views_count, 'status': 'ok'})
    return JsonResponse({'error': 'Unauthorized'}, status=401)
```

**JavaScript:**
```javascript
document.getElementById('like-btn').addEventListener('click', async function () {
    const postId = this.dataset.postId;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch(`/posts/${postId}/like/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
        },
    });
    const data = await response.json();
    document.getElementById('views-count').textContent = data.views;
});
```

---

## 10.4 Load More (Infinite Scroll)
```javascript
let page = 1;
const loadMoreBtn = document.getElementById('load-more');

if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', async () => {
        page++;
        const response = await fetch(`/api/posts/?page=${page}`);
        const data = await response.json();
        const container = document.getElementById('posts-container');

        data.results.forEach(post => {
            container.insertAdjacentHTML('beforeend', `
                <div class="post-card">
                    <h3><a href="/posts/${post.slug}/">${post.title}</a></h3>
                    <p>${post.excerpt || ''}</p>
                </div>
            `);
        });

        if (!data.next) loadMoreBtn.style.display = 'none';
    });
}
```

---

## Mini-Project: Live Search Feature
Add a live search bar to your blog that searches posts as the user types, showing results in a dropdown without any page reload.

---

## Quiz
1. What is AJAX and why is it useful?
2. What does `fetch()` return?
3. Why do we use debouncing on the search input?
4. What is the CSRF token and why must it be sent with POST requests?

---
*Get.TechAcad | Module 10 of 12*
