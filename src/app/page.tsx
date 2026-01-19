import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <h1 className="text-6xl font-bold text-center w-full my-8">
          BILKO BIBITKOV LIVES
        </h1>
      </div>

      <div className="relative flex place-items-center before:absolute before:h-[300px] before:w-full before:-translate-x-1/2 before:rounded-full before:bg-gradient-radial before:from-white before:to-transparent before:blur-2xl before:content-[''] after:absolute after:-z-20 after:h-[180px] after:w-full after:translate-x-1/3 after:bg-gradient-conic after:from-sky-200 after:via-blue-200 after:blur-2xl after:content-[''] before:dark:bg-gradient-to-br before:dark:from-transparent before:dark:to-blue-700 before:dark:opacity-10 after:dark:from-sky-900 after:dark:via-[#0141ff] after:dark:opacity-40 sm:before:w-[480px] sm:after:w-[240px] before:lg:h-[360px]">
        {/* Placeholder for future image or content */}
      </div>

      <section className="mt-16 w-full max-w-5xl text-center">
        <h2 className="text-4xl font-semibold mb-8">Heritage: 5 Fascinating Facts About Bulgaria</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 text-left">
          <div className="p-6 border border-gray-700 rounded-lg shadow-md bg-gray-800">
            <h3 className="text-xl font-bold mb-2">1. The Cyrillic Alphabet</h3>
            <p className="text-gray-300">
              The Cyrillic alphabet, used by over 250 million people in Eastern Europe and Asia, was developed in the First Bulgarian Empire in the 9th century. It was created by the disciples of Saints Cyril and Methodius.
            </p>
          </div>
          <div className="p-6 border border-gray-700 rounded-lg shadow-md bg-gray-800">
            <h3 className="text-xl font-bold mb-2">2. Establishment in 681 AD</h3>
            <p className="text-gray-300">
              Bulgaria is one of the oldest European countries and the only one that hasn't changed its name since its establishment in 681 AD. It was founded by Khan Asparuh.
            </p>
          </div>
          <div className="p-6 border border-gray-700 rounded-lg shadow-md bg-gray-800">
            <h3 className="text-xl font-bold mb-2">3. Rose Oil Production</h3>
            <p className="text-gray-300">
              Bulgaria is the world's largest producer of rose oil, an essential ingredient in perfumes and cosmetics. The Kazanlak Rose Valley is famous for its vast fields of oil-bearing roses.
            </p>
          </div>
          <div className="p-6 border border-gray-700 rounded-lg shadow-md bg-gray-800">
            <h3 className="text-xl font-bold mb-2">4. Ancient Thracian Gold</h3>
            <p className="text-gray-300">
              Bulgaria boasts a rich Thracian heritage, with numerous archaeological sites and some of the world's oldest and most exquisite gold treasures, dating back thousands of years.
            </p>
          </div>
          <div className="p-6 border border-gray-700 rounded-lg shadow-md bg-gray-800">
            <h3 className="text-xl font-bold mb-2">5. Origin of Bulgarian Yogurt</h3>
            <p className="text-gray-300">
              The unique Lactobacillus bulgaricus bacterium, responsible for the distinct taste and health benefits of Bulgarian yogurt, was named after the country where it was discovered and widely used.
            </p>
          </div>
        </div>
      </section>

      <div className="mb-32 grid text-center lg:mb-0 lg:w-full lg:max-w-5xl lg:grid-cols-4 lg:text-left">
        {/* Existing links/cards if any, or remove if not needed */}
      </div>
    </main>
  );
}
