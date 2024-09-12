'use client'

import Modal from "@/app/ui/modal/modal";
import {useState} from "react";


export default function NewScanButton ({onClick}) {

  const [open, setOpen] = useState(false);

  return (
    <div>
      <button 
        onClick={() => setOpen(true)}
        >
        New scan
      </button>
      <Modal 
        isOpen={open} 
        onClose={() => setOpen(false)}
        title="New Scan"
      >
        <p>Hello long text as child</p>
      </Modal>
    </div>
  );
}
