import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Bilkobibitkov",
  description: "The resilient digital inventory.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-slate-100 antialiased">
        {children}
      </body>
    </html>
  );
}
