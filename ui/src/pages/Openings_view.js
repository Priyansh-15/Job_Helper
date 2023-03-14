import React from 'react'
import {Link} from 'react-router-dom'
import "./Openings_view.css"
const Openings_view = () => {
    const job_data=[
        {
            image_url:"https://blog.hubspot.com/hubfs/image8-2.jpg",
            Company_Name:"Google",
            Job_Title:"Commodity Manager, Supplier Responsibility and Supply Chain Sustainability",
            Job_Type:"Internship",
            Job_Location:"London,Uk",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study. Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
            Url:"https://careers.google.com/jobs/results/108830945294852806-commodity-manager-supplier-responsibility-and-supply-chain-sustainability/?distance=50&employment_type=FULL_TIME"    

        },
        {
            image_url:"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Amazon_icon.svg/2048px-Amazon_icon.svg.png",
            Company_Name:"Amazon",
            Job_Title:"Sr Embedded Software Engineer- Graviton AWS",
            Job_Type:"Experienced",
            Job_Location:"Bengaluru,India",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study. Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
            Url:"https://www.amazon.jobs/en/jobs/2336434/sr-embedded-software-engineer-graviton-aws"    

        }
        ,
        {
            image_url:"https://cdn-icons-png.flaticon.com/512/882/882730.png",
            Company_Name:"Cisco",
            Job_Title:"Application Software Developer",
            Job_Type:"New Graduate",
            Job_Location:"Chennai,India",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study. Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
            Url:"https://careers.google.com/jobs/results/108830945294852806-commodity-manager-supplier-responsibility-and-supply-chain-sustainability/?distance=50&employment_type=FULL_TIME"    

        }
        ,
        {
            image_url:"https://blog.hubspot.com/hubfs/image8-2.jpg",
            Company_Name:"Google",
            Job_Title:"Commodity Manager, Supplier Responsibility and Supply Chain Sustainability",
            Job_Type:"Internship",
            Job_Location:"London,Uk",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study. Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study",
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
        <div className='user_form_title'>
              Available Jobs
            </div>
            
      {
        job_data.map((item)=>(
                   <center>
                    <div className='job_tab'>
                        <div className='first_r'>
                          <div className='IMAGE'>
                            <img src={item.image_url} alt="icon" width="70" height="70"/>
                          </div>
                          <div className='j_type'>

                            {item.Company_Name} - {item.Job_Type}
                            <div className='j_loca'>
                            {item.Job_Location}
                          </div>
                          </div>
                        </div>
                        
                        <div className='j_title'>
                            {item.Job_Title}
                            
                        </div> 
                        <div className='j_desc'>
                            {item.Description}
                            
                        </div> 
                        <Link to={item.Url}>
                        <div className='j_apply'>
                            Apply Now
                        </div> 
                        </Link>

                        </div>
                        </center>

                       
                    ))
                }
                </div>
    
  )
}

export default Openings_view
