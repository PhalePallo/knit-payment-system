// src/pages/SchoolRevenue.jsx
import React, { useState, useEffect } from "react";
import api from "../api/api.js";

export default function SchoolRevenue() {
  const [schools, setSchools] = useState([]);
  const [schoolId, setSchoolId] = useState("");
  const [revenue, setRevenue] = useState(null);
  const [status, setStatus] = useState(null); // 'success' or 'error'

  // Load schools from backend
  useEffect(() => {
    api.get("/schools")
      .then(res => setSchools(res.data))
      .catch(err => console.error("Failed to load schools:", err));
  }, []);

  const fetchRevenue = async () => {
    if (!schoolId) {
      setRevenue({ error: "Please select a school" });
      setStatus("error");
      return;
    }

    setRevenue(null);
    setStatus(null);

    try {
      const res = await api.get(`/schools/${schoolId}/revenue`);
      setRevenue(res.data);
      setStatus("success");
    } catch (err) {
      setRevenue({ error: "Failed to fetch revenue" });
      setStatus("error");
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "20px auto", fontFamily: "Arial, sans-serif" }}>
      <h2>School Revenue</h2>
      <label>
        School:
        <select value={schoolId} onChange={e => setSchoolId(e.target.value)}>
          <option value="">Select School</option>
          {schools.map(s => (
            <option key={s.id} value={s.id}>{s.name}</option>
          ))}
        </select>
      </label>
      <button onClick={fetchRevenue} style={{ marginLeft: "10px", padding: "6px 12px", cursor: "pointer" }}>
        Get Revenue
      </button>

      {revenue && (
        <div
          style={{
            marginTop: "20px",
            padding: "10px",
            border: status === "success" ? "1px solid green" : "1px solid red",
            backgroundColor: status === "success" ? "#e0f8e0" : "#f8e0e0",
            color: status === "success" ? "green" : "red",
            borderRadius: "4px"
          }}
        >
          {status === "success" ? (
            <ul style={{ listStyleType: "none", paddingLeft: 0 }}>
              <li><strong>School:</strong> {revenue.school}</li>
              <li><strong>Total Collected:</strong> {revenue.total_collected}</li>
              <li><strong>Total Knit Fees:</strong> {revenue.total_knit_fees}</li>
              <li><strong>Total Paid to School:</strong> {revenue.total_paid_to_school}</li>
            </ul>
          ) : (
            <p>{revenue.error}</p>
          )}
        </div>
      )}
    </div>
  );
}