import os
from tavily import TavilyClient
from bs4 import BeautifulSoup
import requests
from typing import List, Dict

def extract_text_from_urls(url_list):
    all_text = ""
    for url in url_list:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            page_text = soup.get_text(separator=' ', strip=True)
            all_text += page_text + "\n\n"
        except Exception as e:
            print(f"Error extracting text from {url}: {str(e)}")
    return all_text

def search(query: str, max_results: int = 5) -> List[Dict]:
    tavily_api_key = os.getenv('TAVILY_API_KEY')
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables")
    
    tavily_client = TavilyClient(api_key=tavily_api_key)
    result = tavily_client.search(query, max_results=max_results)
    
    papers = []
    for item in result['results']:
        paper = {
            'title': item.get('title', ''),
            'abstract': item.get('snippet', ''),
            'authors': [item.get('source', 'Unknown')],
            'published': item.get('published_date', ''),
            'url': item.get('url', '')
        }
        papers.append(paper)
    
    return papers