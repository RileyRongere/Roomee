import React from "react";
import { callApi } from "../api_calls/api";

const checkUser = async () => {
  return await callApi("users");
};

// we need to figure out how to hold if the user is true or not
// then pass that to the next page and change the contents bassed on that

// also pass the username on for search

function handleClickSignIn() {
  console.log("come handle click fun");
  this.props.history.push({
    pathname: "/password_page",
    state: { username: "Steven" },
  });
}

const Username = (props) => {
  return (
    <div className="container">
      <h1>Roomee</h1>
      <h2>Login</h2>
      <form id="username" onSubmit="checkUser()">
        <label>
          <input type="email" placeholder="Username" name="name" />
        </label>
        <button class="button">Submit</button>
      </form>
    </div>
  );
};

export default Username;

// Log to console
// console.log('Username Entered')
