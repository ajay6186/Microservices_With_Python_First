import axios from 'axios';

const API_URL = 'http://localhost:5001/api';  // Replace with your actual service URL

export const getBooks = async () => {
  try {
    const response = await axios.get(`${API_URL}/books`);
    return response.data;
  } catch (error) {
    console.error('Error fetching books:', error);
    return [];
  }
};

export const getBookById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/books/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching book:', error);
    return null;
  }
};
