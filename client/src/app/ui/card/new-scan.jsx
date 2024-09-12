'use client'

import Modal from "@/app/ui/modal/modal";
import {useState} from "react";
import Button from "@/app/ui/button";


export default function NewScan ({onClick}) {

  const [open, setOpen] = useState(false);

  return (
    <div>
      <Button 
        onClick={() => setOpen(true)}
        >
        New scan
      </Button>
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
