import React from 'react'
import "./Loading.css"
const Loading = () => {
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
            Please wait...
         </div>
      </div>
  )
}

export default Loading
