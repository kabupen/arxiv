import arxiv
from deep_translator import GoogleTranslator

if __name__ == "__main__" : 
    search = arxiv.Search(
                query = "cs.CV AND submittedDate:[20211207 TO 20211208]",
                max_results = 3,
                sort_by = arxiv.SortCriterion.SubmittedDate,
                sort_order = arxiv.SortOrder.Descending
                )
   
    google = GoogleTranslator(source='auto', target='ja')
    for rs in search.results():

        title_ja = google.translate(rs.title) 
        summary_ja = google.translate(rs.summary.replace('\n', ''))

        print(rs.title)
        print(title_ja, '\n')
        print(summary_ja)
        print(rs.pdf_url)
        print('-'*50)
        print("\n")
                

