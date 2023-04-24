import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './Pages/Home'
import Dummy from './Pages/Dummy'
import Quiz from './Pages/Quiz'

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dummy" element={<Dummy />} />
        <Route path="/quiz" element={<Quiz />} />
      </Routes>
    </>
  );
};

export default App;
