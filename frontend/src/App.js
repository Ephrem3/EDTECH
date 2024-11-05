import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import {Login} from './components/Login';
import {Logout} from './components/Logout';
import {Home} from './components/Home';
import {Navigation} from './components/Navigation';


function App() {
  return 
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
      </Routes>
    </Router>
}

export default App;
