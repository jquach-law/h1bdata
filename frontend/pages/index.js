import axios from "axios";
import Head from "next/head";
import Link from "next/link";
import React, { useEffect, useState } from "react";
import { useQuery } from "react-query";
import { useDispatch } from "react-redux";
import Layout, { siteTitle } from "../components/layout";
import { saveSearch } from "../state/slices/searchSlice";
import utilStyles from "../styles/utils.module.css";

export default function Home() {
  const [employer, setEmployer] = useState("");
  const [jobTitle, setJobTitle] = useState("");
  const [employerCity, setEmployerCity] = useState("");

  const {
    isLoading,
    error,
    data,
    refetch: refetchSearchResults,
  } = useQuery(
    ["searchResults", employer, jobTitle, employerCity],
    () =>
      axios
        .get(
          `https://h1bdata-api.herokuapp.com/search?employer=${employer}&job_title=${jobTitle}&city=${employerCity}`
        )
        .then((res) => res.data),
    {
      refetchOnWindowFocus: false,
      enabled: false,
    }
  );
  const dispatch = useDispatch();

  if (data) {
    dispatch(saveSearch(data));
  }

  useEffect(() => {
    console.log(employer, jobTitle, employerCity);
  }, []);

  return (
    <Layout home>
      <Head>
        <title>{siteTitle}</title>
      </Head>

      <section className={utilStyles.headingMd}>
        <div className="flex">
          <h1>H1B Data Salary Search</h1>
          <div>
            <form>
              <fieldset className="flex three">
                <label>
                  <input
                    type="text"
                    placeholder="Employer"
                    onChange={(event) => setEmployer(event.target.value)}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="Job Title"
                    onChange={(event) => setJobTitle(event.target.value)}
                  />
                </label>
                <label>
                  <input
                    type="text"
                    placeholder="City"
                    onChange={(event) => setEmployerCity(event.target.value)}
                  />
                </label>
              </fieldset>
              <Link href="/results">
                <button type="button" onClick={() => refetchSearchResults()}>
                  Search
                </button>
              </Link>
            </form>
          </div>
          {/* TODO: Get available years from the database? */}
          {/* <select>
            <option>2022</option>
            <option>2021</option>
          </select> */}
        </div>
      </section>
    </Layout>
  );
}
