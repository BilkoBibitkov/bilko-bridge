import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-bulgarian-flag">
      <div className="z-10 w-full max-w-5xl items-center justify-center font-mono text-sm lg:flex">
        <h1 className="text-6xl font-bold text-white text-center drop-shadow-lg">
          Bilko lives!
        </h1>
      </div>
    </main>
  );
}
