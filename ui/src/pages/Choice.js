import React, { useState } from 'react';
import {Link} from 'react-router-dom'
import "./Choice.css"
const Choice = () => {
    const Data=[
        {
           id:1,
           subject:"Internship",
           selected:false
        },
        {
            id:2,
            subject:"New_Graduates",
            selected:false
         }
         ,{
            id:3,
            subject:"Experienced",
            selected:false
         }
    ]
   const [select,setSelect]= useState(Data)
   console.log("selected",select)
    const handleonClick=(item)=>{
        const newItems=select.map((val)=>{
            if(val.id===item.id){
                return {...val,selected:!val.selected}
            }
            else
            {
                return val;
            }

        })
        
        setSelect(newItems)
    }

    
 


  return (
    <div className='choice'>
    <div className='user_form_title'>
            Job Type Selection
            </div>
            <div className='main_options'>
                {
                    select.map((item, idx)=>(
                   <center>
                    <div className='options' onClick={()=>handleonClick(item)} style={{backgroundColor:item.selected?'#7F53AC':'#647DEE'}} >
                        {item.subject}
                        </div>
                        </center>
                    ))
                }
                {/* <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSB6FBLdTfaMvSCP_YNKDa0YiG26znI44d2PooB2B19ghWqh-1HuwWe71vhexanpdJylAI&usqp=CAU"></img>
                <img src="https://www.shutterstock.com/image-vector/graduated-student-logo-260nw-1174254523.jpg"></img> */}
                 <center>
                 <Link to ='/loading'>
                 
                <div className='btn1'>
                 Show Openings
                </div>
                </Link>
                </center>
            </div>

         

    </div>
  )
}

export default Choice
