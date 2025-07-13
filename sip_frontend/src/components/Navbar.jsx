import React from 'react'
import { FaLongArrowAltRight } from "react-icons/fa";
import { NavLink } from 'react-router-dom';

const Navbar = () => {
  return (
    <div>
        <div className='flex justify-around h-[7rem] mt-3 items-center'>

            <img src="logo.png" alt="logo" />
            <ul className='flex gap-7 '>
                <li>Home</li>
                <li>Feature</li>
                <li>Resources</li>
                <li>Contact</li>

            </ul>
            <NavLink to='/login' className='bg-[#0B2545] flex justify-center items-center text-white border-2 rounded-xl h-[2.7rem] w-[8rem] mr-3.5 p-1.5 mt-6 \'>Get Started<FaLongArrowAltRight /></NavLink>
        </div>
        <hr className='text-gray-300 w-[80rem] ml-[6rem]'/>
        
        


    </div>
  )
}

export default Navbar