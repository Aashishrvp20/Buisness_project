import React from 'react'
import { NavLink } from 'react-router-dom';

const Detail = () => {
      const Data = [
    {
      svg: "/SVG.png",
      name: "kirana pasal",
    },
    {
      svg: "/SVG1.png",
      name: "contruction",
    },
    {
      svg: "/SVG2.png",
      name: "Agriculture",
    },
    {
      svg: "/SVG3.png",
      name: "Electronic",
    },
    {
      svg: "/SVG4.png",
      name: "Clothing",
    },
    {
      svg: "/SVG5.png",
      name: "Food and Bevrages",
    },
    
    {
      svg: "/SVG6.png",
      name: "Medicine and Healthcare",
    },
    {
      svg: "/SVG7.png",
      name: "Hardware",
    },
    {
      svg: "/SVG8.png",
      name: "Auto/Parts",
    },
    {
      svg: "/SVG9.png",
      name: "Mobile pasal",
    },
  ];
  return (
    <div>
      <NavLink to='/sales' className='flex justify-center align-middle font-bold text-2xl mb-2'>Made to grow with Buisness</NavLink>
    
    <div className='flex justify-center gap-4 h-[15rem]'>
        
        
 {Data.map((i,index)=>{
    return <div key={index}  className='bg-gray-50 shadow-2xl w-[13rem] h-[10rem] p-2 flex flex-col gap-2.5 text-center justify-center items-center rounded-xl '>
        <img src={i.svg} alt=""  className='h-7 w-7' />
        <h2>{i.name}</h2>

    </div>
   
 })}

    </div>
   
    </div>
     
  )
}

export default Detail