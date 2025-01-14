import React, { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleAsk = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
      });
      const data = await response.json();
      setAnswer(data.answer);
    } catch (err) {
      console.error(err);
      setAnswer("Error connecting to the backend.");
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", fontFamily: "Arial" }}>
      <h1>CDP Chatbot</h1>
      <textarea
        rows={4}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question about Segment, mParticle, Lytics, or Zeotap..."
        style={{ width: "100%", padding: "10px" }}
      />
      <button onClick={handleAsk} style={{ marginTop: "10px", padding: "8px 16px" }}>
        Ask
      </button>

      {answer && (
        <div style={{ marginTop: "20px", whiteSpace: "pre-wrap" }}>
          <strong>Answer:</strong> 
          <div>{answer}</div>
        </div>
      )}
    </div>
  );
}

export default App;
