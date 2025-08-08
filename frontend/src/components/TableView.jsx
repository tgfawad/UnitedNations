import React from "react";

export default function TableView({ rows }) {
  return (
    <table className="data-table">
      <thead>
        <tr>
          <th>Year</th>
          <th>Population</th>
        </tr>
      </thead>
      <tbody>
        {(rows || []).map((r) => (
          <tr key={r.year}>
            <td>{r.year}</td>
            <td>{Number(r.population).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
