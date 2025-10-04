const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
  // Cambiar a estado de carga
  btn.classList.add("loading");

  // Esperar al final de la animación (3s)
  setTimeout(() => {
    btn.classList.remove("loading");
    btn.textContent = "Iniciar"; // restaurar texto
    alert("¡Completado!");
  }, 3000); // mismo tiempo que la animación CSS
});
