import Homepage from './pages/Homepage';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import './App.css';
import Navbar from './components/Navbar';
import Choice from './pages/Choice';
import Loading from './pages/Loading';

function App() {
  return (
    <div className="App">
    <Navbar/>
    <Router>
      <Routes>
        <Route exact path="/" element={<Homepage/>}/>
        <Route exact path="/choice" element={<Choice/>}/>
        <Route exact path="/loading" element={<Loading/>}/>
      </Routes>
    </Router>
    </div>
  );
}

export default App;
