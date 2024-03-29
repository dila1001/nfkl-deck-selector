import TableGames, { GameMetadata } from "../components/TableGames";

export default function page() {
  const data: GameMetadata[] = [
    {
      title: "Foundation",
      author: "Isaac Asimov",
      year: 1951,
      reviews: {
        positive: 2223,
        negative: 259,
      },
    },
    {
      title: "Frankenstein",
      author: "Mary Shelley",
      year: 1818,
      reviews: {
        positive: 5677,
        negative: 1265,
      },
    },
    {
      title: "Solaris",
      author: "Stanislaw Lem",
      year: 1961,
      reviews: {
        positive: 3487,
        negative: 1845,
      },
    },
    {
      title: "Dune",
      author: "Frank Herbert",
      year: 1965,
      reviews: {
        positive: 8576,
        negative: 663,
      },
    },
    {
      title: "The Left Hand of Darkness",
      author: "Ursula K. Le Guin",
      year: 1969,
      reviews: {
        positive: 6631,
        negative: 993,
      },
    },
    {
      title: "A Scanner Darkly",
      author: "Philip K Dick",
      year: 1977,
      reviews: {
        positive: 8124,
        negative: 1847,
      },
    },
  ];
  return <TableGames data={data} />;
}
