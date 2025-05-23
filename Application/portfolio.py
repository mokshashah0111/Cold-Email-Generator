import pandas as pd
import chromadb
import uuid

class portfolio:
    def __init__(self, file_path = "C:\Code\Cold Email Generator-tool\Application\Resources\my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name = "portfolio")

        def load_portfolio(self):
            if not self.collection.count():
                for _, row in self.data.iterrrows():
                    self.collection.add(documents = row["Techstack"],
                                        metadata = {"links" : row["links"]},
                                        ids = [str(uuid.uuid4())])
        
        def query_links(self,skills):
            return self.collection.query(query_text = skills, n_result = 2).get('metadata',[])