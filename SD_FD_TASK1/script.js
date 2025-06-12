// ========== Dark Mode Toggle ========== //
const toggle = document.getElementById('dark-mode-toggle');

// Load dark mode preference
if (localStorage.getItem('dark-mode') === 'enabled') {
  document.body.classList.add('dark-mode');
}

toggle.addEventListener('click', () => {
  document.body.classList.toggle('dark-mode');
  // Save preference
  if (document.body.classList.contains('dark-mode')) {
    localStorage.setItem('dark-mode', 'enabled');
  } else {
    localStorage.setItem('dark-mode', 'disabled');
  }
});

// ========== Scroll Reveal Animation ========== //
function revealOnScroll() {
  const reveals = document.querySelectorAll('section');
  for (let i = 0; i < reveals.length; i++) {
    const windowHeight = window.innerHeight;
    const elementTop = reveals[i].getBoundingClientRect().top;
    const elementVisible = 100;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add('reveal');
    } else {
      reveals[i].classList.remove('reveal');
    }
  }
}
window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll); // Reveal on load

// ========== Highlight Active Navigation Link ========== //
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('.nav-links a');

function highlightNav() {
  let current = '';

  sections.forEach((section) => {
    const sectionTop = section.offsetTop - 100;
    if (scrollY >= sectionTop) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
}
window.addEventListener('scroll', highlightNav);

// ========== Smooth Scrolling to Anchors ========== //
navLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute("href").substring(1);
    const target = document.getElementById(targetId);
    if (target) {
      window.scrollTo({
        top: target.offsetTop - 50,
        behavior: "smooth"
      });
    }
  });
});

// ========== Enhanced Contact Form ========== //
document.querySelector('form').addEventListener('submit', function (e) {
  e.preventDefault();

  const name = this.querySelector('input[type="text"]').value.trim();
  const email = this.querySelector('input[type="email"]').value.trim();
  const message = this.querySelector('textarea').value.trim();

  if (!name || !email || !message) {
    alert("Please fill out all fields.");
    return;
  }

  if (!/^\S+@\S+\.\S+$/.test(email)) {
    alert("Please enter a valid email address.");
    return;
  }

  alert(`Thank you, ${name}! Your message has been received.`);
  this.reset();
});
