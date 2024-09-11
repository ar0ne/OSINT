'use client'

import styles from "@/app/ui/buttons/buttons.module.css";


export default function NewScanButton ({onClick}) {
  return (
    <button
      className={styles.button}
      onClick={onClick}
    >New Scan
    </button>
  );
}
