import { useSelector } from "react-redux";
import Layout from "../components/layout";
import { selectSearchResults } from "../state/slices/searchSlice";

export default function Results() {
  const searchResults = useSelector(selectSearchResults);

  return (
    <>
      <Layout>
        <section>
          <div className="table-container">
            <table className="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
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
