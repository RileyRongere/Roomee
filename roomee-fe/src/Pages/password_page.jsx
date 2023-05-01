import { Link } from "react-router-dom";
// this may or may not get the info we need from the username page 
import { userTrueFalse } from "username_page"
import { Username } from "username_page"



// we think that passes stuff we don't know 
// function searchPassword() {
//   fetch('api_name')
// if

// else

// Conditional statment that sends password and either calls next page or throws an error message 

// we need to change heading to a conditional bassed on if the username is found or not 

function Heading({ userTrueFalse }) {
    if (userTrueFalse) {
        return <h2> Enter Password </h2>;
    }
    return <h2> Create Password </h2>;
}


function componentDidMount() {
    console.log(this.props.location.state.username);
}

const Password = () => {
    return (
        <div className="Password">
            <head>
                <Heading userTrueFalse={True} />
                <form id="password" onSubmit="searchPassword()">
                    <input type="text" id="password" name="password" placeholder="password" size="15"> </input>
                    <button class="button">Submit</button>
                </form>
            </head>
        </div>

    );
}
export default Password;