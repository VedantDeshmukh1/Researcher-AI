import React from 'react';
import PaperCard from './PaperCard';

const PaperList = ({ papers }) => {
  return (
    <div className="paper-list">
      {papers.map((paper, index) => (
        <PaperCard 
          key={index} 
          paper={paper}
        />
      ))}
    </div>
  );
};

export default PaperList;