import React, { useEffect, useRef } from "react";
import PropTypes from "prop-types";
import * as d3 from "d3";

export default function ChartView({ rows, fill = "steelblue" }) {
  const ref = useRef(null);

  useEffect(() => {
    if (!ref.current) return;
    const data = (rows || [])
      .slice()
      .sort((a, b) => d3.ascending(a.year, b.year));

    const width = 700;
    const height = 400;
    const margin = { top: 20, right: 20, bottom: 40, left: 80 };

    const svg = d3
      .select(ref.current)
      .attr("viewBox", `0 0 ${width} ${height}`)
      .attr("width", "100%")
      .attr("height", "100%");

    svg.selectAll("*").remove();

    const x = d3
      .scaleBand()
      .domain(data.map((d) => d.year))
      .range([margin.left, width - margin.right])
      .padding(0.2);

    // Scale to millions for display
    const maxPop = d3.max(data, (d) => d.population) || 0;
    const y = d3
      .scaleLinear()
      .domain([0, maxPop / 1_000_000])
      .nice()
      .range([height - margin.bottom, margin.top]);

    // Axis
    svg
      .append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x));

    svg
      .append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y).ticks(8))
      .append("text")
      .attr("fill", "currentColor")
      .attr("x", -40)
      .attr("y", margin.top - 10)
      .attr("text-anchor", "start")
      .text("Population (million)");

    // Bars
    svg
      .append("g")
      .selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", (d) => x(d.year))
      .attr("y", (d) => y(d.population / 1_000_000))
      .attr("width", x.bandwidth())
      .attr("height", (d) => y(0) - y(d.population / 1_000_000))
      .attr("fill", fill);
  }, [rows, fill]);

  return (
    <div className="chart-wrapper">
      <svg
        ref={ref}
        aria-roledescription="bar chart"
        aria-label="US Population bar chart"
      />
    </div>
  );
}

ChartView.propTypes = {
  rows: PropTypes.arrayOf(
    PropTypes.shape({
      year: PropTypes.oneOfType([PropTypes.string, PropTypes.number])
        .isRequired,
      population: PropTypes.oneOfType([PropTypes.string, PropTypes.number])
        .isRequired,
    })
  ),
  fill: PropTypes.string,
};
