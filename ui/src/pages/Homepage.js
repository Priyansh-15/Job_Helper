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
            <form>
            <div className='form'>
              
                <div className='section_1'>
                  <fieldset>
                    <legend>Personal Details</legend>
                    <div className='main_section_1'>
                        <div className='labels'>
                          <span>Name</span>
                          <br/>
                            <input type="text"  className='search_box' name="name"/>
                        </div>
                            
                      <div className='labels'>
                         <span>Email</span>
                          <br/>
                            <input type="text" className='search_box'  name="email"/>
                      </div>
                      
                      <div className='labels'>
                      <span>Phone Number</span>
                          <br/>
                            <input type="text" className='search_box'  name="phoneno"/>
                      </div>
                      
                      <div className='labels'>
                      <span>College</span>
                          <br/>
                            <input type="text" className='search_box'  name="college"/>
                      </div>
                      
                      <div className='labels'>
                      <span> Degree</span>
                          <br/>
                            <input type="text" className='search_box'  name="degree"/>
                      </div>
                     
                      <div className='labels'>
                      <span>Major</span>
                          <br/>
                            <input type="text" className='search_box'  name="major"/>
                      </div>
                      <div className='labels'>
                          <span>GPA</span>
                          <br/>
                            <input type="text" className='search_box'  name="gpa"/>
                      </div>
                      
                      </div>
                  </fieldset>
                </div>
             
                
                
            </div>
            </form>
         </div>
    </div>
  )
}

export default Homepage
