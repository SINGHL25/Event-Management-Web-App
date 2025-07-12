fetch("/api/events")
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("events");
    container.innerHTML = data.map(e => `<p>${e.name} - ${e.category}</p>`).join("");
  });
