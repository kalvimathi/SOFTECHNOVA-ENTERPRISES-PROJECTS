function toggleMenu() {
  const nav = document.getElementById('navLinks');
  nav.classList.toggle('active');
}

function openLogin() {
  document.getElementById('loginModal').style.display = 'flex';
}

function closeLogin() {
  document.getElementById('loginModal').style.display = 'none';
}
// 1. Mobile menu toggle (for future mobile design)
document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");

  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
    });
  }

  // 2. Enroll button alert (demo interaction)
  const enrollButtons = document.querySelectorAll(".course-card button");
  enrollButtons.forEach((button) => {
    button.addEventListener("click", () => {
      alert("You have successfully enrolled in the course!");
    });
  });

  // 3. Search filter (Courses page only)
  const searchInput = document.querySelector(".search-bar");
  const courseCards = document.querySelectorAll(".course-card");

  if (searchInput) {
    searchInput.addEventListener("input", () => {
      const value = searchInput.value.toLowerCase();
      courseCards.forEach((card) => {
        const title = card.querySelector("h3").textContent.toLowerCase();
        card.style.display = title.includes(value) ? "block" : "none";
      });
    });
  }

  // 4. Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth",
      });
    });
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const logoutBtn = document.getElementById("logoutBtn");

  if (logoutBtn) {
    logoutBtn.addEventListener("click", (e) => {
      e.preventDefault();
      // Clear user data from storage
      localStorage.removeItem("user"); // or sessionStorage.removeItem("user");
      alert("You have been logged out.");
      window.location.href = "index.html"; // Redirect to homepage or login page
    });
  }
});
