# SouL_Law_Case_Search

## Legal Case Law Search

This repository contains the source code for the **Legal Case Law Search Platform**, which allows users to search for legal case laws from different countries (USA, India, Canada) based on a variety of criteria.

The backend is built with **FastAPI**, utilizing **Elasticsearch** for storing and searching legal case data. The frontend is a simple HTML page that allows users to enter search queries and filter results by country.

## Project Structure

### Frontend
- **index.html**: The main HTML page that provides the search interface for users.
- **styles.css**: The CSS file to style the frontend interface.

### Backend
- **main.py**: FastAPI backend that provides an API endpoint (`/cases/`) to search for cases from Elasticsearch.
- **data_loader.py**: A script to populate the Elasticsearch index with mock legal case data.

### Elasticsearch
Elasticsearch is used to store and search case data, which is indexed by country and case fields like title, summary, and legal topics.

## Features
- **Search by Keyword**: Allows users to search for cases based on keywords in the case title, summary, or legal topics.
- **Country Filter**: Users can filter the results based on the country (USA, India, Canada).
- **View Case Details**: Each result includes a link to the full case information.
- **Display Ratings**: Cases are displayed with a default rating (for example, 4/5).

## Setup

### Prerequisites
- **Elasticsearch**: You need to have an instance of Elasticsearch running locally. You can follow the official Elasticsearch installation guide.
- **Python Dependencies**: The backend is built using Python and requires the following packages:
  - FastAPI
  - Elasticsearch
  - Uvicorn (for serving the app)

To install these dependencies, run the following command:

```bash
pip install fastapi[all] elasticsearch uvicorn


## Running the Project

To get the project up and running, follow these steps:

### 1. **Start Elasticsearch**

You need to have an Elasticsearch instance running locally or remotely. The easiest way to do this is by using Docker. Run the following command to start Elasticsearch:

```bash
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.8.1

