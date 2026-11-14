const form = document.getElementById("chat-form");
const input = document.getElementById("question-input");
const messages = document.getElementById("chat-messages");
const sendButton = document.getElementById("send-button");

function addMessage(text, sender) {
  const row = document.createElement("div");
  row.className = `message ${sender}`;

  const avatar = document.createElement("div");
  avatar.className = "avatar";
  avatar.textContent = sender === "user" ? "YOU" : "KG";

  const bubble = document.createElement("div");
  bubble.className = "bubble";

  // textContent prevents user-entered text from being interpreted as HTML.
  const paragraph = document.createElement("p");
  paragraph.textContent = text;
  bubble.appendChild(paragraph);

  row.appendChild(avatar);
  row.appendChild(bubble);
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
}

async function sendQuestion(question) {
  addMessage(question, "user");
  sendButton.disabled = true;
  sendButton.textContent = "Thinking...";

  try {
    const response = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.answer || "Request failed.");
    addMessage(data.answer, "assistant");
  } catch (error) {
    addMessage("Sorry, I couldn't connect to the Python backend. Check that Flask is running and try again.", "assistant");
    console.error(error);
  } finally {
    sendButton.disabled = false;
    sendButton.innerHTML = 'Send <span aria-hidden="true">➤</span>';
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const question = input.value.trim();
  if (!question) return;
  input.value = "";
  sendQuestion(question);
});

document.querySelectorAll(".topic-chip").forEach((button) => {
  button.addEventListener("click", () => {
    const question = button.dataset.question;
    sendQuestion(question);
  });
});
