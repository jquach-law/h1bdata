import Head from "next/head";
import { useSelector } from "react-redux";
import Layout from "../components/layout";
import { selectSearchResults } from "../state/slices/searchSlice";

export default function Results() {
  const searchResults = useSelector(selectSearchResults);

  return (
    <>
      <Layout>
        <Head>
          <title>First Post</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>
      </Layout>

      <table>
        <thead>
          {Object.keys(searchResults[0]).map((colName) => (
            <th>{colName}</th>
          ))}
        </thead>
        <tbody>
          {searchResults.map((row) => {
            return (
              <tr>
                {Object.keys(searchResults[0]).map((colName) => (
                  <td>{row[colName]}</td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
    </>
  );
}
