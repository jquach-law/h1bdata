import axios from "axios";
import { useRouter } from "next/router";
import React, { useState } from "react";
import { useQuery } from "react-query";
import { useDispatch } from "react-redux";
import Layout from "../components/layout";
import { SAVE_SEARCH } from "../state/slices/searchSlice";
import utilStyles from "../styles/utils.module.css";

export default function Home() {
  const router = useRouter();
  const [employer, setEmployer] = useState("");
  const [jobTitle, setJobTitle] = useState("");
  const [employerCity, setEmployerCity] = useState("");
  const dispatch = useDispatch();

  const { refetch: refetchSearchResults } = useQuery(
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
      onSuccess: (data) => dispatch(SAVE_SEARCH(data)),
    }
  );

  return (
    <Layout home>
      <section className={utilStyles.indexMaxWidth}>
        <div className="flex">
          <h1 className="title">H1B Data Salary Search</h1>
          <div>
            <form
              onSubmit={(event) => {
                event.preventDefault();
                refetchSearchResults().then(() => router.push("/results"));
              }}
            >
              <fieldset className="flex three">
                <div className="field">
                  <label className="label">Employer</label>
                  <input
                    className="input"
                    type="text"
                    placeholder="Employer"
                    onChange={(event) => setEmployer(event.target.value)}
                  />
                </div>
                <div className="field">
                  <label className="label">Job</label>
                  <input
                    className="input"
                    type="text"
                    placeholder="Job"
                    onChange={(event) => setJobTitle(event.target.value)}
                  />
                </div>
                <div className="field">
                  <label className="label">City</label>
                  <input
                    className="input"
                    type="text"
                    placeholder="City"
                    onChange={(event) => setEmployerCity(event.target.value)}
                  />
                </div>
                <div className="field">
                  <button className="button" type="submit">
                    Search
                  </button>
                </div>
              </fieldset>
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
