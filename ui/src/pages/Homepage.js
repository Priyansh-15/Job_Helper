import React from 'react'


import "./Homepage.css"
const Homepage = () => {
  return (
    
    <div>
        
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
                            <input type="text"  className='search_box' name="name" placeholder='Full Name'/>
                        </div>
                            
                      <div className='labels'>
                         <span>Email</span>
                          <br/>
                            <input type="text" className='search_box'  name="email" placeholder='xyz@mail.com'/>
                      </div>
                      
                      <div className='labels'>
                      <span>Phone Number</span>
                          <br/>
                            <input type="text" className='search_box'  name="phoneno" placeholder='xxxxxxxxxx'/>
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
                            <input type="text" className='search_box'  name="major" />
                      </div>
                      <div className='labels'>
                          <span>GPA</span>
                          <br/>
                            <input type="text" className='search_box'  name="gpa" placeholder='scale of 10'/>
                      </div>
                      
                      </div>
                  </fieldset>
                </div>
                
               
                
                <div className='section_2'>
                  <fieldset>
                    <legend>Skill Evaluation</legend>
                    <div className='main_section_2'>
                      <div className='labels'>
                         <span>C++/C</span>
                          <br/>
                            <input type="text" className='search_box'  name="c++/c" placeholder='Rate on scale(1-10)'/>
                      </div>
                      
                      <div className='labels'>
                      <span>Python</span>
                          <br/>
                            <input type="text" className='search_box'  name="python" placeholder='Rate on scale(1-10)'/>
                      </div>
                      
                      <div className='labels'>
                      <span>Java</span>
                          <br/>
                            <input type="text" className='search_box'  name="java" placeholder='Rate on scale(1-10)'/>
                      </div>
                      
                      <div className='labels'>
                      <span>JavaScript</span>
                          <br/>
                            <input type="text" className='search_box'  name="javascript" placeholder='Rate on scale(1-10)'/>
                      </div>
                      <div className='labels'>
                          <span>Data Structures and Algorithms</span>
                          <br/>
                            <input type="text"  className='search_box' name="dsa" placeholder='Rate on scale(1-10)'/>
                        </div>
                      <div className='labels'>
                      <span>Problem Solving</span>
                          <br/>
                            <input type="text" className='search_box'  name="problem" placeholder='Rate on scale(1-10)'/>
                      </div>
                      <div className='labels'>
                          <span>MySQL</span>
                          <br/>
                            <input type="text" className='search_box'  name="sql" placeholder='Rate on scale(1-10)'/>
                      </div>
                      <div className='labels'>
                          <span>Web services</span>
                          <br/>
                            <input type="text" className='search_box'  name="web" placeholder='Rate on scale(1-10)'/>
                      </div>
                      <div className='labels'>
                          <span>HTML/CSS</span>
                          <br/>
                            <input type="text" className='search_box'  name="html/css" placeholder='Rate on scale(1-10)'/>
                      </div>
                      </div>
                  </fieldset>
                </div>
                <div className='section_3'>
                  <fieldset>
                    <legend>Soft Skills</legend>
                    <div className='main_section_3'>
                    <div className='labels'>
                          <span>Reading, Writing, Speaking (English)</span>
                          <br/>
                            <input type="text" className='search_box'  name="english" placeholder='Rate on scale(1-10)'/>
                      </div>
                      <div className='labels'>
                          <span>Team work</span>
                          <br/>
                            <input type="text" className='search_box'  name="team work" placeholder='Rate on scale(1-10)'/>
                      </div>
                      <div className='labels'>
                          <span>Leadership</span>
                          <br/>
                            <input type="text" className='search_box'  name="leadership" placeholder='Rate on scale(1-10)'/>
                      </div>
                      <div className='labels'>
                          <span>Adaptability</span>
                          <br/>
                            <input type="text" className='search_box'  name="adapt" placeholder='Rate on scale(1-10)'/>
                      </div> 
                      </div>
                  </fieldset>
                </div>
                <div className='section_4'>
                  <fieldset>
                    <legend>Websites and other Links</legend>
                    <div className='main_section_4'>
                    <div className='labels'>
                          <span>Portfolio</span>
                          <br/>
                            <input type="text" className='search_box'  name="portfolio"/>
                      </div> 
                      <div className='labels'>
                          <span>Github</span>
                          <br/>
                            <input type="text" className='search_box'  name="git"/>
                      </div>
                      <div className='labels'>
                          <span>LinkedIn</span>
                          <br/>
                            <input type="text" className='search_box'  name="linked"/>
                      </div> 
                      <div className='labels'>
                          <span>LeetCode</span>
                          <br/>
                            <input type="text" className='search_box'  name="leetcode"/>
                      </div>  
                      <div className='labels'>
                          <span>Codeforces</span>
                          <br/>
                            <input type="text" className='search_box'  name="cf"/>
                      </div> 
                      </div>
                  </fieldset>
                </div>
                <div className='section_5'>
                  <fieldset>
                    <legend>Resume *</legend>
                    <div className='main_section_5'>
                      </div> 
                    <input type='file'/>
                     
                    <button className='btns'> 
                      UPLOAD
                    </button>
                  </fieldset>
                </div>
                <center>
                <div className='btn'>
                  NEXT
                </div>
                </center>
                
            </div>
          
            </form>
            
         </div>
    </div>
  )
}

export default Homepage
