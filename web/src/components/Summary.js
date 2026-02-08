export default function Summary({ data }) {
  if (!data) return null;

  return (
    <div style={{
      border: "1px solid #ddd",
      padding: "16px",
      marginTop: "20px",
      width: "400px",
      background: "#f9f9f9"
    }}>
      <h3>Summary</h3>
      <p><b>Total Equipment:</b> {data.total_equipment}</p>
      <p><b>Avg Flowrate:</b> {data.average_flowrate}</p>
      <p><b>Avg Pressure:</b> {data.average_pressure}</p>
      <p><b>Avg Temperature:</b> {data.average_temperature}</p>
    </div>
  );
}
