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
            POSITIONS APPLYING FOR
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
