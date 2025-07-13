import React from "react";
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import Detail from "./components/Detail";
import Review from "./components/Review";
import Data from "./components/Data";
import Base from "./components/Base";
import { Routes,Route } from "react-router-dom";
import Login from "./pages/Login";
import RegisterPage from "./pages/RegisterPage";
import PartnerPermission from "./components/PartnerPermission";
import ManagerPermission from "./components/ManagerPermission";
import SalesPermission from "./components/SalesPermission";

const App = () => {

  return (
    <div>
      <Navbar />
      <HeroSection />
      <Detail />
      <Data/>
      <Review/>
      <Base/>

      <Routes>
        <Route path="/login" element={<Login/>} />
        <Route path="/register" element={<RegisterPage/>} />
        <Route path="/partner" element={<PartnerPermission/>} />
        <Route path="/manager" element={<ManagerPermission/>} />
        <Route path="/sales" element={<SalesPermission/>} />
        </Routes>

    </div>
  );
};

export default App;
