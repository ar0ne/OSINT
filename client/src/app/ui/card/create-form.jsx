"use client"

import { createScan } from "@/app/lib/actions";

export default function Form() {
  
  return (
    <form action={createScan}>

      <Button type="submit">Create Invoice</Button>
    </form>
  );
}
