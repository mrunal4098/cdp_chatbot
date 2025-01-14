# cdp_chatbot
Support Agent Chatbot for CDP

Project Overview

The Support Agent Chatbot for Customer Data Platforms (CDPs) is a web-based application that provides answers to "how-to" questions about the following CDPs:

Segment

mParticle

Lytics

Zeotap

The chatbot retrieves relevant information from official documentation to guide users on how to perform tasks or achieve specific outcomes within each platform.

Key Features

Core Functionalities

Answer "How-to" Questions

Examples:

"How do I set up a new source in Segment?"

"How can I create a user profile in mParticle?"

"How do I build an audience segment in Lytics?"

"How can I integrate my data with Zeotap?"

Extract Information from Documentation

The chatbot retrieves precise information from the official documentation of the four CDPs.

Identifies relevant sections and extracts the necessary instructions or steps.

Handle Variations in Questions

Supports questions with varying lengths and phrasing.

Handles irrelevant questions (e.g., "Which movie is releasing this week?") and provides appropriate responses.

Bonus Features

Cross-CDP Comparisons

Example query: "How does Segment's audience creation process compare to Lytics'?"

Provides side-by-side comparisons of features or functionalities across multiple CDPs.

Advanced "How-to" Questions

Handles complex or platform-specific queries such as:

"How do I configure identity resolution in Zeotap?"

"How do I set up real-time streaming in Lytics?"

User Feedback System

Allows users to rate responses and provide feedback, aiding continuous improvement.

Project Structure

cdp_chatbot
├── backend
│    ├── app.py               # FastAPI backend
│    ├── scraper.py           # Documentation scraper (optional)
│    ├── indexer.py           # Indexing and search logic
│    ├── requirements.txt     # Backend dependencies
│    └── data
│         └── cdp_docs.json   # Knowledge base with indexed docs
│
└── frontend
     ├── package.json         # Frontend dependencies
     ├── src
     │    ├── App.js          # React frontend logic
     │    └── index.js        # React entry point
     └── public
          └── index.html      # Frontend HTML

Setup Instructions

1. Backend Setup

Navigate to the backend/ directory:

cd cdp_chatbot/backend

Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate   # For Windows: .\venv\Scripts\activate
pip install -r requirements.txt

Start the backend server:

uvicorn app:app --reload

Test the backend:

Open a browser and navigate to http://127.0.0.1:8000.

Use tools like Postman or curl to test the /query endpoint.

Example:

curl -X POST -H "Content-Type: application/json" \
-d '{"question": "How do I set up a new source in Segment?"}' \
http://127.0.0.1:8000/query

2. Frontend Setup

Navigate to the frontend/ directory:

cd cdp_chatbot/frontend

Install frontend dependencies:

npm install

Start the frontend:

npm start

Open the application in your browser at http://localhost:3000.

Deployment

Dockerization

Backend Dockerfile

# backend/Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

Frontend Dockerfile

# frontend/Dockerfile
FROM node:18-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80

Deployment Platforms

GitHub Actions: Set up CI/CD pipelines for automated builds and deployments.

Cloud Providers: Deploy the app using Docker containers on AWS, GCP, or Heroku.

Testing and Validation

Functionality Tests:

Test common "how-to" queries for all CDPs.

Validate responses for irrelevant questions.

Performance Tests:

Measure response time for various queries.

Test the chatbot with high concurrent usage.

UX Tests:

Verify the frontend’s usability and responsiveness.

Test cross-browser compatibility.

Non-Functional Features

Security:

Input validation to prevent malicious injections.

HTTPS configuration for secure communication in production.

Performance:

Fast response times with lightweight indexing.

Caching mechanisms for frequently asked questions (optional).

Scalability:

Dockerized deployment ensures the app can scale horizontally.

GitHub Repository

Provide your GitHub repository link here:
GitHub Repository Link

Screenshots

Include screenshots of:

The running chatbot in the frontend.

API responses from the backend (e.g., via Postman or curl).

Conclusion

This project demonstrates the ability to build a robust and scalable software solution to address "how-to" queries for CDPs. It integrates modular architecture, clean code, and deployment-ready practices to meet and exceed the assignment criteria.

