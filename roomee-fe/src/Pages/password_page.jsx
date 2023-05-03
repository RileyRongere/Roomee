import { Link } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import {
  callApi,
  getUserExists,
  submitPassword,
  userLogin,
  userRegister,
} from "../api_calls/api";
import { useState } from "react";

const Password = (props) => {
  const [password, setPassword] = useState("");

  const { state } = useLocation();

  const submittedUser = state.name["userName"];

  const handleSubmit = async (event) => {
    event.preventDefault();

    console.log("user promise");
    console.log(getUserExists(submittedUser));

    let checkUserResult = await getUserExists(submittedUser).then(
      (response) => response
    );

    if (checkUserResult == 204) {
      alert("User exists");
      let loginResult = await userLogin(submittedUser, password).then(
        (response) => response
      );
      let loginStatus = loginResult["message"];

      console.log(loginStatus);
      if (loginStatus === "Login successful.") {
        alert("Successful Login");
      } else {
        alert("Login was not successful");
      }
    } else {
      alert("Creating user");
      userRegister(submittedUser, password);
    }
    setPassword("");
  };

  return (
    <div className="Password">
      <h1>Password Page</h1>
      <form id="password" onSubmit={handleSubmit}>
        <input
          type="text"
          id="password"
          name="password"
          placeholder="password"
          onChange={(event) => setPassword(event.target.value)}
        ></input>
        <button className="button" onClick={handleSubmit}>
          Submit
        </button>
      </form>
      <Link to={"/username"}>user</Link>
    </div>
  );
};
export default Password;
