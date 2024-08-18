import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const searchPapers = async (query, maxResults, source) => {
  try {
    const response = await axios.post(`${API_URL}/search`, {
      query,
      max_results: maxResults,
      source
    });
    return response.data;
  } catch (error) {
    console.error('Error searching papers:', error);
    throw error;
  }
};
