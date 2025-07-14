import { BrowserRouter } from 'react-router-dom'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { PermissionProvider } from './context/PermissionContext.jsx'

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
  <PermissionProvider>
    <App />
  </PermissionProvider>
  </BrowserRouter>
)
