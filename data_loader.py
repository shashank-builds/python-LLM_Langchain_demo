import requests
import xml.etree.ElementTree
import scholarly

print("ok")

class DataLoader():

    def fetch_archive_paper(self,query):
        def search_archive(query):
             pass




        url = f"http://export.arxiv.org/api/query?search_query={query}"
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            papers = []
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
                link = entry.find('{http://www.w3.org/2005/Atom}link').attrib['href']
                papers.append({'title': title, 'summary': summary, 'link': link})
            return papers
        else:
            return []
        
    def fetch_google_scholar_paper(self,query):
            search_results = scholarly.search_pubs(query)
            papers = []
            for result in search_results:
                papers.append(result)
                if len(papers) >= 5:
                    break
            return papers