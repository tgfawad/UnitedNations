import React, { useEffect, useMemo, useState } from "react";
import Menu from "./components/Menu.jsx";
import TextView from "./components/TextView.jsx";
import TableView from "./components/TableView.jsx";
import ChartView from "./components/ChartView.jsx";
import "./app.css";

const apiBase = window.APP_CONFIG?.API_BASE_URL || "http://localhost:5000";

export default function App() {
  const [menu, setMenu] = useState([]);
  const [selected, setSelected] = useState(null);
  const [content, setContent] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${apiBase}/api/getMenu?locale=en`)
      .then((r) => r.json())
      .then(setMenu)
      .catch((e) => setError(String(e)));
  }, []);

  useEffect(() => {
    if (!selected) return;
    setLoading(true);
    setError(null);
    fetch(`${apiBase}${selected.rule}`)
      .then((r) => r.json())
      .then((data) => setContent(data))
      .catch((e) => setError(String(e)))
      .finally(() => setLoading(false));
  }, [selected]);

  const view = useMemo(() => {
    if (!selected) return null;
    if (selected.type === "text") {
      const fontSize = selected.params?.["font-size"] || "30px";
      return <TextView text={content?.text || ""} fontSize={fontSize} />;
    }
    if (selected.type === "table") {
      return <TableView rows={Array.isArray(content) ? content : []} />;
    }
    if (selected.type === "chart") {
      const fill = selected.params?.fill || "steelblue";
      return (
        <ChartView rows={Array.isArray(content) ? content : []} fill={fill} />
      );
    }
    return <div>Unsupported type: {selected.type}</div>;
  }, [selected, content]);

  return (
    <div className="layout">
      <header className="header">Welcome on our page</header>
      <aside className="sidebar">
        <Menu items={menu} onSelect={setSelected} selected={selected} />
      </aside>
      <main className="content">
        {error && <div className="error">{error}</div>}
        {loading && <div>Loading...</div>}
        {!loading && !error && view}
      </main>
    </div>
  );
}
