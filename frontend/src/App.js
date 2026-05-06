import { useState, useEffect } from "react";

const API = "http://localhost:8000";

export default function App() {
  const [platform, setPlatform] = useState("");
  const [genre, setGenre] = useState("");
  const [year, setYear] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);

  const fetchHistory = async () => {
    const res = await fetch(`${API}/history`);
    const data = await res.json();
    setHistory(data);
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  const handlePredict = async () => {
    const res = await fetch(`${API}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ platform, genre, year: parseInt(year) }),
    });
    const data = await res.json();
    setResult(data.predicted_sales);
    fetchHistory();
  };

  return (
    <div style={{ maxWidth: 600, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h1>Game Sales Predictor</h1>

      <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
        <input placeholder="Platform (e.g. PS2)" value={platform} onChange={e => setPlatform(e.target.value)} />
        <input placeholder="Genre (e.g. Action)" value={genre} onChange={e => setGenre(e.target.value)} />
        <input placeholder="Year (e.g. 2005)" value={year} onChange={e => setYear(e.target.value)} />
        <button onClick={handlePredict}>Predict</button>
      </div>

      {result && <h2>Predicted Sales: {result} million units</h2>}

      <h3>Prediction History</h3>
      <table border="1" cellPadding="8" width="100%">
        <thead>
          <tr>
            <th>Platform</th>
            <th>Genre</th>
            <th>Year</th>
            <th>Predicted Sales</th>
          </tr>
        </thead>
        <tbody>
          {history.map(h => (
            <tr key={h.id}>
              <td>{h.platform}</td>
              <td>{h.genre}</td>
              <td>{h.year}</td>
              <td>{h.predicted_sales}M</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}