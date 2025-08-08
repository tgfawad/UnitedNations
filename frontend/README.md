Frontend notes

- The UI layout uses CSS Grid for a sticky header and a split pane with a 30% sidebar and 70% content area.
- The app is fully data-driven by /api/getMenu.
- Runtime API base URL is injected via /config.js by Nginx (no rebuild needed).
