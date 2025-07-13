
import { useForm } from "react-hook-form";
import { FaGoogle, FaEnvelope, FaLock } from "react-icons/fa";
import { NavLink, useNavigate } from "react-router-dom";


const Login=()=> {
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    try {
    const response = await fetch("http://localhost:8000/api/users/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials:'include',
      body: JSON.stringify({
        email: data.email, 
        password: data.password,
      }),
    });
    
    const result = await response.json();

    if (response.ok) {
      
      

      
      navigate("/");
    } else {
      alert(result.detail || "Invalid credentials");
    }
  } catch (error) {
    console.error("Login error:", error);
    alert("Something went wrong");
  }
};

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
      <div id="loader"></div>
      <div className="bg-white shadow-lg rounded-xl flex flex-col md:flex-row w-full max-w-5xl overflow-hidden">
        <div className="w-full md:w-1/2 p-10 flex flex-col justify-center">
          <div className="flex items-center space-x-3 mb-2">
            <img src="logo.png" alt="Mero Byapar Logo" className="h-[10rem]" />
          </div>

          <h2 className="text-2xl font-semibold mb-2 text-gray-900">Let’s Get Started</h2>
          <p className="text-gray-600 mb-6">Please login to continue</p>

          <form onSubmit={handleSubmit(onSubmit)}>
            <div className="flex items-center border border-gray-300 rounded-md overflow-hidden mb-4">
              <span className="bg-gray-100 px-3 py-2 text-gray-700">
                <FaEnvelope />
              </span>
              <input
                type="email"
                placeholder="you@example.com"
                className="w-full px-3 py-2 outline-none text-gray-900"
                
                {...register("email", { required: "Email is required" })}
              />
            </div>
            {errors.email && (
              <p className="text-sm text-red-500 mb-2">{errors.email.message}</p>
            )}

            <div className="flex items-center border border-gray-300 rounded-md overflow-hidden">
              <span className="bg-gray-100 px-3 py-2 text-gray-700">
                <FaLock />
              </span>
              <input
                type="password"
                placeholder="••••••••"
                className="w-full px-3 py-2 outline-none text-gray-900"
                
                {...register("password", { required: "Password is required" })}
              />
            </div>
            {errors.password && (
              <p className="text-sm text-red-500 mt-2">{errors.password.message}</p>
            )}

            <button
              type="submit"
              className="w-full bg-indigo-900 text-white py-2 rounded-md mt-6 hover:bg-indigo-800 transition"
            >
              Continue
            </button>
          </form>

          <div className="my-6 text-center text-gray-400">or</div>

          <button className="w-full flex items-center justify-center bg-black text-white py-2 rounded-md hover:bg-gray-800 transition">
            <FaGoogle className="mr-2" /> Sign in with Google
          </button>

          <p className="text-sm text-gray-600 mt-6 text-center">
            Don’t have an account?{" "}
            <NavLink
              to="/register"
              className="font-semibold text-indigo-900 cursor-pointer hover:underline"
            >
              Register
            </NavLink>
          </p>
        </div>

        <div className="hidden md:flex w-1/2 bg-indigo-50 items-center justify-center p-10">
          <img
            src="loginbg.png"
            alt="App Preview"
            className="max-w-full max-h-[30rem] object-contain"
          />
        </div>
      </div>
      
    </div>
  );
}
export default Login
