🚗 Vehicle Management System

A Vehicle Analysis & Management System built with Django and Machine Learning to track, analyze, and manage vehicle data efficiently.

This system allows users to store vehicle information, analyze data, and perform different operations related to vehicle management.

📌 Features

Add, update, delete, and view vehicle records

Analyze vehicle-related data

Machine learning integration for data insights

Organized Django project structure

Simple and clean interface

🛠️ Technologies Used

Python

Django

SQLite3

HTML

Machine Learning (Python-based models)

📁 Project Structure
Vehicles-Management-System/
│
├── config/              # Django project configuration
├── vehicles/            # Main app for vehicle logic
├── dummy_data/          # Sample data for testing
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
├── requirements.txt     # Project dependencies
└── README.md
⚙️ Installation & Setup Guide

Follow these steps to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/your-username/Vehicles-Management-System.git
cd Vehicles-Management-System
2️⃣ Create a Virtual Environment
python -m venv venv
3️⃣ Activate the Virtual Environment

On Windows:

venv\Scripts\activate

On Mac/Linux:

source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Run Migrations (if needed)
python manage.py migrate
6️⃣ Start the Development Server
python manage.py runserver

Now open your browser and go to:

http://127.0.0.1:8000/

🎉 Your Vehicle Management System should now be running!

🧠 Machine Learning Integration

The system uses machine learning algorithms to analyze vehicle-related data.
These models help in generating insights and improving decision-making based on stored vehicle information.

📊 Database

Default database: SQLite3

Database file: db.sqlite3

You can modify database settings inside config/settings.py

👤 Author

FURAHA NIYONGIRA Celia
Software Developer | UI/UX Designer

📜 License

This project is for educational, learning and commercial purposes.
