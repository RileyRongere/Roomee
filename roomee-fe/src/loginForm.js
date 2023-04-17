import React, { useState } from 'react';

const LoginForm = () => {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Submitted: ', inputValue);
  };

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  return (
    <div>
      <label htmlFor="username-email">Username or Email</label>
      <br />
      <input
        type="text"
        id="username-email"
        value={inputValue}
        onChange={handleChange}
      />
      <br />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default LoginForm;
