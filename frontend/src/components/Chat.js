import React, { useState } from "react";
import axios from "axios";
import Message from "./Message";

function Chat({ setMetrics }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;

    const text = input;

    // user message
    setMessages(prev => [...prev, { type: "user", text }]);
    setInput("");

    // loading message
    setMessages(prev => [...prev, { type: "ai", loading: true }]);

    try {
      const res = await axios.post("http://127.0.0.1:8000/ask", {
        query: text,
        dataset: "business"
      });

      const data = res.data;

      setMessages(prev => [
        ...prev.slice(0, -1),
        {
          type: "ai",
          corrected_query: data.corrected_query,
          answer: data.answer,
          explanations: data.explanations,
          metrics: data.metrics,
          response_time: data.response_time
        }
      ]);

      setMetrics(data);

    } catch {
      setMessages(prev => [
        ...prev.slice(0, -1),
        { type: "ai", text: "Server error" }
      ]);
    }
  };

  return (
    <div className="card">
      <h2>Chat</h2>

      <div className="chat-box">
        {messages.map((msg, i) => (
          <Message key={i} msg={msg} />
        ))}
      </div>

      <div className="input-row">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Ask your question..."
        />
        <button onClick={sendMessage}>→</button>
      </div>
    </div>
  );
}

export default Chat;