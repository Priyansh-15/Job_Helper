import React from 'react'
import "./Openings_view.css"
const Openings_view = () => {
    const job_data=[
        {
            image_url:"https://blog.hubspot.com/hubfs/image8-2.jpg",
            Company_Name:"Google",
            Job_Title:"SDE",
            Job_Type:"Internship",
            Job_Location:"London,Uk",
            Description:"Currently pursuing a Bachelors degree in Information Technology or related technical field.Currently in your penultimate year of study"    

        },
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

        },
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
            <div className='job_space'>
      {
        job_data.map((item)=>(
               
                    <div className='job_tab'>
                        <div className='IMAGE'>
                        <img src={item.image_url} alt="icon" width="100" height="80"/>
                        </div>
                        <div className='job_details'>
                            
                        <div className='j_title'>
                            {item.Job_Title}
                            </div>  
                            <div className='j_type'>
                            {item.Company_Name} - {item.Job_Type}
                            </div>
                            <div className='j_loca'>
                            {item.Job_Location}
                            </div>
                            <div className='j_desc'>
                            {item.Description}
                            </div>
                        </div> 

                        </div>
                       
                    ))
                }
                </div>
    </div>
  )
}

export default Openings_view
