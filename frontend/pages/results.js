import Head from "next/head";
import { useSelector } from "react-redux";
import Layout from "../components/layout";
import { selectSearchResults } from "../state/slices/searchSlice";

export default function Results() {
  const searchResults = useSelector(selectSearchResults);
  console.log(searchResults);

  return (
    <>
      <Layout>
        <Head>
          <title>First Post</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>
      </Layout>
    </>
  );
}
