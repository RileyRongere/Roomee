import { Link } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { callApi, getUserExists, submitPassword, userLogin, userRegister} from "../api_calls/api";
import { useState } from "react";
// need to get username form the other page - how pass?

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
    console.log(password);
    userLogin(submittedUser, password)
    
    // if(getUserExists(submittedUser)){
      // }else{
        //   userRegister(submittedUser, password)
        // }
    //setPassword("");
  };
  //console.log(getUserExists("user/kevindurant@gmail.com"))
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
      <button
          className="button"
          onClick={handleSubmit}
        >
          Submit
        </button>
      </form>
      <Link to = {"/username"}>user</Link>
    </div>
  );
};
export default Password;
