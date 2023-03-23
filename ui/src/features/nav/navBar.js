import React from 'react';
import "./navBar.css"
const NavBar = () => {
    return (
        <nav className='nav-bar'>
            <div className='sub-nav'>
                <h1>Job Helper</h1>
            </div>
            <div className='sub-nav'>
                <ul>
                    <li>Home</li>
                    <li>Choices</li>
                    <li>Stuff</li>
                </ul>
            </div>
        </nav>
    )
}

export default NavBar
