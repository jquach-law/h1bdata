import Head from "next/head";
import { useSelector } from "react-redux";
import Layout, { siteTitle } from "../components/layout";
import { selectSearchResults } from "../state/slices/searchSlice";

export default function Results() {
  const searchResults = useSelector(selectSearchResults);

  return (
    <>
      <Layout>
        <Head>
          <title>{siteTitle}</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>

        <section>
          <div>
            <table className="primary">
              <thead>
                {searchResults.length > 0 &&
                  Object.keys(searchResults[0]).map((colName) => (
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
          </div>
        </section>
      </Layout>
    </>
  );
}
