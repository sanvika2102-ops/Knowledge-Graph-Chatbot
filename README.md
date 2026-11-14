# StudyGraph — Knowledge Graph Question Answering Prototype

A small educational chatbot prototype using a predefined directed knowledge graph, rule-based question processing, and BFS path search.

## Requirements
- Python 3.9 or newer
- Flask

## Run on Windows

1. Open this folder in VS Code.
2. Open Terminal in VS Code.
3. (Recommended) Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```powershell
   py -m pip install -r requirements.txt
   ```

5. Start the app:

   ```powershell
   py app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## Example questions
- What are the prerequisites of Machine Learning?
- Which topics belong to Mathematics?
- What can I learn after Data Structures?
- Find the path from Programming in C to Machine Learning.
- Tell me about Operating Systems.

## Project note
This version is a rule-based prototype. It does not use a large language model or understand arbitrary questions. It recognizes supported topics and question patterns, then retrieves information from the graph. This distinction should be stated accurately in the project report and presentation.

## Graph data
The graph contains 15 vertices and 23 directed labelled edges, following the project graph:
- 11 `prerequisite_of` relationships
- 12 `belongs_to` relationships
