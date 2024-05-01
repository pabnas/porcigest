// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.font.family = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.font.defaultFontColor = '#858796';

// Pie Chart 

var ctx = document.getElementById("myPieChart");
var data = {
  labels: ["Nivel del agua", "Restante"],
  datasets: [{
    data: [80,20],
    backgroundColor: ['#3C8DBC','#EEEEEE'],
    hoverBackgroundColor: ['#3C8DBC','#EEEEEE'],
    hoverBorderColor: "rgba(234, 236, 244, 1)",
  }],
};

var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: data,
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: false
        },
        tooltips: {
           enabled: false
        },
    },
    cutoutPercentage: 80,
  },
});
