// When the browser window is resized, makeResponsive() is called.
d3.select(window).on("resize", makeResponsive);

// When the browser loads, makeResponsive() is called.
makeResponsive();

// The code for the chart is wrapped inside a function that
// automatically resizes the chart
function makeResponsive() {

  // if the SVG area isn't empty when the browser loads,
  // remove it and replace it with a resized version of the chart
  var svgArea = d3.select("body").select("svg");

  // clear svg is not empty
  if (!svgArea.empty()) {
    svgArea.remove();
  }

  // SVG wrapper dimensions are determined by the current width and
  // height of the browser window.
  var svgWidth = window.innerWidth;
  var svgHeight = window.innerHeight;

  margin = {
    top: 50,
    bottom: 50,
    right: 50,
    left: 50
  };

  var height = svgHeight - margin.top - margin.bottom;
  var width = svgWidth - margin.left - margin.right;

  // Append SVG element
  var svg = d3
    .select(".chart")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

  // Append group element
  var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // Read CSV
  d3.csv("USCarrier_Traffic_20180710132024.csv", function(err, schedulData) {

    // create Period parser
    var PeriodParser = d3.timeParse("%d-%b-%Y");

    // parse data
    schedulData.forEach(function(data) {
      data.Period = PeriodParser(data.Period);
      data.Scheduled = +data.Scheduled;
    });

    // create scales
    var xTimeScale = d3.scaleTime()
      .domain(d3.extent(schedulData, d => d.Period))
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([0, d3.max(schedulData, d => d.Scheduled)])
      .range([height, 0]);

    // create axes
    var xAxis = d3.axisBottom(xTimeScale);
    var yAxis = d3.axisLeft(yLinearScale).ticks(6);

    // append axes
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(xAxis);

    chartGroup.append("g")
      .call(yAxis);

    // line generator
    var line = d3.line()
      .x(d => xTimeScale(d.Period))
      .y(d => yLinearScale(d.Scheduled));

    // append line
    chartGroup.append("path")
      .data([schedulData])
      .attr("d", line)
      .attr("fill", "none")
      .attr("stroke", "red");

    // append circles
    var circlesGroup = chartGroup.selectAll("circle")
      .data(schedulData)
      .enter()
      .append("circle")
      .attr("cx", d => xTimeScale(d.Period))
      .attr("cy", d => yLinearScale(d.Scheduled))
      .attr("r", "10")
      .attr("fill", "gold")
      .attr("stroke-width", "1")
      .attr("stroke", "black");

    // Period formatter to display Periods nicely
    var PeriodFormatter = d3.timeFormat("%d-%b-%y");

    // Step 1: Append tooltip div
    var toolTip = d3.select("body")
      .append("div")
      .style("display", "none")
      .classed("tooltip", true);

    // Step 2: Create "mouseover" event listener to display tooltip
    circlesGroup.on("mouseover", function(d) {
      toolTip.style("display", "block")
          .html(
            `<strong>${PeriodFormatter(d.Period)}<strong><hr>${d.Scheduled}
        passangers`)
          .style("left", d3.event.pageX + "px")
          .style("top", d3.event.pageY + "px");
    })
      // Step 3: Create "mouseout" event listener to hide tooltip
      .on("mouseout", function() {
        toolTip.style("display", "none");
      });

  });
}
