from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter



class ingest_data:
    
    def __init__(self):
        print("data ingestion class has init")

    def data_ingestion(self):
        pass

if __name__ == '__main__':
    data_ingestion = ingest_data()