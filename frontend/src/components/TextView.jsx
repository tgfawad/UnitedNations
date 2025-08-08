import React from "react";
import PropTypes from "prop-types";

export default function TextView({ text, fontSize = "30px" }) {
  return <div style={{ fontSize }}>{text}</div>;
}

TextView.propTypes = {
  text: PropTypes.string.isRequired,
  fontSize: PropTypes.string,
};
