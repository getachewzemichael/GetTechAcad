// ===== DARK / LIGHT MODE TOGGLE =====
(function () {
  // Handles both desktop (#themeToggle) and mobile (#themeToggleMobile) buttons
  function applyTheme(isLight) {
    document.body.classList.toggle('light-mode', isLight);
    ['themeIcon', 'themeIconMobile'].forEach(function (id) {
      const icon = document.getElementById(id);
      if (!icon) return;
      if (isLight) {
        icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
      } else {
        icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
      }
    });
  }

  // Apply saved preference immediately (no flash)
  const saved = localStorage.getItem('theme');
  applyTheme(saved === 'light');

  // Attach click to both buttons
  ['themeToggle', 'themeToggleMobile'].forEach(function (id) {
    const btn = document.getElementById(id);
    if (!btn) return;
    btn.addEventListener('click', function () {
      const isLight = !document.body.classList.contains('light-mode');
      applyTheme(isLight);
      localStorage.setItem('theme', isLight ? 'light' : 'dark');
    });
  });
})();

// ===== NAVBAR SCROLL EFFECT =====
window.addEventListener('scroll', function () {
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    if (window.scrollY > 50) {
      navbar.classList.add('navbar-scrolled');
    } else {
      navbar.classList.remove('navbar-scrolled');
    }
  }
});

// ===== ACTIVE NAV LINK — handled via Django template blocks =====
// Each page template sets {% block nav_X %}active{% endblock %} on its link.

// ===== BACK TO TOP =====
const backToTop = document.getElementById('backToTop');
if (backToTop) {
  window.addEventListener('scroll', function () {
    if (window.scrollY > 400) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  });

  backToTop.addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ===== FADE-UP ANIMATION ON SCROLL =====
const observer = new IntersectionObserver(function (entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.05 });

document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

// ===== SKILL BAR ANIMATION =====
const skillObserver = new IntersectionObserver(function (entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.skill-fill').forEach(bar => {
        const width = bar.getAttribute('data-width');
        setTimeout(() => { bar.style.width = width + '%'; }, 200);
      });
    }
  });
}, { threshold: 0.3 });

document.querySelectorAll('.skill-category').forEach(cat => skillObserver.observe(cat));

// ===== TYPED TEXT EFFECT =====
(function () {
  const el = document.getElementById('typed-text');
  if (!el) return;
  const texts = [
    'Computer Science Engineer',
    'Digital Marketing Trainer',
    'AI & Software Developer',
    'Technology Consultant',
    'Founder of Get.TechAcad'
  ];
  let textIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let delay = 100;

  function type() {
    const current = texts[textIndex];
    if (isDeleting) {
      el.textContent = current.substring(0, charIndex--);
      delay = 60;
    } else {
      el.textContent = current.substring(0, charIndex++);
      delay = 100;
    }

    if (!isDeleting && charIndex === current.length + 1) {
      isDeleting = true;
      delay = 1800;
    } else if (isDeleting && charIndex === -1) {
      isDeleting = false;
      textIndex = (textIndex + 1) % texts.length;
      delay = 400;
    }

    setTimeout(type, delay);
  }

  setTimeout(type, 800);
})();

// ===== COUNTER ANIMATION =====
document.querySelectorAll('.counter').forEach(counter => {
  const target = parseInt(counter.getAttribute('data-target'));
  const duration = 2000;
  const step = target / (duration / 16);
  let current = 0;

  const counterObserver = new IntersectionObserver(function (entries) {
    if (entries[0].isIntersecting) {
      const interval = setInterval(() => {
        current += step;
        if (current >= target) {
          counter.textContent = target;
          clearInterval(interval);
        } else {
          counter.textContent = Math.floor(current);
        }
      }, 16);
      counterObserver.unobserve(counter);
    }
  });

  counterObserver.observe(counter);
});

// ===== AUTO DISMISS ALERTS =====
setTimeout(function () {
  document.querySelectorAll('.alert').forEach(alert => {
    alert.style.transition = 'opacity 0.5s';
    alert.style.opacity = '0';
    setTimeout(() => alert.remove(), 500);
  });
}, 4000);
