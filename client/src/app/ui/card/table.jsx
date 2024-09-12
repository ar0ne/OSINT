'use client'


import styles from "@/app/ui/card/card.module.css";
import { useState, useEffect } from "react";
import { usePathname, useRouter, useSearchParams } from 'next/navigation';
import { fetchScanData } from "@/app/lib/data";

import Card from "@/app/ui/card/card";
import CardDetails from "@/app/ui/card/details";
import Pagination from "@/app/ui/card/pagination";
import Modal from "@/app/ui/modal/modal";


const Table = ({scans}) => {
  const { replace } = useRouter();
  const router = useRouter();
  const searchParams = useSearchParams();
  const pathname = usePathname();
  const [card, setCard] = useState(null);
  const [scanId, setScanId] = useState(null);

  useEffect(() => {
    let ignore = false;
    setCard(null);
    if (!scanId) return;
    fetchScanData(scanId).then(res => {
      if (!ignore) {
        setCard(res);
      }
    });
    return () => {
      ignore = true;
    }
  }, [scanId]);

  const getCards = (scans) => {
    if (!scans) return (<h1>...</h1>);
    return (
      <div className={styles.cards}>
        {scans.items.map((i) => 
          <Card 
            key={i.id} 
            {...i}
            onClick={() => setScanId(i.id)}
          />
        )}
      </div>
    );
  };

  const onCloseModal = () => {
    setScanId(null);
    router.refresh(); 
  }

  const cards = getCards(scans);
  const totalPages = scans ? Math.floor(scans.total / scans.count) : 0;
  const currentPage = scans ? scans.page : 1

  return (
    <div className={styles.table}>
      <h1>Previous scans</h1>
      <p className={styles.title}>- - - - </p>
      {cards}
      {card && <Modal
        isOpen={true} 
        onClose={onCloseModal}
        title="Scan results"
        >
          <CardDetails {...card} />
        </Modal>}
      <Pagination
        totalPages={totalPages}
        currentPage={currentPage}
        onClick={(p) => replace(`${pathname}?page=${p}`)}
      />
    </div>
  )
};

export default Table;
