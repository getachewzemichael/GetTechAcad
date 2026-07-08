# Module 02 — Web Fundamentals (HTML, CSS, Bootstrap)
**Duration: 1 Week | Get.TechAcad**

---

## Learning Objectives
- [ ] Build structured HTML pages with semantic tags
- [ ] Style with CSS (flexbox, grid, variables)
- [ ] Build responsive layouts with Bootstrap 5
- [ ] Understand how these connect to Django templates

---

## HTML Essentials
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Get.TechAcad</title>
</head>
<body>
  <header><nav><a href="/">Home</a></nav></header>
  <main>
    <h1>Welcome</h1>
    <p>Technology Education Platform</p>
  </main>
  <footer><p>&copy; 2024 Get.TechAcad</p></footer>
</body>
</html>
```

---

## CSS Essentials
```css
:root {
  --primary: #1fda57;
  --bg: #020d12;
}

body { background: var(--bg); color: #e0e6ed; }

.card {
  padding: 1.5rem;
  border-radius: 12px;
  border: 1px solid #1e3a2f;
}

/* Flexbox */
.navbar { display: flex; justify-content: space-between; align-items: center; }

/* Responsive */
@media (max-width: 768px) {
  .grid { grid-template-columns: 1fr; }
}
```

---

## Bootstrap 5 Essentials
```html
<!-- Include -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Grid -->
<div class="container">
  <div class="row g-4">
    <div class="col-lg-4 col-md-6">Card 1</div>
    <div class="col-lg-4 col-md-6">Card 2</div>
    <div class="col-lg-4 col-md-6">Card 3</div>
  </div>
</div>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="/">Brand</a>
    <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#nav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="nav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link" href="/about">About</a></li>
      </ul>
    </div>
  </div>
</nav>
```

---

## Mini-Project: Responsive Landing Page
Build a landing page for Get.TechAcad with:
- Navbar with logo and links
- Hero section with CTA button
- 3-column course cards grid
- Contact form
- Footer

---
*Get.TechAcad | Module 02 of 12*
