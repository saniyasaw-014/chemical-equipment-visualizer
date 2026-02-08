import { useState } from "react";
import API from "../services/api";

export default function UploadCSV({ onUpload }) {
  const [status, setStatus] = useState("");

  const upload = async (e) => {
    setStatus("Uploading...");
    const file = e.target.files[0];
    const form = new FormData();
    form.append("file", file);

    const res = await API.post("upload/", form);
    onUpload(res.data);
    setStatus("Upload successful ✅");
  };

  return (
    <div>
      <h3>Upload CSV</h3>
      <input type="file" accept=".csv" onChange={upload} />
      <p>{status}</p>
    </div>
  );
}
