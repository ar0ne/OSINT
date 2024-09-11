'use client'

import styles from "@/app/ui/card/card.module.css";
import { generatePagination } from "@/app/lib/utils";

export default function Pagination ({totalPages, currentPage, onClick}) {
  if (!totalPages) return;

  const pagination = generatePagination(currentPage, totalPages);

  const handleOnClick = (page, idx) => {
    if (currentPage !== page){
      if (page === "...") {
        page = Math.floor((pagination[idx - 1] + pagination[idx + 1] ) / 2);
      }
      onClick(page);
    }
  }

  return (
    <div className={styles.pagination}>
      {pagination.map((page, idx) =>  
        <button
          key={idx}
          className={`${styles.button} ${page === currentPage ? styles.currentbutton : ''} `}
          onClick={() => handleOnClick(page, idx)}
          >
        {page}
        </button>
      )}
    </div>
  );
}
