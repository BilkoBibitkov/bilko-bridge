export default function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center p-4">
      <div className="text-center max-w-lg mx-auto">
        <h1 className="text-5xl md:text-6xl font-extrabold mb-6">
          Hello, Bilkobibitkov.dev!
        </h1>
        <h2 className="text-3xl md:text-4xl font-bold mb-4">
          Welcome to Your Digital Inventory
        </h2>
        <p className="text-xl md:text-2xl mb-8 opacity-90">
          This is where you can manage and keep track of all your digital assets. Built with Next.js and Tailwind CSS, this application is designed to be fast, resilient, and easy to use.
        </p>
        <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50">
          Start Building
        </button>
      </div>
    </div>
  );
}
