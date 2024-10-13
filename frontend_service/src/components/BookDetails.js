import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getBookById } from '../services/bookService';

function BookDetails() {
  const { id } = useParams();
  const [book, setBook] = useState(null);

  useEffect(() => {
    const fetchBook = async () => {
      const data = await getBookById(id);
      setBook(data);
    };
    fetchBook();
  }, [id]);

  if (!book) return <p>Loading...</p>;

  return (
    <div>
      <h1>{book.title}</h1>
      <p>{book.description}</p>
    </div>
  );
}

export default BookDetails;
