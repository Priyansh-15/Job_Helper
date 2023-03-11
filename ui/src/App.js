import Homepage from './pages/Homepage';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import './App.css';
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="App">
    <Navbar/>
    <Router>
      <Routes>
        <Route exact path="/" element={<Homepage/>}/>
      
      </Routes>
    </Router>
    </div>
  );
}

export default App;
