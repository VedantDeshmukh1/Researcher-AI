import React from 'react';

const PaperCard = ({ paper }) => {
  return (
    <div className="paper-card">
      <h2>{paper.title}</h2>
      <p>Authors: {paper.authors.join(', ')}</p>
      <p>Published: {paper.published}</p>
      <p>{paper.abstract}</p>
      {paper.url && <a href={paper.url} target="_blank" rel="noopener noreferrer">Read More</a>}
    </div>
  );
};

export default PaperCard;