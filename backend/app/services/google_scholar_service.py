from tavily import TavilyClient
from typing import List, Dict

def search(query: str, max_results: int = 5) -> List[Dict]:
    tavily_client = TavilyClient(api_key="")
    result = tavily_client.search(query, max_results=max_results, search_depth="advanced")
    
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
