'use client'
import styles from "@/app/ui/card/card.module.css";
import {useState} from "react";
import Card from "@/app/ui/card/card";

const CardBoard = ({items}) => {
  if (!items) return;

  const [page, setPage] = useState(1);

  return (
    <div className={styles.cardboard}>
      <h1>Previous scans</h1>
      <p className={styles.title}>- - - - </p>
      <div className={styles.cards}>
        {items.map((i) => 
          <Card 
            key={i.id} 
            {...i} 
          />
        )}
      </div>
      <div className={styles.controls}>
        <button className={`${styles.currentbutton} ${styles.button}`}>1</button>
        <button className={styles.button}>2</button>
        <button className={styles.button}>3</button>
      </div>
    </div>
  )
};

export default CardBoard;
