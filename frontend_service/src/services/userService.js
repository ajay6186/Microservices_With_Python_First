import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const loginUser = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}/login`, { username, password });
    return response.data;
  } catch (error) {
    console.error('Login error', error);
    return null;
  }
};

export const registerUser = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}/register`, { username, password });
    return response.data;
  } catch (error) {
    console.error('Registration error', error);
    return null;
  }
};
