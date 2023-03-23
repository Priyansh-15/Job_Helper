import Homepage from './pages/Homepage';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import './App.css';

import Choice from './pages/Choice';
import Loading from './pages/Loading';
import OpeningsView from './pages/Openings_view';
import NavBar from './features/nav/navBar';

function App() {
  return (
    <div className="App">
    <NavBar/>
    <Router>
      <Routes>
        <Route exact path="/" element={<Homepage/>}/>
        <Route exact path="/choice" element={<Choice/>}/>
        <Route exact path="/loading" element={<Loading/>}/>
        <Route exact path="/jobs" element={<OpeningsView/>}/>
      </Routes>
    </Router>
    </div>
  );
}

export default App;
