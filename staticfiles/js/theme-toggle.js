// theme-toggle.js

const themeToggle = document.querySelector(".theme-controller");
const savedTheme = localStorage.getItem("theme") || "dracula";

document.documentElement.setAttribute("data-theme", savedTheme);
themeToggle.checked = savedTheme === "forest";

themeToggle.addEventListener("change", ({ target }) => {
  const theme = target.checked ? "forest" : "dracula";
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);
});
