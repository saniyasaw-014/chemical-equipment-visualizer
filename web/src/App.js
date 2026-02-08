import { useState } from "react";
import Login from "./components/Login";
import UploadCSV from "./components/UploadCSV";
import Summary from "./components/Summary";
import Charts from "./components/Charts";
import History from "./components/History";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [summary, setSummary] = useState(null);

  if (!loggedIn) return <Login onLogin={() => setLoggedIn(true)} />;

  return (
    <div>
      <h1>Chemical Equipment Visualizer</h1>
      <UploadCSV onUpload={setSummary} />
      <Summary data={summary} />
      <Charts data={summary} />
      <History />
    </div>
  );
}

export default App;
