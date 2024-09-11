'use client'


import styles from "@/app/ui/card/card.module.css";
import {useState} from "react";
import { usePathname, useRouter, useSearchParams } from 'next/navigation';

import Card from "@/app/ui/card/card";
import Pagination from "@/app/ui/card/pagination";

const CardBoard = ({scans}) => {

  const { replace } = useRouter();
  const searchParams = useSearchParams();
  const pathname = usePathname();

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
        totalPages={scans.total / scans.count}
        currentPage={scans.page}
        onClick={(p) => replace(`${pathname}?page=${p}`)}
      />
    </div>
  )
};

export default CardBoard;
