import React from 'react'
import Navbar from '../components/Navbar'

import "./Homepage.css"
const Homepage = () => {
  return (
    
    <div>
        <Navbar/>
         <div className='mainapp'>
            <div className='user_form_title'>
              User Profile Details
            </div>
            <div className='form'>
                <div className='section_head'>Personal details</div>
                
            </div>
         </div>
    </div>
  )
}

export default Homepage
