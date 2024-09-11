import Image from "next/image";
import styles from "./page.module.css";
import { fetchScanData } from "@/app/lib/data";
import CardBoard from "@/app/ui/card/board";

export default async function Home() {
  const scans = await fetchScanData();
  const items = scans.items;
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <CardBoard items={items} />
      </main>
      <footer className={styles.footer}>
      </footer>
    </div>
  );
}
