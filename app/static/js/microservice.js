const ctx = document.getElementById("statisticsChart").getContext("2d");

const statisticsChart = new Chart(ctx, {
	type: "line",
	data: {
		labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
		datasets: [
			{
				label: "Score",
				borderColor: "#177dff",
				pointBackgroundColor: "rgba(23, 125, 255, 0.6)",
				pointRadius: 0,
				backgroundColor: "rgba(23, 125, 255, 0.4)",
				legendColor: "#177dff",
				fill: true,
				borderWidth: 2,
				data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 900],
			},
		],
	},
	options: {
		responsive: true,
		maintainAspectRatio: false,
		legend: {
			display: false,
		},
		interaction: {
			mode: "index",
			intersect: false,
		},
		tooltips: {
			bodySpacing: 4,
			mode: "nearest",
			intersect: 0,
			position: "nearest",
			xPadding: 10,
			yPadding: 10,
			caretPadding: 10,
		},
		layout: {
			padding: { left: 5, right: 5, top: 15, bottom: 15 },
		},
		scales: {
			yAxes: [
				{
					ticks: {
						fontStyle: "500",
						beginAtZero: false,
						maxTicksLimit: 5,
						padding: 10,
					},
					gridLines: {
						drawTicks: false,
						display: false,
					},
				},
			],
			xAxes: [
				{
					gridLines: {
						zeroLineColor: "transparent",
					},
					ticks: {
						padding: 10,
						fontStyle: "500",
					},
				},
			],
		},
	},
});

const lineChartContext = document.getElementById("lineChart").getContext("2d");

const lineChart = new Chart(lineChartContext, {
	type: "line",
	data: {
		labels: ["S", "M", "T", "W", "T", "F", "S", "S", "M", "T"],
		datasets: [
			{
				label: "Number Of Commits Per Day",
				backgroundColor: "rgba(220,53,69,0.3)",
				borderColor: "#dc3545",
				pointBackgroundColor: "#dc3545",
				pointRadius: 0,
				borderWidth: 2,
				data: [6, 4, 9, 5, 4, 6, 4, 3, 8, 10],
			},
			{
				label: "Total Number Of successful Builds",
				backgroundColor: "rgba(23, 125, 255, 0.3)",
				borderColor: "rgba(23, 125, 255)",
				pointBackgroundColor: "rgba(23, 125, 255)",
				pointRadius: 0,
				borderWidth: 2,
				data: [1, 2, 2, 7, 2, 6, 1, 5, 12, 6],
			},
		],
	},
	options: {
		responsive: true,
		maintainAspectRatio: false,
		legend: {
			display: false,
		},
		interaction: {
			mode: "index",
			intersect: false,
		},
	},
});
