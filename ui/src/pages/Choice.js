import React, { useState } from 'react';
import { useNavigate,useLocation } from 'react-router-dom';


import "./Choice.css"
const Choice = () => {
    const location1 = useLocation();
    const navigate = useNavigate();
    
    console.log(location1.state)
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
        let obj={...location1.state,...newItems}
        console.log(obj)
            navigate('/loading',{state:obj })  
    }

  return (
    
    <div className='choice'>
        
    <div className='user_form_title'>
            Job Type Selection
            </div>
            <div className='type_description'>
            You can choose your ideal job match, from the following three options
            </div>
            
            <div className='main_options'>
                <div className='button_row'>
                    <div className='option_col'>
                    
                <div className='image1'>
                    <img src='./image/intern.png' height='120px' width='120px'/>
                  </div>
                  <div className='descript'>
                                  Write something realted to Internship
                  </div>
                    <div className='options' onClick={()=>handleonClick(Data[0])} >
                           
                        {Data[0].subject}
                        </div>
                        </div>
                        <div className='option_col'>
                        <div className='image1'>
                    <img src='./image/new_grad.png' height='120px' width='120px'/>
                  </div>
                  <div className='descript'>
                                  Write something realted to New_Graduates
                  </div>
                        <div className='options' onClick={()=>handleonClick(Data[1])} >
                           
                        {Data[1].subject}
                        </div></div>
                        <div className='option_col'>
                        <div className='image1'>
                    <img src='./image/experienced.png' height='120px' width='120px'/>
                  </div>
                  <div className='descript'>
                                  Write something realted to Experienced candidates
                  </div>
                  <div className='options' onClick={()=>handleonClick(Data[2])} >
                           
                        {Data[2].subject}
                        </div>
                        </div>
                        
                       
                       
                    
                
                </div>
                {/* <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSB6FBLdTfaMvSCP_YNKDa0YiG26znI44d2PooB2B19ghWqh-1HuwWe71vhexanpdJylAI&usqp=CAU"></img>
                <img src="https://www.shutterstock.com/image-vector/graduated-student-logo-260nw-1174254523.jpg"></img> */}
            
                 
        
               
                
            </div>



    </div>
  )
}

export default Choice
