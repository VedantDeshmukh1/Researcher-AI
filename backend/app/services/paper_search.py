import arxiv
from scholarly import scholarly

def search_arxiv(query, max_results):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = []
    for paper in search.results():
        results.append({
            'title': paper.title,
            'abstract': paper.summary,
            'url': paper.pdf_url,
            'authors': [author.name for author in paper.authors],
            'published': paper.published.strftime("%Y-%m-%d")
        })
    return results

def search_google_scholar(query, max_results):
    search_query = scholarly.search_pubs(query)
    results = []
    for i in range(max_results):
        try:
            paper = next(search_query)
            results.append({
                'title': paper['bib']['title'],
                'abstract': paper.get('bib', {}).get('abstract', 'No abstract available'),
                'url': paper.get('pub_url', ''),
                'authors': paper['bib'].get('author', []),
                'published': paper['bib'].get('pub_year', 'Unknown')
            })
        except StopIteration:
            break
    return results

def search(query, max_results, source):
    if source.lower() == 'arxiv':
        return search_arxiv(query, max_results)
    elif source.lower() == 'google_scholar':
        return search_google_scholar(query, max_results)
    else:
        raise ValueError("Invalid source. Choose 'arxiv' or 'google_scholar'.")