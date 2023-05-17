import React, {useEffect, useState} from 'react'
import "./Loading.css"
import {useLocation} from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import axios from 'axios';
    
const Loading = () => {
   const location = useLocation();
   const navigate = useNavigate();
   let temp=location.state
   let c='0',py='0',j='0',js='0',dsa='0',ps='0',sql='0',wb='0',hs='0',co='0',l='0',t='0',a='0';
   let category=""
   if(temp.cplus!==undefined){
      c=temp.cplus
   }
   if(temp.python!==undefined){
      py=temp.python
   }
   if(temp.java!==undefined){
      j=temp.java
   }
   if(temp.javascript!==undefined){
      js=temp.javascript
   }
   if(temp.dsa!==undefined){
      dsa=temp.dsa
   }
   if(temp.problem_solving!==undefined){
      ps=temp.problem_solving
   }
   if(temp.sql!==undefined){
      sql=temp.sql
   }
   if(temp.html_css!==undefined){
      hs=temp.html_css
   }
   if(temp.web!==undefined){
      wb=temp.web
   }
   if(temp.english!==undefined){
      co=temp.english
   }
   if(temp.team_work!==undefined){
      t=temp.team_work
   }
   if(temp.leadership!==undefined){
      l=temp.leadership
   }
   if(temp.adapt!==undefined){
      a=temp.adapt
   }

   if(temp[0].selected===true){
      category="internship"
   }

   if(temp[1].selected===true){
      category="newgrad"
   }

   if(temp[2].selected===true){
      category="experienced"
   }

   let url="http://127.0.0.1:5000/"+category+"_api?c="+c+"&py="+py+"&j="+j+"&js="+js+"&dsa="+dsa+"&ps="+ps+"&sql="+sql+"&wb="+wb+"&hs="+hs+"&co="+co+"&t="+t+"&l="+l+"&a="+a
   console.log(url)
   
   const [people, setPeople]= useState([]);
   console.log(people)
  
   console.log(people.length)
   useEffect(()=>{
      axios.get(url).then(res=>setPeople(res.data));
   },[]);
   console.log(people)
   console.log(people.length)
   navigate('/jobs',{state:people})
   
   
   
   
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
            Just a moment...
         </div>
      </div>
  )
}

export default Loading
