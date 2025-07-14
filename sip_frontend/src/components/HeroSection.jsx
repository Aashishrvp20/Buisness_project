import React, { useEffect, useState } from "react";
import { FaLaptopCode } from "react-icons/fa";
import { MdOutlineFileDownload } from "react-icons/md";
import SplitText from "./SpiltText.jsx";
import { NavLink } from "react-router-dom";

const HeroSection = () => {
  const [showLogo, setShowLogo] = useState(false);

  useEffect(() => {
    const timeout = setTimeout(() => setShowLogo(true), 100);
    return () => clearTimeout(timeout);
  }, []);

  return (
    <div className="flex justify-evenly items-center flex-wrap px-4 py-8">
      <div>
        <div>
          <SplitText
            text="Byapar KO Control"
             className="text-4xl font-bold text-center"
            delay={150}
            duration={0.6}
            ease="power3.out"
            splitType="chars"
            from={{ opacity: 0, y: 40 }}
            to={{ opacity: 1, y: 0 }}
            threshold={0.1}
            rootMargin="-100px"
            textAlign="center"
          />
      

          <h1 className="text-4xl mb-5 font-bold">JaHa Pani, Jahile Pani</h1>
          <NavLink to='student/' className="text-gray-600 text-m">
            Mero Byapar simplifies business for you – smart, efficient, and </NavLink>
            <br />
           <p> stress-free. Track sales, manage expenses, maintain ledgers, <br />
            control inventory, and more – all from one easy platform.
          </p>
        </div>
        <div className="mt-8 flex gap-9">
          <NavLink to='/manager' className="bg-[#0B2545] gap-2 text-white items-center justify-center rounded flex border-2 border-black h-[2.5rem] w-[10rem]">
            <FaLaptopCode />
            Use web version
          </NavLink>
          <NavLink to='/partner' className="flex gap-2 items-center justify-center rounded border-2 border-gray-300 h-[2.5rem] w-[10rem]">
            <MdOutlineFileDownload />
            Download App
          </NavLink>
        </div>
      </div>

      <div className="flex justify-start mb-4 overflow-hidden">
        <img
          src="bg.png"
          alt="Mero Byapar Logo"
          className={`object-contain max-w-[400px] transition-all duration-[1000ms] ease-[cubic-bezier(0.25, 1, 0.5, 1)] 
            ${showLogo ? 'translate-x-0 opacity-100' : 'translate-x-20 opacity-0'}`}
        />
      </div>
    </div>
  );
};

export default HeroSection;
