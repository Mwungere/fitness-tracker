# Fitness Tracking System

---

## Table of Contents

- [Fitness Tracking System](#fitness-tracking-system)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Getting Started](#getting-started)

---

## Project Overview

The **Fitness Tracking System** is a web application that helps users manage and track their fitness goals. Users can log meals, track their exercise routines, and monitor their progress over time. Based on user inputs such as body measurements, diet, and exercise, the system provides personalized recommendations to support healthy living and fitness.

---

## Features

- **User Profile**: Manage user information including height, weight, and fitness goals.
- **Meal Logging**: Track meals with calorie information to monitor daily intake.
- **Exercise Logging**: Record exercises with duration and calories burned.
- **Personalized Recommendations**: Get daily recommendations for meals and exercises.
- **Dashboard and Analytics**: Visualize data on a user-friendly dashboard with charts to track progress over time.

---

## Technologies Used

- **Backend**: Django, PostgreSQL (database)
- **Frontend**: Django templates, HTML, Bootstrap CSS
- **Visualization**: Chart.js for interactive charts and analytics
- **Database Connection**: psycopg2-binary for PostgreSQL

---



## Getting Started

To get a local copy of the **Fitness Tracking System** running, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fitness-tracking-system.git

2. Navigate to the project directory
   ```bash
   cd fitness-tracking-system
3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
4. Setup the database
   If you're using PostgreSQL, make sure to adjust the settings.py file accordingly. Then, apply the migrations to set up the database schema.
   ```bash
   python manage.py migrate

5. Start the Django development server
    Make sure you Visit http://127.0.0.1:8000/register in your browser to begin  registration after running the server.

   ```bash
   python manage.py runserver


6. Insert random activities data
   ```bash
   python manage.py insert_random_activities
7. Export your data into CSV file 
   ```bash
   python manage.py extract_activities   
