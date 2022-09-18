import './App.css';
import Landing from "./Landing";
import Home from "./Home";
import Insights from "./Insights";
import Profile from "./Profile";
import {Routes, Route} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Landing></Landing>} />
        <Route path="/home" element={<Home></Home>} />
        <Route path="/insights" element={<Insights></Insights>} />
        <Route path="/profile" element={<Profile></Profile>} />
      </Routes>
    </div>
  );
}

export default App;
