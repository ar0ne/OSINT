import localFont from "next/font/local";
import "./globals.css";

//const geistSans = localFont({
//  src: "./fonts/GeistVF.woff",
//  variable: "--font-geist-sans",
//  weight: "100 900",
//});
//const geistMono = localFont({
//  src: "./fonts/GeistMonoVF.woff",
//  variable: "--font-geist-mono",
//  weight: "100 900",
//});
//
//
const hackBold = localFont({
  src: "./fonts/Hack-Bold.woff",
  variable: "--font-hack-bold",
  weight: "100 900",
});

const hackRegular = localFont({
  src: "./fonts/Hack-Regular.woff",
  variable: "--font-hack",
  weight: "100 900",
});


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${hackRegular.variable} ${hackBold.variable}`}>
        {children}
      </body>
    </html>
  );
}
