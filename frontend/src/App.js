import React, { useState } from 'react';
import SearchForm from './components/SearchForm';
import PaperList from './components/PaperList';
import './App.css';

export function App() {
  const [searchResults, setSearchResults] = useState([]);

  const handleSearchResults = (results) => {
    setSearchResults(results);
  };

  return (
    <div className="App">
      <h1>Research Paper Search</h1>
      <SearchForm onSearchResults={handleSearchResults} />
      <PaperList papers={searchResults} />
    </div>
  );
}