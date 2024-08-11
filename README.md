# RAG System with VectorDB

## Overview
This project tests and implements query functionality using a vector database with MongoDB. The project demonstrates how to perform efficient vector searches by integrating embeddings generated from text data with MongoDB's vector search capabilities. The goal is to explore and validate the performance and accuracy of vector searches within MongoDB.

## Features
- **Vector Embeddings:** Converts text data into vector embeddings using a pre-trained language model (gte-large)
- **MongoDB Integration:** Stores and retrieves vector embeddings in MongoDB.
- **Vector Search:** Performs vector similarity searches in MongoDB to find the most relevant results based on a query.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Khim3/Rag_with_VectorDB.git
    ```

2. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up MongoDB:**
    - Ensure you have access to a MongoDB instance, either locally or through a cloud service like MongoDB Atlas.
     ```
     import pymongo

     def connect_mongodb(mongo_uri):
      try:
          client = pymongo.MongoClient(mongo_uri, appname='vector_search_app')
          print("Connected to MongoDB")
          return client
      except pymongo.errors.ConnectionFailure as e:
          print("Could not connect to MongoDB: %s" % e)
          return None
      
      mongo_uri = 'your-mongo-uri-here'
      client = connect_mongodb(mongo_uri)
     ```
     - Once connected, you can create a new database and collection to store your vector embeddings:
       ```
       db = client['vector_search_db']
       collection = db['vector_embeddings']
       ```
     - Set up index search for database
       ```
        index_spec = {
                  "vector": {
                      "key": "embedding",
                      "dimensions": 768,  # Example dimension size, replace with your actual embedding size
                      "metric": "cosine"  # Similarity function; options include 'cosine', 'euclidean', etc.
                  }
              }
       ```
      
## Usage

1. **Prepare the input data:**
    - Input text data that will be converted into vector embeddings.

2. **Generate vector embeddings:**
    - Use the provided Python scripts to convert your text data into embeddings using a pre-trained language model.
      ```
      def get_embedding(text: str) -> list[float]:
          if text is None or not text.strip():
          #    print('No text found')
              return []
          embedding = model.encode(text)
          return embedding.tolist()
      ```

3. **Insert embeddings into MongoDB:**
    - Store the generated embeddings in a MongoDB collection.
    ```
    client['movies']['movies_collection'].insert_many(df.to_dict('records'))
    ```
4. **Perform vector search:**
    ```python
    query = "Your query text"
    results = vector_search(query, collection)
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Score: {result['score']}")
        print(f"Plot: {result['fullplot']}\n")
    ```
## Requirements
- Python 3.8+
- MongoDB (local or cloud)
- Python packages: `pymongo`, `transformers`, `torch`,... (check requirements.txt for further info).

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.


## Acknowledgments
- Special thanks to the [Hugging Face](https://huggingface.co) team for providing the transformer models.

## Contact
If you have any questions, feel free to reach out at nhatkhiem003@gmail.com
