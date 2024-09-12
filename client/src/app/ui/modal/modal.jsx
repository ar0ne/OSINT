"use client"

import { createPortal } from 'react-dom';
import styles from "@/app/ui/modal/modal.module.css";

const Modal = ({children, isOpen, onClose, title, ...props}) => {
  
  if (!isOpen) return;

  return createPortal(
    <div className={styles.overlay}>
      <div className={styles.modal}>
        <h2>{title}</h2>
        <button 
          className={styles.close}
          onClick={onClose}
          >Close</button>
          {children && <div>{children}</div>}
      </div>
    </div>,
    document.body
  );
}

export default Modal;
