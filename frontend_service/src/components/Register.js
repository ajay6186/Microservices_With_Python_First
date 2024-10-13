import React, { useState } from 'react';
import { registerUser } from '../services/userService';

function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    const response = await registerUser(username, password);
    if (response) {
      alert('User registered successfully');
    } else {
      alert('Error registering user');
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Register</button>
    </form>
  );
}

export default Register;
