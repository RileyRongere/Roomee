import { Link } from "react-router-dom";


const Password = () => {
    return (
        <div className="Password">
            <head>
                <h2> Enter Password Here </h2>
                <form action="/action_page.php">
                    <input type="text" id="password" name="password" placeholder="password" size="15"> </input>
                </form>
                <form id="password" onSubmit="searchPassword()">
                    <button class="button">Submit</button>
                </form>
            </head>
        </div>

    );
}
export default Password;