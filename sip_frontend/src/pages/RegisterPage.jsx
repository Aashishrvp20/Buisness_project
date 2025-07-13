import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';

const RegisterPage = () => {
  const { register, reset, handleSubmit } = useForm();
  const navigate = useNavigate();
  const roles = ['staff', 'customer', 'instructor', 'student'];

  const submit = async (data) => {
    try {
      const response = await fetch('http://localhost:8000/api/users/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      console.log("User registered successfully:", result);
      reset();
      navigate('/login');
    } catch (error) {
      console.error("Error registering user:", error);
      alert("An error occurred. Please try again later.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
      <div className="bg-white rounded-2xl shadow-md p-8 w-full max-w-md">
        
       
        <div className="flex justify-start mb-4">
          <img 
            src="logo.png" 
            alt="Mero Byapar Logo" 
            className="w-[12rem] h-[8rem] object-contain"
          />
        </div>

        <h2 className="text-2xl font-semibold text-gray-800 mb-2">Create an Account</h2>
        <p className="text-sm text-gray-500 mb-6">
          Please enter the following details to get started
        </p>

        <form onSubmit={handleSubmit(submit)} className="space-y-4">
          {/* Email */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Your Email</label>
            <input
              type="email"
              {...register('email', { required: true })}
              placeholder="eg. ramkc@example.com"
              className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />
          </div>

          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Your Password</label>
            <input
              type="password"
              {...register('password', { required: true })}
              placeholder="eg. Hbsg226b"
              className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />
          </div>

          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Your Phone</label>
            <input
              type="tel"
              {...register('phone', { required: true })}
              placeholder="eg. +977743434"
              className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />
          </div>

          {/* Role */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Role</label>
            <select
              {...register('role', { required: true })}
              className="w-full border border-gray-300 rounded-lg px-4 py-2 bg-white focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            >
              <option value="">Select Role</option>
              {roles.map((role, index) => (
                <option key={index} value={role}>
                  {role}
                </option>
              ))}
            </select>
          </div>

          
          <div className="flex justify-between mt-6">
            <button
              type="button"
              onClick={() => navigate('/login')}
              className="flex items-center gap-1 px-4 py-2 rounded-lg bg-gray-200 text-gray-700 hover:bg-gray-300 transition"
            >
              ← Back
            </button>
            <button
              type="submit"
              className="px-4 py-2 rounded-lg bg-blue-950 text-white hover:bg-blue-700 transition"
            >
              Create an Account
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default RegisterPage;
