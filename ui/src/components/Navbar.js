import React from 'react'
import './Navbar.css';
import {Link} from 'react-router-dom'
const Navbar = () => {
  return (
    <nav className='nav-bar'>
    <div className='sub-nav'>
        <h1>Job Helper</h1>
    </div>
    <div className='sub-nav'>
        <ul>
            <Link to='/'><li>Home</li></Link>
            <li>About</li>
            <li>Stuff</li>
        </ul>
    </div>
</nav>
  )
}

export default Navbar
