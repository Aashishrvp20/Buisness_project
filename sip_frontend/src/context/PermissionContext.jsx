// src/context/PermissionContext.js
import React, { createContext, useState } from 'react';

export const PermissionContext = createContext();

const initialPermissions = {};
[
  'Create Sale', 'Delete Sale', 'Edit Sale', 'View Sale',
  'Create Purchase', 'Delete Purchase', 'Edit Purchase', 'View Purchase',
  'Create Income Expense', 'Delete Income Expense', 'Edit Income Expense', 'View Income Expense',
  'Create Item', 'Delete Item', 'Edit Delete Item Category', 'Edit Item',
  'Create Adjustments', 'Delete Adjustments', 'Edit Adjustments',
  'Create Customer', 'Delete Customer', 'Edit Customer', 'View Customer',
].forEach(p => initialPermissions[p] = !p.toLowerCase().includes('delete'));

export const PermissionProvider = ({ children }) => {
  const [permissions, setPermissions] = useState(initialPermissions);

  return (
    <PermissionContext.Provider value={{ permissions, setPermissions }}>
      {children}
    </PermissionContext.Provider>
  );
};
