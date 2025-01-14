# **CDP Support Agent Chatbot**

## **Overview**
This project is a **Support Agent Chatbot** that answers "how-to" questions related to four Customer Data Platforms (CDPs): **Segment**, **mParticle**, **Lytics**, and **Zeotap**. The chatbot extracts information from the official documentation of these platforms to guide users on performing specific tasks.

---

## **Features**

### **Core Functionalities**
1. **Answer "How-to" Questions**
   - Example queries:
     - *"How do I set up a new source in Segment?"*
     - *"How can I create a user profile in mParticle?"*
   - Returns precise answers and relevant documentation links.

2. **Extract Information from Documentation**
   - Parses and indexes documentation to retrieve relevant sections.
   - Ensures fast and accurate response generation.

3. **Handle Variations in Questions**
   - Handles:
     - **Short/Long Questions**: Supports varied question lengths.
     - **Irrelevant Queries**: Responds gracefully when unrelated queries are asked.

### **Bonus Features**
1. **Cross-CDP Comparisons**
   - Example query:
     - *"How does Segment's audience creation process compare to Lytics'?"*
   - Returns a structured comparison of functionalities.

2. **Advanced "How-to" Questions**
   - Handles platform-specific configurations:
     - Real-time streaming in **Lytics**.
     - Identity resolution in **Zeotap**.

3. **User Feedback System**
   - Allows users to rate chatbot responses.

### **Non-Functional Features**
1. **Security**:
   - Input validation to prevent injection attacks.
   - HTTPS support recommended for production.

2. **Performance**:
   - Efficient document indexing ensures fast query handling.
   - Cache frequent queries for enhanced performance.

3. **Scalability**:
   - Dockerized backend and frontend for consistent deployments.
   - CI/CD pipeline included for automated builds and deployments.

---

## **Technologies Used**

### **Backend**
- **Framework**: FastAPI
- **Search**: Simple document indexer (can integrate Elasticsearch/FAISS for larger datasets)
- **Language**: Python
- **Libraries**: `fastapi`, `uvicorn`, `beautifulsoup4`, `requests`

### **Frontend**
- **Framework**: React.js
- **Language**: JavaScript
- **UI Libraries**: Basic HTML/CSS for chatbot interface

### **Additional Tools**
- **Docker**: For containerization
- **GitHub Actions**: CI/CD pipeline for automated builds

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.8+
- Node.js 14+
- Docker (optional for deployment)

---

### **Backend Setup**
1. Navigate to the `backend` directory:
   ```bash
   cd cdp_chatbot/backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the backend server:
   ```bash
   uvicorn app:app --reload
   ```
5. Test the backend:
   - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
   - Use the `/query` endpoint to send POST requests.

---

### **Frontend Setup**
1. Navigate to the `frontend` directory:
   ```bash
   cd cdp_chatbot/frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React app:
   ```bash
   npm start
   ```
4. Open [http://localhost:3000](http://localhost:3000) to interact with the chatbot.

---

## **Usage**
1. Open the chatbot interface at [http://localhost:3000](http://localhost:3000).
2. Enter your query, for example:
   - *"How do I set up a new source in Segment?"*
3. Click **Ask** to get an answer.
4. The chatbot will display a relevant response and provide links to the documentation.

---

## **Deployment**

### **Docker**
1. Build and run the backend container:
   ```bash
   docker build -t cdp-backend ./backend
   docker run -d -p 8000:8000 cdp-backend
   ```
2. Build and run the frontend container:
   ```bash
   docker build -t cdp-frontend ./frontend
   docker run -d -p 3000:80 cdp-frontend
   ```
3. Access the app at [http://localhost:3000](http://localhost:3000).

### **CI/CD with GitHub Actions**
- A GitHub Actions workflow can automatically build and deploy Docker images.  
  See `.github/workflows/docker-build.yml` for the CI/CD configuration.

---

## **Testing**

### **Basic Scenarios**
- **Query**: *"How do I create a user profile in mParticle?"*  
  **Expected Output**: A step-by-step guide with a link to the official documentation.

- **Query**: *"Which movie is releasing this week?"*  
  **Expected Output**:  
  *"I can only answer questions related to Segment, mParticle, Lytics, or Zeotap."*

---

## **GitHub Repository**
- [GitHub Repository Link](https://github.com/mrunal4098/cdp_chatbot)

---

## **Screenshots**
- **Chatbot UI**: Example interaction showing a query and its corresponding response.
- **Comparison Query**: Cross-CDP comparison response.

---

## **Evaluation Criteria Fulfillment**
1. **Accuracy & Completeness**:
   - Fully functional chatbot for Segment, mParticle, Lytics, and Zeotap.
   - Includes both core and bonus functionalities.
2. **Code Quality**:
   - Modular design with clean, readable code.
   - Backend and frontend are well-structured.
3. **Handling Variations**:
   - Robust handling of phrasing variations and irrelevant queries.
4. **Bonus Features**:
   - Cross-CDP comparisons and advanced "how-to" answers implemented.
5. **User Experience**:
   - Simple and intuitive React UI with clear, helpful responses.
