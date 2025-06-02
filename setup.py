from setuptools import setup

setup(
    name="e-commerce-bot",
    version="0.0.1",
    author="utkarsh",
    author_email="bizzboosterdata@gmail.com",
    packages=[
        "retriever",
        "templates",
        "data_ingestion",
        "prompt_library",
        "data_collection_pipeline",
        "utils"
    ],
    install_requires=[
        "langchain-astradb",
        "langchain"
    ],
)
