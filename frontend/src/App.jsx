// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MakePayment from "./pages/MakePayment.jsx";
import SchoolRevenue from "./pages/SchoolRevenue.jsx";
import "./index.css";  // <-- import your CSS here

export default function App() {
  return (
    <Router>
      <div>
        <header style={{ padding: "20px", background: "#fff", borderBottom: "1px solid #ccc" }}>
          <h1>Knit Payment System</h1>
          <nav>
            <Link style={{ marginRight: "15px" }} to="/">Make Payment</Link>
            <Link to="/revenue">School Revenue</Link>
          </nav>
        </header>

        <main style={{ padding: "20px" }}>
          <Routes>
            <Route path="/" element={<MakePayment />} />
            <Route path="/revenue" element={<SchoolRevenue />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}