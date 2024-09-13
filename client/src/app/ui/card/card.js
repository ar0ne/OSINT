'use client'


import styles from "@/app/ui/card/card.module.css";

export default function Card ({id, status, domain, tool, created_at, onClick}) {
  if (!status) return;

  return (
    <div className={styles.card} role="button" onClick={() => onClick(id)}>
      <div className={styles.row}>
        <div className={styles.column}>
          Status: 
        </div>
        <div className={styles.column}>
          <p className="bold">{status}</p>
        </div>
      </div>
      <div className={styles.row}>
        <div className={styles.column}>
          Domain: 
        </div>
        <div className={styles.column}>
          {domain}
        </div>
      </div>
      <div className={styles.row}>
        <div className={styles.column}>
          Tool: 
        </div>
        <div className={styles.column}>
          {tool?.name}
        </div>
      </div>
      <div className={styles.row}>
        <div className={styles.column}>
          Date: 
        </div>
        <div className={styles.column}>
          {created_at ? created_at : '--'}
        </div>
      </div> 
    </div>
  );
}
