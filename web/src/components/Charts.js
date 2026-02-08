import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale } from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale);

export default function Charts({ data }) {
  if (!data) return null;

  const chartData = {
    labels: Object.keys(data.type_distribution),
    datasets: [{
      label: "Equipment Count",
      data: Object.values(data.type_distribution),
    }]
  };

  return <Bar data={chartData} />;
}
