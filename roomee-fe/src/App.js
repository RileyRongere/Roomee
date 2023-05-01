import './App.css';
import { Routes, Route } from 'react-router-dom';
import Home from './Pages/Home'
import Dummy from './Pages/Dummy'
import Quiz from './Pages/Quiz'
import Username from './Pages/Username'
import Password from './Pages/Password'

export function App() {
  return (
    <>
      <nav>
        <ul>
          <li><Link to="/quiz">Edit Answers</Link></li>
          <li><Link to="/username">Logout</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/dummy" element={<Dummy />} />
        <Route path="/quiz" element={<Quiz />} />
        <Route path="/" element={<Username />} />
        <Route path="/password" element={<Password />} />
        <Route path="/match" element={<Match />} />
      </Routes>
    </>
  );
};

export default App;
