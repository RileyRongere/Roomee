import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './Pages/Home'
import Dummy from './Pages/Dummy'
import Quiz from './Pages/Quiz'
import Match from './Pages/Match'

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dummy" element={<Dummy />} />
        <Route path="/quiz" element={<Quiz />} />
        <Route path="/match" element={<Match />} />
      </Routes>
    </>
  );
};

export default App;
