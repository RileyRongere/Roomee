import { Link } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { getUserExists, submitPassword } from "../api_calls/api";
import { useState } from "react";
// need to get username form the other page - how pass?

function searchPassword() {
  fetch("api_name");
  // if

  // else

  // Conditional statment that sends password and either calls next page or throws an error message
}

// we need to change heading to a conditional bassed on if the username is found or not

// function componentDidMount() {
//   console.log(this.props.location.state.username);
// }
// <div className="Password">
//   <head>
//     <h2> Enter Password Here </h2>
//     <form id="password" onSubmit="searchPassword()">
//       <input
//         type="text"
//         id="password"
//         name="password"
//         placeholder="password"
//         size="15"
//       >
//       </input>
//       <button class="button">Submit</button>
//     </form>
//   </head>
// </div>

const Password = (props) => {
  const [password, setPassword] = useState("");

  const { state } = useLocation();
  console.log(state.name["userName"]);

  const submittedUser = state.name["userName"];

  const handleSubmit = (event) => {
    event.preventDefault();
    setPassword("");
    console.log(password);

    // if(getUserExists(submittedUser)){
    //   //userLogin(submittedUser, password)
    // }else{
    //   //userRegister(submittedUser, password)
    // }
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
      </form>
    </div>
  );
};
export default Password;
