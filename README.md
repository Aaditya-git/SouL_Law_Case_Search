# SouL_Law_Case_Search
Legal Case Law Search
This repository contains the source code for the Legal Case Law Search Platform that allows users to search for legal case laws from different countries (USA, India, Canada) based on a variety of criteria.

The backend is built with FastAPI, utilizing Elasticsearch for storing and searching legal case data. The frontend is a simple HTML page that allows users to enter search queries and filter results by country.

Project Structure
Frontend

index.html: The main HTML page that provides the search interface for users.
styles.css: The CSS file to style the frontend interface.
Backend

main.py: FastAPI backend which provides an API endpoint (/cases/) to search for cases from Elasticsearch.
data_loader.py: A script to populate the Elasticsearch index with mock legal case data.
Elasticsearch

Elasticsearch is used to store and search case data, which is indexed by country and case fields like title, summary, and legal topics.


Legal Case Law Search
This repository contains the source code for the Legal Case Law Search Platform that allows users to search for legal case laws from different countries (USA, India, Canada) based on a variety of criteria.

The backend is built with FastAPI, utilizing Elasticsearch for storing and searching legal case data. The frontend is a simple HTML page that allows users to enter search queries and filter results by country.

Project Structure
Frontend

index.html: The main HTML page that provides the search interface for users.
styles.css: The CSS file to style the frontend interface.
Backend

main.py: FastAPI backend which provides an API endpoint (/cases/) to search for cases from Elasticsearch.
data_loader.py: A script to populate the Elasticsearch index with mock legal case data.
Elasticsearch

Elasticsearch is used to store and search case data, which is indexed by country and case fields like title, summary, and legal topics.

Features
Search by Keyword: Allows users to search for cases based on keywords in the case title, summary, or legal topics.
Country Filter: Users can filter the results based on the country (USA, India, Canada).
View Case Details: Each result includes a link to the full case information.
Display Ratings: Cases are displayed with a default rating (for example, 4/5).



Setup
Prerequisites
Install Elasticsearch: You need to have an instance of Elasticsearch running locally. You can follow the official Elasticsearch installation guide.

Install Python Dependencies: The backend is built using Python and requires the following packages:

FastAPI
Elasticsearch
Uvicorn (for serving the app)
To install these dependencies, run the following:
pip install fastapi[all] elasticsearch uvicorn


Running the Project
1.Start Elasticsearch: Ensure Elasticsearch is running locally or remotely. You can start it using Docker:
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.8.1

2. Run the Backend: To start the FastAPI backend, run the following command:
uvicorn main:app --reload

3. python populate_fake_data.py
4. Open the Frontend: Open the index.html file in your browser to access the Legal Case Law Search interface.


Legal Case Law Search
This repository contains the source code for the Legal Case Law Search Platform that allows users to search for legal case laws from different countries (USA, India, Canada) based on a variety of criteria.

The backend is built with FastAPI, utilizing Elasticsearch for storing and searching legal case data. The frontend is a simple HTML page that allows users to enter search queries and filter results by country.

Project Structure
Frontend

index.html: The main HTML page that provides the search interface for users.
styles.css: The CSS file to style the frontend interface.
Backend

main.py: FastAPI backend which provides an API endpoint (/cases/) to search for cases from Elasticsearch.
data_loader.py: A script to populate the Elasticsearch index with mock legal case data.
Elasticsearch

Elasticsearch is used to store and search case data, which is indexed by country and case fields like title, summary, and legal topics.
Features
Search by Keyword: Allows users to search for cases based on keywords in the case title, summary, or legal topics.
Country Filter: Users can filter the results based on the country (USA, India, Canada).
View Case Details: Each result includes a link to the full case information.
Display Ratings: Cases are displayed with a default rating (for example, 4/5).
Setup
Prerequisites
Install Elasticsearch: You need to have an instance of Elasticsearch running locally. You can follow the official Elasticsearch installation guide.

Install Python Dependencies: The backend is built using Python and requires the following packages:

FastAPI
Elasticsearch
Uvicorn (for serving the app)
To install these dependencies, run the following:

bash
Copy code
pip install fastapi[all] elasticsearch uvicorn
Configure Elasticsearch: Update the connection details in the main.py and data_loader.py files to match your local Elasticsearch setup.

Running the Project
Start Elasticsearch: Ensure Elasticsearch is running locally or remotely. You can start it using Docker:

bash
Copy code
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.8.1
Run the Backend: To start the FastAPI backend, run the following command:

bash
Copy code
uvicorn main:app --reload
Populate Elasticsearch with Mock Data: To load mock data into Elasticsearch, run the data_loader.py script:

bash
Copy code
python data_loader.py
Open the Frontend: Open the index.html file in your browser to access the Legal Case Law Search interface.

API Endpoints
GET /cases/
Query Parameters:

query: The search query string for filtering case titles, summaries, or legal topics.
country (optional): Filter the results by country (USA, Canada, India).
Response: A JSON object containing an array of matching cases.



Acknowledgements
FastAPI for building the API.
Elasticsearch for efficient searching.

