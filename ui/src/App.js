import Homepage from './pages/Homepage';
import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";
import './App.css';

function App() {
  return (
    <div className="App">
    <Router>
      <Routes>
        <Route exact path="/" element={<Homepage/>}/>
      
      </Routes>
    </Router>
    </div>
  );
}

export default App;
