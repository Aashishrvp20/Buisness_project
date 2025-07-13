import React from "react";
import { FaLongArrowAltRight } from "react-icons/fa";

const Data = () => {
  const data = [
    {
      image: "a1.png",
      name: "Record Transactions",
      data: "Add sales, purchases & expenses",
    },
    { image: "a2.png", name: "Manage parties" ,data:"Manage customers & suppliers ledger"},
    { image: "a3.png", name: "Manage inventory" ,data:"Keep track of products in real time"},
    { image: "a4.png", name: "Buisness Insights" ,data:"Keep track of products in real time"},
    { image: "a5.png", name: "Desktop Web Version",data:"View business performance report" },
    { image: "a6.png", name: "Multi Staff",data:"Add users & manage their access" },
    { image: "a7.png", name: "Upload Bill Images" ,data:"Organize paper bills & receipts"},
    { image: "a8.png", name: "Send Payment Reminder",data:"Send reminders via WhatsApp & SMS" },
  ];
  return (
    <div className="text-center mt-8">
      <h2 className="text-center text-blue-400 font-bold mb-4">
        What is meroByapar?
      </h2>
      <h1 className="text-3xl font-bold"> Effortless Buisness</h1>
      <h1 className="text-black text-3xl font-bold">management start here</h1>
      <h2 className="text-gray-500 mt-[2rem]">
        Manage your accounting and inventory with ease- MeroByapar is your
        all-in-one digital buisness assistant
      </h2>
      <h2 className="text-center text-gray-500">on mobile and desktop</h2>

      <div className="flex justify-center align-middle items-center rounded-3xl mt-15">
        <img
          src="desc.png"
          alt="abcs"
          className="h-[500px] w-[900px] rounded "
        />
      </div>

      <div className="mt-[5rem] flex flex-col gap-6">
        <h1 className="text-[#1F2262] text-xl font-bold">Key Features</h1>
        <h1 className="text-3xl font-bold">ALL U Need. Just One App.</h1>
        <h1 className="text-gray-500">
          Mero Byapar simplifies buisness: track finances, inventory, and
          clients in one smart app
        </h1>
      </div>

      <div className="grid grid-cols-4 mt-[5rem] gap-[4rem] w-[70%] relative left-[15rem] ">
        {data.map((i, index) => {
          return (
            <div
              key={index}
              className="flex flex-col justify-center align-middle items-center"
            >
              <div className="  h-[13rem] w-[13rem]">
                <img src={i.image} alt="" className="" />
              </div>
              <h2 className="font-bold mt-3">{i.name}</h2>
              <h1 className="text-gray-500 text-[12px] mt-3">{i.data}</h1>
            </div>
          );
        })}
      </div>
     <center className="mb-5"><button className="border-2 border-gray-200 h-[3rem] rounded-xl p-2 w-[12rem] font-bold  flex gap-1.5 justify-center align-middle items-center mt-[3.5rem] ">View All Feature <FaLongArrowAltRight /> </button>
</center>


    </div>
  );
};

export default Data;
