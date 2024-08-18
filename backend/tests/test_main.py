import requests
from bs4 import BeautifulSoup

def search(query, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    search_query = f"search_query=all:{query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    response = requests.get(base_url + search_query)
    soup = BeautifulSoup(response.content, 'xml')

    papers = []
    for entry in soup.find_all('entry'):
        title = entry.title.text
        abstract = entry.summary.text
        authors = [author.name.text for author in entry.find_all('author')]
        published = entry.published.text
        papers.append({
            'title': title,
            'abstract': abstract,
            'authors': authors,
            'published': published
        })
    return papers