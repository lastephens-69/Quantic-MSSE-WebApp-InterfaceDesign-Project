import { useEffect, useState } from "react";
import {
  getAdminSummary,
  getAdminCustomers,
  getAdminReservations,
} from "../services/api";

export default function Admin() {
  const [summary, setSummary] = useState(null);
  const [customers, setCustomers] = useState([]);
  const [reservations, setReservations] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    (async () => {
      try {
        const [sum, cust, resv] = await Promise.all([
          getAdminSummary(),
          getAdminCustomers(),
          getAdminReservations(),
        ]);
        setSummary(sum);
        setCustomers(cust);
        setReservations(resv);
      } catch (e) {
        setError(e.message);
      }
    })();
  }, []);

  return (
    <div className="container" style={{ padding: "2rem 1rem", maxWidth: 1100, margin: "0 auto" }}>
      <h1>Admin (read-only)</h1>
      {error && <div style={{ color: "crimson", marginBottom: 12 }}>Error: {error}</div>}

      {summary && (
        <div style={{ display: "flex", gap: 16, marginBottom: 24 }}>
          <Stat label="Customers" value={summary.customers} />
          <Stat label="Reservations" value={summary.reservations} />
        </div>
      )}

      <Section title="Latest Reservations">
        <Table cols={["id","Customer_id","time_slot","table_number","created_at"]} rows={reservations} />
      </Section>

      <Section title="Latest Customers">
        <Table cols={["id","name","email","phone","created_at"]} rows={customers} />
      </Section>
    </div>
  );
}

function Stat({ label, value }) {
  return (
    <div style={{ padding: 16, border: "1px solid #ddd", borderRadius: 12, minWidth: 180 }}>
      <div style={{ fontSize: 12, color: "#666" }}>{label}</div>
      <div style={{ fontSize: 28, fontWeight: 600 }}>{value}</div>
    </div>
  );
}

function Section({ title, children }) {
  return (
    <section style={{ marginBottom: 28 }}>
      <h2 style={{ margin: "12px 0 10px" }}>{title}</h2>
      {children}
    </section>
  );
}

function Table({ cols, rows }) {
  return (
    <div style={{ overflowX: "auto" }}>
      <table style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            {cols.map((c) => (
              <th key={c} style={{ textAlign: "left", padding: "8px 10px", borderBottom: "1px solid #ddd" }}>
                {c}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.id}>
              {cols.map((c) => (
                <td key={c} style={{ padding: "8px 10px", borderBottom: "1px solid #f0f0f0" }}>
                  {String(r[c] ?? "")}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      {!rows.length && <div style={{ color: "#777", padding: "10px 0" }}>No data.</div>}
    </div>
  );
}
