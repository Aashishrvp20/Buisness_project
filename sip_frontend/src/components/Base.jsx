import React, { useState } from 'react';
import { FaLongArrowAltRight } from "react-icons/fa";

const Base = () => {
  const faqs = [
    {
      question: 'What is your return policy?',
      answer: 'You can return any item within 30 days of purchase.',
    },
    {
      question: 'How long does shipping take?',
      answer: 'Shipping usually takes 5-7 business days.',
    },
    {
      question: 'What is your return policy?',
      answer: 'You can return any item within 30 days of purchase.',
    },
    {
      question: 'How long does shipping take?',
      answer: 'Shipping usually takes 5-7 business days.',
    },
    {
      question: 'What is your return policy?',
      answer: 'You can return any item within 30 days of purchase.',
    },
    {
      question: 'How long does shipping take?',
      answer: 'Shipping usually takes 5-7 business days.',
    },
    {
      question: 'What is your return policy?',
      answer: 'You can return any item within 30 days of purchase.',
    },
    {
      question: 'How long does shipping take?',
      answer: 'Shipping usually takes 5-7 business days.',
    },
  ];

  const [openIndex, setOpenIndex] = useState(null);

  const toggleFAQ = (index) => {
    setOpenIndex(openIndex === index ? null : index);
  };

  return (
    <div className="min-h-screen bg-gray-50 px-4 py-8">
      <div className='flex justify-center items-center'>
        <h1 className='text-3xl font-bold text-gray-800 mb-10'>FREQUENTLY ASKED QUESTIONS (FAQs)</h1>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-5xl mx-auto">
        {faqs.map((faq, index) => {
          const isOpen = openIndex === index;
          return (
            <div
              key={index}
              className="bg-white shadow-md rounded-lg p-5 transition duration-300 hover:shadow-xl cursor-pointer"
              onClick={() => toggleFAQ(index)}
            >
              <div className="flex justify-between items-center font-semibold text-gray-800">
                <h2>{faq.question}</h2>
                <span
                  className={`text-xl transition-transform duration-300 ${
                    isOpen ? 'rotate-45' : 'rotate-0'
                  }`}
                >
                  +
                </span>
              </div>
              {isOpen && (
                <div className="mt-3 text-gray-600 transition-all duration-300 ease-in-out">
                  {faq.answer}
                </div>
              )}
            </div>
          );
        })}
      </div>

      <div className="flex justify-center mt-10">
        <button className='flex items-center gap-2 border-2 border-gray-300 px-4 py-2 rounded-md text-sm font-semibold text-gray-800 hover:bg-gray-100 transition'>
          See all FAQs <FaLongArrowAltRight />
        </button>
      </div>
    </div>
  );
};

export default Base;
