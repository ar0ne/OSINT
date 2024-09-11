'use client'


import styles from "@/app/ui/card/card.module.css";
import {useState} from "react";
import Card from "@/app/ui/card/card";
import Pagination from "@/app/ui/card/pagination";


const CardBoard = ({scans}) => {

  //const [page, setPage] = useState(1);


  const getCards = (scans) => {
    if (!scans) return (<h1>...</h1>);
    return (
      <div className={styles.cards}>
        {scans.items.map((i) => 
          <Card 
            key={i.id} 
            {...i}
            onClick={console.log}
          />
        )}
      </div>
    );
  };

  const cards = getCards(scans);

  return (
    <div className={styles.cardboard}>
      <h1>Previous scans</h1>
      <p className={styles.title}>- - - - </p>
      {cards}
      <Pagination
        totalPages={3}
        currentPage={1}
        onClick={console.log}
      />
    </div>
  )
};

export default CardBoard;
