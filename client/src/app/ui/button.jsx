"use client"


export default function Button ({children, className, ...otherProps}) {

  return (
    <button
      {...otherProps}
      className={className}
      >
      {children}
    </button>
  );
}
