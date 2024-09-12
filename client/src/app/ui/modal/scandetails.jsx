"use client"


import Modal from "@/app/ui/modal/modal";


export default function ScanDetails({isOpen, onClose}) {

  return (
    <div className="container">
      <Modal isOpen={open} onClose={() => setOpen(false)}/>
    </div>
  );
}
