import React, { useState } from 'react';
import { searchPapers } from '../services/api';

const SearchForm = ({ onSearchResults }) => {
  const [query, setQuery] = useState('');
  const [maxResults, setMaxResults] = useState(10);
  const [source, setSource] = useState('arxiv');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const results = await searchPapers(query, maxResults, source);
      onSearchResults(results);
    } catch (error) {
      console.error('Error searching papers:', error);
      onSearchResults([]);
    }
    setIsLoading(false);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter search query"
        required
      />
      <input
        type="number"
        value={maxResults}
        onChange={(e) => setMaxResults(parseInt(e.target.value))}
        min="1"
        max="50"
      />
      <select value={source} onChange={(e) => setSource(e.target.value)}>
        <option value="arxiv">arXiv</option>
        <option value="scholar">Google Scholar</option>
      </select>
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Searching...' : 'Search'}
      </button>
    </form>
  );
};

export default SearchForm;