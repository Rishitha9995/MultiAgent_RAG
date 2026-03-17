// const sendBtn = document.getElementById("sendBtn");
// const queryInput = document.getElementById("queryInput");
// const chatContainer = document.getElementById("chatContainer");

// sendBtn.addEventListener("click", async () => {
//     const query = queryInput.value.trim();
//     if (!query) return;

//     // Show user message
//     const userMsgDiv = document.createElement("div");
//     userMsgDiv.className = "chat-message user-message";
//     userMsgDiv.textContent = query;
//     chatContainer.appendChild(userMsgDiv);

//     // Reset input
//     queryInput.value = "";

//     // Show AI loading
//     const aiMsgDiv = document.createElement("div");
//     aiMsgDiv.className = "chat-message ai-message";
//     aiMsgDiv.textContent = "Thinking...";
//     chatContainer.appendChild(aiMsgDiv);

//     try {
//         const response = await fetch("http://127.0.0.1:8000/ask", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({ query: query, dataset: "business" })
//         });

//         if (!response.ok) throw new Error("Failed to fetch response");

//         const data = await response.json();

//         // Build AI message content
//         let content = `<h4>Auto-Corrected Query:</h4><p>${data.corrected_query}</p>`;
//         content += `<h4>Answer:</h4><ul>`;
//         if (data.answer) {
//             data.answer.split("•").forEach(item => {
//                 if (item.trim()) content += `<li>${item.trim()}</li>`;
//             });
//         }
//         content += `</ul>`;

//         if (data.documents && data.documents.length) {
//             content += `<h4>Top Documents:</h4><ul>`;
//             data.documents.forEach(doc => {
//                 if (typeof doc === "string") {
//                     content += `<li>${doc}</li>`;
//                 } else {
//                     content += `<li><strong>${doc.name}</strong> (Score: ${doc.similarity_score?.toFixed(3)}) - ${doc.reason}</li>`;
//                 }
//             });
//             content += `</ul>`;
//         }

//         if (data.metrics) {
//             content += `<h4>RAG Metrics:</h4><ul>`;
//             Object.entries(data.metrics).forEach(([key, val]) => {
//                 content += `<li>${key}: ${val}</li>`;
//             });
//             content += `</ul>`;
//         }

//         aiMsgDiv.innerHTML = content;
//         chatContainer.scrollTop = chatContainer.scrollHeight;

//     } catch (err) {
//         console.error(err);
//         aiMsgDiv.textContent = "Error fetching response. Please check backend server.";
//     }
// });
const sendBtn = document.getElementById("sendBtn");
const queryInput = document.getElementById("queryInput");
const chatContainer = document.getElementById("chatContainer");

sendBtn.addEventListener("click", async () => {
    const query = queryInput.value.trim();
    if (!query) return;

    // Show user message
    const userMsgDiv = document.createElement("div");
    userMsgDiv.className = "chat-message user-message";
    userMsgDiv.textContent = query;
    chatContainer.appendChild(userMsgDiv);

    queryInput.value = "";

    // Show AI loading
    const aiMsgDiv = document.createElement("div");
    aiMsgDiv.className = "chat-message ai-message";
    aiMsgDiv.textContent = "Thinking...";
    chatContainer.appendChild(aiMsgDiv);

    try {
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: query, dataset: "business" })
        });

        if (!response.ok) throw new Error("Failed to fetch response");
        const data = await response.json();

        // Clear "Thinking..."
        aiMsgDiv.innerHTML = "";

        // Auto-Corrected Query Card
        const correctedCard = document.createElement("div");
        correctedCard.className = "section-card";
        correctedCard.innerHTML = `<h4>Auto-Corrected Query</h4><p>${data.corrected_query}</p>`;
        aiMsgDiv.appendChild(correctedCard);

        // Answer Card
        const answerCard = document.createElement("div");
        answerCard.className = "section-card";
        let answerHTML = `<h4>Answer</h4><ul>`;
        if (data.answer) {
            data.answer.split("•").forEach(item => {
                if (item.trim()) answerHTML += `<li>${item.trim()}</li>`;
            });
        }
        answerHTML += `</ul>`;
        answerCard.innerHTML = answerHTML;
        aiMsgDiv.appendChild(answerCard);

        // Documents Card
        if (data.documents && data.documents.length) {
            const docCard = document.createElement("div");
            docCard.className = "section-card";
            let docHTML = `<h4>Top Retrieved Documents</h4><ul>`;
            data.documents.forEach(doc => {
                if (typeof doc === "string") docHTML += `<li>${doc}</li>`;
                else docHTML += `<li><strong>${doc.name}</strong> (Score: ${doc.similarity_score?.toFixed(3)}) - ${doc.reason}</li>`;
            });
            docHTML += `</ul>`;
            docCard.innerHTML = docHTML;
            aiMsgDiv.appendChild(docCard);
        }

        // Metrics Card
        if (data.metrics) {
            const metricsCard = document.createElement("div");
            metricsCard.className = "section-card";
            let metricsHTML = `<h4>RAG Metrics</h4><ul>`;
            Object.entries(data.metrics).forEach(([key, val]) => {
                metricsHTML += `<li>${key}: ${val}</li>`;
            });
            metricsHTML += `</ul>`;
            metricsCard.innerHTML = metricsHTML;
            aiMsgDiv.appendChild(metricsCard);
        }

        chatContainer.scrollTop = chatContainer.scrollHeight;

    } catch (err) {
        console.error(err);
        aiMsgDiv.textContent = "Error fetching response. Please check backend server.";
    }
});