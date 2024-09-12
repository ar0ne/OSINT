"use client"


export default function CardDetails({id, status, data, domain, tool, created_at, updated_at}) {

  if (!id) return;

  return (
    <div>
      <p>ID: {id}</p>
      <p>Scan results: {status}</p>
      <p>Domain: {domain}</p>
      <p>Tool: {tool}</p>
      <p>Scan requested: {created_at}</p>
      <p>Scan competed: {updated_at}</p>
      <p>- - - - -</p>
      <p>{data}</p>
    </div>
  );
}
