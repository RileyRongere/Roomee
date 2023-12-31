import React from "react";
import { callApi } from "../api_calls/api";
import { useState } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
// const handleClickSignIn = () => {
//   console.log("come handle click fun");
//   this.props.history.push({
//     pathname: "/password_page",
//     state: { username: "Steven" },
//   });
// }

function Username() {
  const [userName, setUserName] = useState("Username");

  const navigate = useNavigate();
  const handleSubmit = (event) => {
    event.preventDefault();
    setUserName("Username");
    console.log(userName);
  };

  return (
    <div className="container">
      <h1>Roomee</h1>
      <h2>Login</h2>
      <form id="username" onSubmit={handleSubmit}>
        <label>
          <input
            type="email"
            placeholder={userName}
            name="name"
            onChange={(event) => setUserName(event.target.value)}
          />
        </label>

        <button
          className="button"
          onClick={() => {
            navigate("/password", { state: { name: { userName } } });
          }}
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default Username;

// Log to console
// console.log('Username Entered')
