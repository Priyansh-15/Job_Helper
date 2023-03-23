import React from 'react'
import {Link} from 'react-router-dom'
import { ImLocation } from 'react-icons/im';
import { HiOfficeBuilding } from 'react-icons/hi';
import "./Openings_view.css"
import Navbar from '../components/Navbar';

const Openings_view = () => {
    const num1=499;
    const job_data=[
        {
            image_url:"https://static.vecteezy.com/system/resources/previews/009/469/630/original/google-logo-isolated-editorial-icon-free-vector.jpg",
            Company_Name:"Google",
            Job_Title:"Information Technology Intern",
            Job_Type:"Internship",
            Job_Location:"Sydney NSW, Australia",
            Description:"Currently pursuing a Bachelor’s degree in Information Technology or related technical field.Currently in your penultimate year of study.",
            Url:"https://careers.google.com/jobs/results/84209077426496198-information-technology-intern-summer-2023-indigenous-identified/?degree=BACHELORS&distance=50&employment_type=INTERN"    

        },
        
        {
            image_url:"https://www.citypng.com/public/uploads/preview/-11596400565qsuxfwyv9j.png",
            Company_Name:"Amazon",
            Job_Title:"Software Development Engineer Internship (H/F)",
            Job_Type:"Internship",
            Job_Location:"FR, Bordeaux",
            Description:"Collaborate with experienced cross-disciplinary Amazonians to conceive, design, and bring to market innovative products and services.",
            Url:"https://www.amazon.jobs/en/jobs/2206003/2023-software-development-engineer-internship-h-f"    

        },
        {
            image_url:"https://static.vecteezy.com/system/resources/previews/009/469/630/original/google-logo-isolated-editorial-icon-free-vector.jpg",
            Company_Name:"Google",
            Job_Title:"Commodity Manager, Supplier Responsibility and Supply Chain Sustainability",
            Job_Type:"Internship",
            Job_Location:"London,Uk",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
            Url:"https://careers.google.com/jobs/results/108830945294852806-commodity-manager-supplier-responsibility-and-supply-chain-sustainability/?distance=50&employment_type=FULL_TIME"    

        },
        
        {
            image_url:"https://www.citypng.com/public/uploads/preview/-11596400565qsuxfwyv9j.png",
            Company_Name:"Amazon",
            Job_Title:"Sr Embedded Software Engineer- Graviton AWS",
            Job_Type:"Experienced",
            Job_Location:"Bengaluru,India",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
            Url:"https://www.amazon.jobs/en/jobs/2336434/sr-embedded-software-engineer-graviton-aws"    

        }
        ,
        {
            image_url:"https://cdn-icons-png.flaticon.com/512/882/882730.png",
            Company_Name:"Cisco",
            Job_Title:"Application Software Developer",
            Job_Type:"New Graduate",
            Job_Location:"Chennai,India",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
            Url:"https://careers.google.com/jobs/results/108830945294852806-commodity-manager-supplier-responsibility-and-supply-chain-sustainability/?distance=50&employment_type=FULL_TIME"    

        }
        ,
        {
            image_url:"https://blog.hubspot.com/hubfs/image8-2.jpg",
            Company_Name:"Google",
            Job_Title:"Commodity Manager, Supplier Responsibility and Supply Chain Sustainability",
            Job_Type:"Internship",
            Job_Location:"London,Uk",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
            Url:"https://careers.google.com/jobs/results/108830945294852806-commodity-manager-supplier-responsibility-and-supply-chain-sustainability/?distance=50&employment_type=FULL_TIME"    

        }
        ,
        {
            image_url:"https://blog.hubspot.com/hubfs/image8-2.jpg",
            Company_Name:"Google",
            Job_Title:"SDE",
            Job_Type:"Internship",
            Job_Location:"London,Uk",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study"    

        }
        ,
        {
            image_url:"https://blog.hubspot.com/hubfs/image8-2.jpg",
            Company_Name:"Google",
            Job_Title:"SDE",
            Job_Type:"Internship",
            Job_Location:"London,Uk",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study"    

        }
    ]
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
                           {item.Job_Title}
                            
                        </div> 
                        </Link>
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
                        

                        </div>
                        </center>

                       
                    ))
                }
                </div>
    
  )
}

export default Openings_view
