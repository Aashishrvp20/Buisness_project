import React, { useContext} from 'react';
import { useNavigate } from 'react-router-dom';
import { TiTick } from 'react-icons/ti';
import { PermissionContext } from '../context/PermissionContext';

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

const EditManagerPermissions = () => {
  const { permissions, setPermissions } = useContext(PermissionContext);
  const navigate = useNavigate();

  const handleToggle = (perm) => {
    setPermissions(prev => ({
      ...prev,
      [perm]: !prev[perm]
    }));
  };

  const handleDone = () => {
    console.log("Updated permissions:", permissions);
    navigate('/manager');
  };

  return (
    <div className="p-6 max-w-5xl mx-auto bg-gray-50 min-h-screen">
      <h1 className="text-xl font-medium mb-4 flex gap-1 items-center">Edit Permissions</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {permissionData.map((section, index) => (
          <div key={index} className="border  border-gray-200 rounded p-8">
            <h2 className="text-sm font-bold mb-3">{section.title}</h2>
            <ul className="space-y-2">
              {section.permissions.map((perm, idx) => (
                <li key={idx} className="flex items-center space-x-2 text-[13px]">
                  <input
                    type="checkbox"
                    checked={permissions[perm]}
                    onChange={() => handleToggle(perm)}
                  />
                  <span>{perm}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>

      <div className="flex justify-end space-x-2 mt-4">
        <button
          onClick={handleDone}
          className="px-4 py-2 bg-blue-900 text-white rounded-md flex items-center gap-2 hover:bg-blue-800"
        >
          <TiTick /> Done
        </button>
      </div>
    </div>
  );
};

export default EditManagerPermissions;


