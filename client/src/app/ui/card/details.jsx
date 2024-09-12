"use client"

import styles from "@/app/ui/card/card.module.css";

export default function CardDetails({id, status, data, domain, tool, created_at, updated_at}) {

  if (!id) return;

  const content = data ? JSON.stringify(JSON.parse(data), null, 4) : "";

  return (
    <div className={styles.scandetails}>
      <p>ID: {id}</p>
      <p>Scan results: {status}</p>
      <p>Domain: {domain}</p>
      <p>Tool: {tool}</p>
      <p>Scan requested: {created_at}</p>
      <p>Scan competed: {updated_at}</p>
      <p>- - - - -</p>
      <pre>{content}</pre>
    </div>
  );
}
