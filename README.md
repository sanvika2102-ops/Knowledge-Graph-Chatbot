# StudyGraph — Knowledge Graph Question Answering System

**Live Prototype:** [https://knowledge-graph-chatbot.onrender.com](https://knowledge-graph-chatbot.onrender.com)  
**Course:** Discrete Mathematics and Graph Theory — Experiential Learning Project  

---

## 1. Overview
**StudyGraph** is an interactive, web-based Question Answering (QA) chatbot built using **Graph Theory** and **Python (Flask)**[cite: 20, 23]. Instead of relying solely on unstructured keyword search, the system organizes Computer Science and Engineering (CSE) subjects and domains into a **labelled directed Knowledge Graph**[cite: 3, 5, 17, 19].

When a user asks a question in natural language, the system parses the intent, extracts target concepts (including common aliases), and traverses the graph—using direct edge lookups and **Breadth-First Search (BFS)**—to retrieve accurate, relationship-backed answers[cite: 19, 21, 22].

---

## 2. System Architecture
The prototype follows a three-tier architecture:
1. **User Interface (`templates/index.html`):** A responsive chat interface featuring domain filters, color-coded quick-prompt pills for all 7 supported question categories, and asynchronous Fetch API calls.
2. **Application & QA Engine (`app.py`, `question_processor.py`):** A Flask backend that exposes `/api/ask`, extracts canonical entities from user queries, classifies question intent, and executes graph queries or BFS shortest-path traversal[cite: 20, 21, 22].
3. **Knowledge Base & Data Layer (`knowledge_graph.py`):** Stores the formal mathematical graph $KG = (V, R, E)$ as a directed adjacency list alongside supplementary educational definitions, study roadmaps, and real-world examples[cite: 5, 21].

---

## 3. Mathematical Model & Graph Structure
The Knowledge Graph is formally defined as a labelled directed graph $KG = (V, R, E)$[cite: 5]:

* **Vertices ($\vert{}V\vert{} = 15$):**
  * **3 Major Domains:** `Mathematics`, `Software`, `Hardware`[cite: 6]
  * **12 CSE Subjects:** `Probability`, `Linear Algebra`, `Discrete Mathematics`, `Programming in C`, `Data Structures`, `Algorithms`, `Machine Learning`, `DBMS`, `Operating Systems`, `Computer Networks`, `Digital Logic`, `Computer Architecture`[cite: 6]
* **Relation Labels ($\vert{}R\vert{} = 2$):**
  * `prerequisite_of`: Represents learning dependencies between subjects (forms a Directed Acyclic Graph / DAG)[cite: 5, 12].
  * `belongs_to`: Maps each subject to its parent academic domain[cite: 12].
* **Directed Edges ($\vert{}E\vert{} = 23$):**
  * **11 Prerequisite Edges** (e.g., `Programming in C → Data Structures → Algorithms → Machine Learning`)[cite: 6, 7, 10]
  * **12 Domain Membership Edges** (e.g., `Probability → Mathematics`, `Digital Logic → Hardware`)[cite: 7]
* **Graph Properties:**
  * $\sum d^+(v) = \sum d^-(v) = 23 = \vert{}E\vert{}$ (satisfies the directed handshaking theorem)[cite: 9, 15].
  * `Data Structures` has the highest subject out-degree ($d^+ = 5$)[cite: 8, 16].
  * `Machine Learning` has the highest subject prerequisite in-degree ($d^- = 3$)[cite: 9, 16].

---

## 4. Supported Question Categories
The chatbot supports **7 distinct question types**, combining strict Knowledge Graph traversal with structured educational explanations:

| Category | Source | Example Query |
| :--- | :--- | :--- |
| **1. Definition** | Educational Content + Graph Domain | *"What is Machine Learning?"* |
| **2. Preparation** | Graph Prerequisites + Study Roadmap | *"How to prepare for Machine Learning?"* |
| **3. Prerequisites** | Knowledge Graph (`prerequisite_of`) | *"What are the prerequisites of Algorithms?"* |
| **4. Related Topics** | Knowledge Graph (Incoming, Outgoing & Sibling Edges) | *"What topics are related to Data Structures?"* |
| **5. Domain** | Knowledge Graph (`belongs_to`) | *"Which domain does Digital Logic belong to?"* |
| **6. Path (BFS)** | Knowledge Graph (Breadth-First Search) | *"Find the path from Programming in C to Machine Learning"* |
| **7. Examples** | Educational Content | *"Give practical examples of DBMS"* |

---

## 5. Project Structure
```text
Knowledge-Graph-Chatbot/
├── app.py                   # Flask web server and REST API endpoints (/api/ask, /api/health)
├── knowledge_graph.py       # 15 vertices, 23 edges, aliases, BFS algorithm & educational content
├── question_processor.py    # Regex entity extraction, intent classification & response formatting
├── templates/
│   └── index.html           # Interactive frontend UI with quick-test category pills
├── requirements.txt         # Python dependencies (Flask, gunicorn)
├── .gitignore               # Excludes .venv and __pycache__
└── README.md                # Project documentation
