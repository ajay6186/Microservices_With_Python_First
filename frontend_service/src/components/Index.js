import React, { useEffect, useState } from 'react';
import { getBooks } from '../services/bookService';
import { Link } from 'react-router-dom';

function Index() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const fetchBooks = async () => {
      const data = await getBooks();
      setBooks(data);
    };
    fetchBooks();
  }, []);

  return (
    <div>
      <h1>Book List</h1>
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            <Link to={`/books/${book.id}`}>{book.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Index;
