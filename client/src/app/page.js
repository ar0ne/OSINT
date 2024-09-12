import styles from "./page.module.css";
import Table from "@/app/ui/card/table";
import { fetchScanPage } from "@/app/lib/data";
import NewScan from "@/app/ui/card/new-scan";

export default async function Home({searchParams}) {
  const page = searchParams["page"] || 1;
  const paginatedScans = await fetchScanPage(+page);

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <NewScan  />
        <Table scans={paginatedScans}/>
      </main>
      <footer className={styles.footer}>
      </footer>
    </div>
  );
}
