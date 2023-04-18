import logo from '../logo.svg';
import { Link } from "react-router-dom";

const Dummy = () => {
    return (
        <div className="Dummy">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    This is a dummy second route
        </p>
                <Link to={"/"}>Go Home</Link>
            </header>
        </div>
    );
}
export default Dummy;