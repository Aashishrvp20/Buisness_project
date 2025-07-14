import React from 'react';
import { Check,X } from 'lucide-react';
import { FaArrowLeft } from "react-icons/fa";
import { LuPencil } from "react-icons/lu";
import { TiTick } from "react-icons/ti";

const permissionData = [
  {
    title: 'Sales Vouchers (Sales, Quotation, Payment In, Sales Return, Other Income)',
    permissions: ['Create Sale', 'Delete Sale', 'Edit Sale', 'View Sale'],
  },
  {
    title: 'Purchase Vouchers (Purchase, Payment Out, Purchase Return)',
    permissions: ['Create Purchase', 'Delete Purchase', 'Edit Purchase', 'View Purchase'],
  },
  {
    title: 'Income & Expenses',
    permissions: ['Create Income Expense', 'Delete Income Expense', 'Edit Income Expense', 'View Income Expense'],
  },
  {
    title: 'Inventory (Item, Category)',
    permissions: ['Create Item', 'Delete Item', 'Edit Delete Item Category', 'Edit Item'],
  },
  {
    title: 'Stock Adjustments',
    permissions: ['Create Adjustments', 'Delete Adjustments', 'Edit Adjustments'],
  },
  {
    title: 'Customers',
    permissions: ['Create Customer', 'Delete Customer', 'Edit Customer', 'View Customer'],
  },
];

const StudentPermission = () => {
  return (
    <div className="p-6 max-w-5xl mx-auto bg-gray-50 min-h-screen">
      <div className="bg-white rounded-2xl shadow-sm border border-gray-300 p-4 mb-6">
        
        <h1 className="text-xl font-medium mb-4 flex gap-1 items-center">
          <FaArrowLeft className="h-4" /> Student Permissions
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-3 ">
          {permissionData.map((section, index) => (
            <div
              key={index}
              className="border border-gray-200 rounded p-8"
            >
              <h2 className="text-sm font-bold mb-3">{section.title}</h2>
              <ul className="space-y-2">
                {section.permissions.map((i, idx) => (
                  <li key={idx} className="flex items-center space-x-2 text-[13px]">
                    <X className="w-4 h-4 text-red-500" />
                    <span className='text-gray-500'>{i}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
          <div className="flex justify-end space-x-2 mt-4">
        <button className="px-4 py-2 border border-gray-300 text-gray-700 gap-1.5 flex items-center rounded-md text-sm hover:bg-gray-100 transition">
          <LuPencil /> Edit Permission
        </button>
        <button className="px-4 py-2 bg-blue-900 text-white rounded-md flex gap-1 items-center text-sm hover:bg-blue-800 transition">
          <TiTick className="text-white" /> Done
        </button>
      </div>
      </div>

    
    </div>
  );
};

export default StudentPermission;
