import { Check, X } from 'lucide-react';
import { FaArrowLeft } from "react-icons/fa";
import { LuPencil } from "react-icons/lu";
import { TiTick } from "react-icons/ti";

const permissionData = [
  {
    title: 'Sales Vouchers (Sales, Quotation, Payment In, Sales Return, Other Income)',
    permissions: [
      { name: 'Create Sale', allowed: true },
      { name: 'Delete Sale', allowed: false },
      { name: 'Edit Sale', allowed: false },
      { name: 'View Sale', allowed: true },
    ],
  },
  {
    title: 'Purchase Vouchers (Purchase, Payment Out, Purchase Return)',
    permissions: [
      { name: 'Create Purchase', allowed: false },
      { name: 'Delete Purchase', allowed: false },
      { name: 'Edit Purchase', allowed: false },
      { name: 'View Purchase', allowed: false },
    ],
  },
  {
    title: 'Income & Expenses',
    permissions: [
      { name: 'Create Income Expense', allowed: true },
      { name: 'Delete Income Expense', allowed: false },
      { name: 'Edit Income Expense', allowed: false },
      { name: 'View Income Expense', allowed: true },
    ],
  },
  {
    title: 'Inventory (Item, Category)',
    permissions: [
      { name: 'Create Item', allowed: false },
      { name: 'Delete Item', allowed: false },
      { name: 'Edit Delete Item Category', allowed: false },
      { name: 'Edit Item', allowed: true },
      { name: 'View Item', allowed: true },
      { name: 'View Item Category', allowed: true },
    ],
  },
  {
    title: 'Stock Adjustments',
    permissions: [
      { name: 'Create Adjustments', allowed: false },
      { name: 'Delete Adjustments', allowed: false },
      { name: 'Edit Adjustments', allowed: false },
    ],
  },
  {
    title: 'Customers',
    permissions: [
      { name: 'Create Customer', allowed: true },
      { name: 'Delete Customer', allowed: false },
      { name: 'Edit Customer', allowed: true },
      { name: 'View Customer', allowed: true },
    ],
  },
];

const SalesPermission = () => {
  return (
    <div className="p-6 max-w-5xl mx-auto bg-gray-50 min-h-screen">
      <div className="bg-white rounded-2xl shadow-sm border border-gray-300 p-4 mb-6">
        <h1 className="text-xl font-medium mb-4 flex gap-1 items-center">
          <FaArrowLeft className="h-4" /> Sales Person's Permissions
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {permissionData.map((section, index) => (
            <div key={index} className="border border-gray-200 rounded p-8">
              <h2 className="text-sm font-bold mb-3">{section.title}</h2>
              <ul className="space-y-2">
                {section.permissions.map((perm, idx) => (
                  <li key={idx} className="flex items-center space-x-2 text-[13px]">
                    {perm.allowed ? (
                      <Check className="w-4 h-4 text-green-500" />
                    ) : (
                      <X className="w-4 h-4 text-red-500" />
                    )}
                    <span className="text-gray-500">{perm.name}</span>
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

export default SalesPermission;
