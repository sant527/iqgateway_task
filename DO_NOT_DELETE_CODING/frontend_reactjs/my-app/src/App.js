import React, { useState } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";
import axios from "axios";

const baseURL = `http://${window.location.hostname}:8028`;

const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 5000,
  headers: {
    Authorization: localStorage.getItem("access_token")
      ? "Bearer " + localStorage.getItem("access_token")
      : null,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

const access_token = localStorage.getItem("access_token");

// This site has 3 pages, all of which are rendered
// dynamically in the browser (not server rendered).
//
// Although the page does not ever refresh, notice how
// React Router keeps the URL up to date as you navigate
// through the site. This preserves the browser history,
// making sure things like the back button and bookmarks
// work properly.

export default function BasicExample() {
  const signOut = (e) => {
    e.preventDefault();
    localStorage.removeItem("access_token");
    localStorage.removeItem("username");
    window.location.assign("/login");
  };

  return (
    <Router>
      <div>
        {access_token != null ? (
          <ul>
            <li>USER: {localStorage.getItem("username")}</li>
            <li>
              <a href="/#" onClick={signOut}>
                Logout
              </a>
            </li>
          </ul>
        ) : null}

        <hr />

        {/*
          A <Switch> looks through all its children <Route>
          elements and renders the first one whose path
          matches the current URL. Use a <Switch> any time
          you have multiple routes, but you want only one
          of them to render at a time
        */}
        {access_token == null ? (
          <Switch>
            <Route path="/login" component={Login} />
            <Redirect strict from="/" to="/login" />
          </Switch>
        ) : (
          <Switch>
            <Route path="/" component={Dashboard} />
          </Switch>
        )}
      </div>
    </Router>
  );
}

// You can think of these components as "pages"
// in your app.

function Login() {
  const [username, setUsername] = useState("");
  const [password, setpassword] = useState("");

  const onChangeUsername = (event) => {
    setUsername(event.target.value);
  };

  const onChangePassword = (event) => {
    setpassword(event.target.value);
  };

  function handleSubmit(event) {
    event.preventDefault();
    authLogin(username, password)
      .then((res) => {
        console.log(JSON.stringify(res, null, 2));
        localStorage.setItem("username", username);
        localStorage.setItem("access_token", res.data.key);
        window.location.assign("/dashboard");
      })
      .catch((err) => {
        console.log(err);
        alert("failed");
      });
  }

  function authLogin(username, password) {
    //dont forget to add slash at the end when we call POST method
    const url = "dj-rest-auth/login/";
    const data = {
      username: username,
      password: password,
    };
    const auth = {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    };
    const promise = axiosInstance.post(url, data, auth);
    return promise;
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Login:
            <input type="text" value={username} onChange={onChangeUsername} />
          </label>
        </div>
        <div>
          <label>
            Password:
            <input type="text" value={password} onChange={onChangePassword} />
          </label>
        </div>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

function Dashboard() {
  const [dataurl, setDataurl] = useState("");
  const [dbname, setDbName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setpassword] = useState("");
  const [date_updated, setDateUpdated] = useState("");
  const [csv_link, setCsvLink] = useState("");

  const onChangeUsername = (event) => {
    setUsername(event.target.value);
  };

  const onChangePassword = (event) => {
    setpassword(event.target.value);
  };

  function onChangeDataurl(event) {
    setDataurl(event.target.value);
  }

  function onChangeDbName(event) {
    setDbName(event.target.value);
  }

  function handleSubmit(event) {
    event.preventDefault();
    getDataFromDatabase(dataurl, dbname, username, password)
      .then((res) => {
        console.log(JSON.stringify(res, null, 2));
        alert("successful");
      })
      .catch((err) => {
        console.log(err);
        alert(err.response.data.detail);
      });
  }

  function getDataFromDatabase(dataurl, dbname, username, password) {
    const url = "get_data/";
    const data = {
      dataurl: dataurl,
      dbname: dbname,
      username: username,
      password: password,
    };
    const auth = {
      headers: {
        Authorization: "Token " + localStorage.getItem("access_token"),
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    };
    const promise = axiosInstance.post(url, data, auth);
    return promise;
  }

  function getRecentFile() {
    const url = "get_recent_file/";
    const auth = {
      headers: {
        Authorization: "Token " + localStorage.getItem("access_token"),
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    };
    const promise = axiosInstance.get(url, auth);
    promise
      .then((res) => {
        console.log(JSON.stringify(res, null, 2));
        setCsvLink(res.data.data_file_name_url);
        setDateUpdated(res.data.updated_at);
      })
      .catch((err) => {
        console.log(err);
        alert(err.response.data.detail);
      });
  }

  return (
    <>
      <div>
        <h2>Get Data</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>
              Database Host:
              <input type="text" value={dataurl} onChange={onChangeDataurl} />
            </label>
          </div>
          <div>
            <label>
              Database Name:
              <input type="text" value={dbname} onChange={onChangeDbName} />
            </label>
          </div>
          <div>
            <label>
              username:
              <input type="text" value={username} onChange={onChangeUsername} />
            </label>
          </div>
          <div>
            <label>
              password:
              <input type="text" value={password} onChange={onChangePassword} />
            </label>
          </div>
          <input type="submit" value="Submit" />
        </form>
      </div>
      <div>
        <h2>Recent Csv File</h2>
        <button onClick={getRecentFile}> Get recent File</button>
        <ul>
          <li>Updated_at :: {date_updated}</li>
          <li>
            Csv File ::{" "}
            <a target="_blank" href={csv_link} rel="noreferrer">
              {csv_link}
            </a>
          </li>
        </ul>
      </div>
    </>
  );
}
