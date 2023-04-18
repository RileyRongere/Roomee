import logo from '../logo.svg';

const Dummy = () => {
    return (
        <div className="Dummy">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    This is a dummy second route
        </p>
                <a href="/">
                    Go to Home
                </a>
            </header>
        </div>
    );
}
export default Dummy;