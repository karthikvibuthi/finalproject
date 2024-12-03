JobHelper: Intelligent Resume Analysis and Job Recommendations
JobHelper is a robust, Flask-based web application designed to streamline job searches, improve resumes, and recommend networking events. The project uses cutting-edge natural language processing (NLP) techniques and machine learning models to analyze resumes, recommend jobs, and provide actionable feedback.

📜 Table of Contents
Problem Statement
Features
Project Architecture
Setup and Installation
Usage Instructions
Screenshots
Future Directions
License
🔍 Problem Statement
The growing volume of resumes and job listings makes it challenging for job seekers to tailor resumes effectively and find suitable opportunities. Manual evaluation is time-consuming and error-prone. This project addresses these challenges by providing:

Automated Resume Scoring
Job and Event Recommendations using NLP and Semantic Similarity
A User-Friendly Interface for seamless interaction.
🌟 Features
Resume Analysis
Resume Scoring: Evaluates resumes based on structure, spelling, impactful words, and more.
Feedback: Provides actionable suggestions to enhance resumes.
Job and Event Recommendations
Job Recommendations: Uses sentence-transformer models to calculate cosine similarity between resumes and job listings.
Event Recommendations: Matches user profiles with networking events tailored to career interests.
Interactive UI
File upload functionality for resume analysis.
Dynamic tables for sorting and filtering job and event recommendations.
Match scores displayed for better visualization of relevance.
🏗️ Project Architecture
Backend:

Framework: Flask
Gunicorn for handling HTTP requests
Python libraries: SpaCy, NLTK, Sentence-Transformers, Selenium, Pandas
Frontend:

HTML/CSS with Bootstrap for responsive design
JavaScript for dynamic interactivity
Data:

Scraped job listings and events stored as CSV files
NLP preprocessing using SpaCy and regex for parsing resumes
Deployment:

Hosted on Amazon Lightsail
Systemd service to ensure the app restarts on instance reboot.
⚙️ Setup and Installation
Prerequisites
Python 3.8+
Google Chrome and Chromedriver for Selenium
An active Amazon Lightsail instance
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/karthikvibuthi/finalproject.git
cd JobHelper
Set up the virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Set up logging and ensure all directories are accessible:

bash
Copy code
mkdir logs
Update scraping scripts:

Ensure your job and event scraping scripts are scheduled using a systemd service. Follow this guide for details.
Start the application:

bash
Copy code
gunicorn -w 4 app:app
🛠️ Usage Instructions
Access the application at http://3.229.200.133:5001in your browser.
Upload a resume in PDF format for analysis.
View:
Resume Score with detailed breakdown
Personalized Job Recommendations
Tailored Event Suggestions
🖼️ Screenshots
Upload Resume

Resume Score

Job Recommendations

🔮 Future Directions
Enhanced Storage:

Transition from CSV files to MongoDB for scalability.
Integrate data pipelines for real-time updates.
API Integration:

Use the Handshake API for dynamic job and event data.
Advanced NLP:

Leverage fine-tuned BERT models for improved resume parsing and matching.
Mobile App:
