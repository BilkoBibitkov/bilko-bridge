import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Bilko Bibitkov Lives!',
  description: 'A Tribute to Bulgarian Heritage',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
