import styles from "./page.module.css";
import CardBoard from "@/app/ui/card/board";
import { fetchScanPage } from "@/app/lib/data";
import NewScanButton from "@/app/ui/buttons/newscan";

export default async function Home({searchParams}) {
  const page = searchParams["page"] || 1;
  const paginatedScans = await fetchScanPage(+page);

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <NewScanButton  />
        <CardBoard scans={paginatedScans}/>
      </main>
      <footer className={styles.footer}>
      </footer>
    </div>
  );
}
