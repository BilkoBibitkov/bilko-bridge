export default function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center p-4">
      <div className="text-center max-w-lg mx-auto">
        <h1 className="text-5xl md:text-6xl font-extrabold mb-6">
          Hello, Bilkobibitkov.dev!
        </h1>
        <p className="text-xl md:text-2xl mb-8 opacity-90">
          Your resilient foundation is ready for takeoff.
        </p>
        <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-8 rounded-full shadow-lg transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-blue-500 focus:ring-opacity-50">
          Start Building
        </button>
      </div>
    </div>
  );
}
