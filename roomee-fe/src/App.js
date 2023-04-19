import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './Pages/Home'
import Dummy from './Pages/Dummy'

const App = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dummy" element={<Dummy />} />
      </Routes>
    </>
  );
};

export default App;
