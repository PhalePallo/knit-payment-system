// src/components/Header.jsx
import React from "react";

export default function Header({ setPage }) {
  return (
    <header style={{ marginBottom: "20px" }}>
      <h1>Knit Payment System</h1>
      <nav>
        <button onClick={() => setPage("payment")} style={{ marginRight: "10px" }}>Make Payment</button>
        <button onClick={() => setPage("revenue")}>School Revenue</button>
      </nav>
    </header>
  );
}