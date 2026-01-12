import type { Metadata } from "next";
import { Cormorant_Garamond, DM_Sans } from "next/font/google";
import "./globals.css";

// Display Font - Humanist Serif for headings
const cormorantGaramond = Cormorant_Garamond({
  weight: ["300", "400", "500", "600", "700"],
  subsets: ["latin"],
  variable: "--font-display",
  display: "swap",
});

// Body Font - Geometric Sans for data/body
const dmSans = DM_Sans({
  weight: ["400", "500", "600", "700"],
  subsets: ["latin"],
  variable: "--font-body",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Harmonia - The Apex Match System",
  description: "A scientific approach to meaningful connection. Tri-factor algorithmic matching based on Visual Preference, Psychological Resonance, and Biological Compatibility.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${dmSans.variable} ${cormorantGaramond.variable} antialiased bg-parchment-texture`}
      >
        {children}
      </body>
    </html>
  );
}
