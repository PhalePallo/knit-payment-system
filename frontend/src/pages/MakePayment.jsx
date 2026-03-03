// src/pages/MakePayment.jsx
import React, { useState, useEffect } from "react";
import api from "../api/api.js";

export default function MakePayment() {
  const [students, setStudents] = useState([]);
  const [studentId, setStudentId] = useState("");
  const [amount, setAmount] = useState("");
  const [reference, setReference] = useState("");
  const [result, setResult] = useState(null);
  const [status, setStatus] = useState(null);

  useEffect(() => {
    api.get("/students")
      .then(res => setStudents(res.data))
      .catch(err => {
        console.error(err);
        setStudents([]);
      });
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult(null);
    setStatus(null);

    if (!studentId) {
      setResult({ error: "Please select a student" });
      setStatus("error");
      return;
    }

    try {
      const res = await api.post("/payments", {
        student_id: studentId,
        amount: parseFloat(amount),
        reference
      });
      setResult(res.data);
      setStatus("success");
      setStudentId("");
      setAmount("");
      setReference("");
    } catch (err) {
      setResult(err.response?.data || { error: "Something went wrong" });
      setStatus("error");
    }
  };

  return (
    <div>
      <h2>Make Payment</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Student:
          <select value={studentId} onChange={e => setStudentId(e.target.value)}>
            <option value="">Select Student</option>
            {students.length === 0 ? (
              <option disabled>Loading students...</option>
            ) : (
              students.map(s => (
                <option key={s.id} value={s.id}>{s.name}</option>
              ))
            )}
          </select>
        </label>
        <br />
        <label>
          Amount:
          <input type="number" value={amount} onChange={e => setAmount(e.target.value)} />
        </label>
        <br />
        <label>
          Reference:
          <input type="text" value={reference} onChange={e => setReference(e.target.value)} />
        </label>
        <br />
        <button type="submit">Pay</button>
      </form>

      {result && (
        <div style={{ marginTop: "20px", color: status === "success" ? "green" : "red" }}>
          {status === "success" ? "Payment successful:" : "Error:"}
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}