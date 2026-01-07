# NLP Customer Support Chatbot

This project is a simple NLP-based customer support chatbot built using Python and Flask.
The chatbot uses intent classification to understand user messages and respond with predefined answers.

It provides both a REST API and a web-based chat interface.

---

## Features
- NLP intent classification using scikit-learn
- Flask REST API
- Web-based chat interface
- Health check endpoint
- Virtual environment and dependency management

---

## Project Structure
nlp-chatbot/
├── app.py
├── nlp_model.py
├── intents.json
├── requirements.txt
├── .gitignore
└── templates/
└── index.html

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/nlp-customer-support-chatbot.git
cd nlp-customer-support-chatbot
```
### 2. Create and activate virtual environment
```bash
python -m venv venv
```
```bash
Windows: venv\Scripts\activate
```
```bash

Mac/Linux: source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application
```bash
python app.py
```
## Usage
Open your browser and go to:
http://127.0.0.1:5000

## Technologies Used

Python

Flask

scikit-learn

HTML, CSS, JavaScript

## Author

Maureen Chepkirui