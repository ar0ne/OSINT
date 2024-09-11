import styles from "./page.module.css";
import CardBoard from "@/app/ui/card/board";
import { fetchScanData } from "@/app/lib/data";
import NewScanButton from "@/app/ui/buttons/newscan";

export default async function Home({searchParams}) {
  const page = searchParams["page"] || 1;
  const scans = await fetchScanData(+page);

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <NewScanButton  />
        <CardBoard scans={scans}/>
      </main>
      <footer className={styles.footer}>
      </footer>
    </div>
  );
}
