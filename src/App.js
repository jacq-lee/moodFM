import './App.css';
import {Route, Routes} from "react-router-dom";
import FirstLogin from "./pages/FirstLogin";
import SecondLogin from "./pages/SecondLogin";
import Home from "./pages/Home";
import HomePressed from "./pages/HomePressed";
import Insights from "./pages/Insights";
import Profile from "./pages/Profile";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<FirstLogin></FirstLogin>}></Route>
        <Route path="/login" element={<SecondLogin></SecondLogin>}></Route>
        <Route path="/read-room" element={<Home></Home>}></Route>
        <Route path="/home" element={<HomePressed></HomePressed>}></Route>
        <Route path="/insights" element={<Insights></Insights>}></Route>
        <Route path="/profile" element={<Profile></Profile>}></Route>
      </Routes>
    </div>
  );
}

export default App;
