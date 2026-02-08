import { useEffect, useState } from "react";
import API from "../services/api";

export default function History() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    API.get("history/").then(res => setHistory(res.data));
  }, []);

  return (
    <div>
      <h3>Upload History</h3>
      <ul>
        {history.map((h, i) => (
          <li key={i}>{h.filename} - {h.uploaded_at}</li>
        ))}
      </ul>
    </div>
  );
}
