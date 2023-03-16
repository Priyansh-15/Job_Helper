import React from 'react'
import "./Loading.css"
import {useLocation} from 'react-router-dom'

    
const Loading = () => {
   const location = useLocation();
   console.log(location.state)
  return (
    <div class="container">
         <div class="wrapper">
            <div class="loader">
               <div class="dot"></div>
            </div>
            <div class="loader">
               <div class="dot"></div>
            </div>
            <div class="loader">
               <div class="dot"></div>
            </div>
            <div class="loader">
               <div class="dot"></div>
            </div>
            <div class="loader">
               <div class="dot"></div>
            </div>
            <div class="loader">
               <div class="dot"></div>
            </div>
         </div>
         <div class="text">
            Extracting matched jobs...
         </div>
      </div>
  )
}

export default Loading
