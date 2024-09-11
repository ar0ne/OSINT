'use client'

import styles from "@/app/ui/card/card.module.css";

export default function Pagination ({totalPages, currentPage, onClick}) {
  if (!totalPages) return;

  const pageNumbers = Array.from({length: totalPages}, (x, i) => i);

  return (
    <div className={styles.pagination}>
      {pageNumbers.map((i) =>  
        <button
          key={i}
          className={`${styles.button} ${i + 1 === currentPage ? styles.currentbutton : ''} `}
          onClick={() => currentPage !== i + 1 ? onClick(i + 1) : undefined}
          >
        {i + 1}
        </button>
      )}
    </div>
  );
}
