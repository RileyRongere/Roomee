import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./Pages/Home";
import Dummy from "./Pages/Dummy";
import Quiz from "./Pages/Quiz";
import Match from "./Pages/Match";
import Username from "./Pages/Username";
import Password from "./Pages/password_page";

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dummy" element={<Dummy />} />
        <Route path="/quiz" element={<Quiz />} />
        <Route path="/match" element={<Match />} />
        <Route path="/username" element={<Username />} />
        <Route path="/password" element={<Password />} />
      </Routes>
    </>
  );
};

export default App;
