import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Index from './components/Index';
import Login from './components/Login';
import Register from './components/Register';
import BookDetails from './components/BookDetails';
import Basket from './components/Basket';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/books/:id" element={<BookDetails />} />
        <Route path="/basket" element={<Basket />} />
      </Routes>
    </Router>
  );
}

export default App;
