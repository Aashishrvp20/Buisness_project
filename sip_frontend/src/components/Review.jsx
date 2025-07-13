import React, { useEffect, useState } from 'react'

const Review = () => {
    const[review,setReview]=useState([])
    const Data=async()=>{
        let response =await fetch ("http://127.0.0.1:8000/api/reviews/review/")
        response=await response.json()
        console.log(response)
        setReview(response)

    }
    useEffect(()=>{Data()},[])
  return (
  <div className="px-10 py-8 bg-[#F9F9F9] mt-[7rem]">
    <h1 className="text-2xl font-bold text-center mb-2">Real Stories from Real Business Owners</h1>
    <p className="text-center text-gray-500 mb-[6rem]">
      MeroByaapar powers financial management for 30k+ businesses across the country.
    </p>
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-6 w-[70%] mx-auto">
      {review.map((i, index) => (
        <div key={index} className="bg-white shadow-md rounded-2xl h-[14rem]  p-3 hover:shadow-lg transition">
          <h1 className="text-yellow-500 text-lg mb-2">
            {"⭐".repeat(Math.round(i.rating))}
          </h1>
          <p className="text-gray-700 mb-4 text-[12px] leading-relaxed">{i.msg}</p>
          <div className="flex items-center gap-3 mt-12">
            <img
              src={i.logo_photo}
              alt="user"
              className="h-10 w-10 rounded-full object-cover hover:scale-110 transition-transform"
            />
            <div>
              <p className="text-sm font-medium">{i.name}</p>
              <p className="text-xs text-gray-500">{i.brand_post}</p>
            </div>
          </div>
        </div>
      ))}
    </div>
  </div>
);
}

export default Review