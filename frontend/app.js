## 📄 frontend/app.js
```javascript
fetch("http://localhost:8000/events")
  .then(res => res.json())
  .then(events => {
    const el = document.getElementById("event-list");
    events.forEach(evt => {
      const div = document.createElement("div");
      div.innerHTML = `<h3>${evt.title}</h3><p>${evt.description}</p>`;
      el.appendChild(div);
    });
  });
```
