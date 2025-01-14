# indexer.py
import json
import re
import os

class CDPIndexer:
    def __init__(self, data_file="data/cdp_docs.json"):
        base_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_path, data_file)
        with open(data_path, "r", encoding="utf-8") as f:
            self.docs = json.load(f)

    def search(self, query):
        """
        Very basic keyword matching:
        1. Convert query to lowercase
        2. Score documents by counting how many query words appear
        """
        query_words = re.findall(r'\w+', query.lower())
        results = []

        for doc in self.docs:
            content_lower = doc["content"].lower()
            # simple sum of occurrences
            score = sum(content_lower.count(qw) for qw in query_words)
            if score > 0:
                results.append((score, doc))

        # Sort by highest score (descending)
        results.sort(key=lambda x: x[0], reverse=True)

        # return top 3 for brevity
        top_results = [doc for _, doc in results[:3]]
        return top_results
