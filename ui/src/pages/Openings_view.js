import React from 'react'
import {Link,useLocation} from 'react-router-dom'
import { ImLocation } from 'react-icons/im';
import { HiOfficeBuilding } from 'react-icons/hi';
import "./Openings_view.css"
import Navbar from '../components/Navbar';
import data from './internship_jobs.json'
const Openings_view = () => {
  const location2 = useLocation();

    const job_data=location2.state
    let num1=job_data.length
  return (
    <div>
        <Navbar/>
        <div className='user_form_titleo'>
             {num1} jobs matched
            </div>        
      {
        job_data.map((item)=>(
                   <center>
                    <div className='job_tab'>
                        <div className='first_r'>
                          <div className='IMAGE'>
                            <img src={item.image_url} alt="icon" width="70" height="70"/>
                          </div>
                          <div className='title_tag'>
                          <Link to={item.Url} target='_blank'>
                          <div className='j_title'>
                           {item.Job_title}
                            
                        </div> 
                        <br/>
                        </Link>
                        
                        <div className='j_title'>
                        Success Percentage:-
                        {item.Percentage}
                            
                        </div>
                        
                        
                        <div className='j_type'>
                        <div className='j_comp'>
                        <HiOfficeBuilding/>&nbsp;&nbsp;{item.Company_Name} - {item.Job_Type}
                           </div>
                        <div className='j_loca'>
                           <ImLocation/>&nbsp;&nbsp;{item.Job_Location}
                        </div>
                        </div>
                        </div>
                        </div>
                        
                        
                        <div className='j_desc'>
                            Basic Qualification:-
                            <ul>
                                <dl>{item.Description}<Link to={item.Url} target='_blank' style={{display:'inline-block' , textDecoration:'none'}}>&nbsp;...Read More</Link></dl>
                                
                            </ul>
                            
                            
                        </div> 
                        
                        <div className='j_mis'>
                          
                            <ul>
                                Missing_Skills:-{item.Missing_Skills}
                                
                            </ul>
                            
                            
                        </div> 
                        </div>
                        </center>

                       
                    ))
                }
                </div>
    
  )
}

export default Openings_view
