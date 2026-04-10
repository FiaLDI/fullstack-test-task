import type { Metadata } from "next";
import 'bootstrap/dist/css/bootstrap.min.css';
import { UiPack } from "../shared";

export async function generateMetadata(): Promise<Metadata> {
  return {
    title: 'Тестовое задание Fullstack',
    description: 'Тестовое задание Fullstack',
  };
}

export default async function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='ru'>
      <head>
        <link rel="icon" href="/public/favicon.ico" sizes="any" />
      </head>
      <body>
        <UiPack.Container fluid className='p-0'>
            {children}
        </UiPack.Container>
      </body>
    </html>
  );
}
