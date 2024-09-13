'use client'

import Modal from "@/app/ui/modal/modal";
import {useState} from "react";
import Button from "@/app/ui/button";
import Form from "@/app/ui/card/create-form"; 


export default function NewScan ({tools, onClick}) {
  const [open, setOpen] = useState(false);
  return (
    <>
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
        <Form 
          onClose={() => setOpen(false)}
          tools={tools}
        />
      </Modal>
    </>
  );
}
