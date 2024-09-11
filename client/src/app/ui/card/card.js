'use client'
import styles from "@/app/ui/card/card.module.css";

export default function Card ({status, domain, tool, created_at}) {
  if (!status) return;

  return (
    <div className={styles.card}>
      <div className={styles.row}>
        <div className={styles.column}>
          Status: 
        </div>
        <div className={styles.column}>
          {status}
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
          {tool}
        </div>
      </div>
      <div className={styles.row}>
        <div className={styles.column}>
          Date: 
        </div>
        <div className={styles.column}>
          {created_at}
        </div>
      </div> 
    </div>
  );
}
