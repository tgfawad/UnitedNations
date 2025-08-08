import React from "react";
import PropTypes from "prop-types";

export default function Menu({ items, onSelect, selected }) {
  return (
    <nav>
      <ul className="menu">
        {(items || []).map((item) => (
          <li key={item.label}>
            <button
              className={`menu-item ${
                selected?.label === item.label ? "active" : ""
              }`}
              onClick={() => onSelect(item)}
            >
              {item.label}
            </button>
          </li>
        ))}
      </ul>
    </nav>
  );
}

Menu.propTypes = {
  items: PropTypes.arrayOf(
    PropTypes.shape({
      label: PropTypes.string.isRequired,
      rule: PropTypes.string.isRequired,
      type: PropTypes.string.isRequired,
      params: PropTypes.object,
    })
  ),
  onSelect: PropTypes.func.isRequired,
  selected: PropTypes.object,
};
