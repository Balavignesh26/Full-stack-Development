Personal Portfolio Website

A modern, responsive portfolio website built with Flask, featuring interactive UI elements, dynamic content, and a professional design. This project showcases my work in software engineering, machine learning, and web development.

[![Flask](https://img.shields.io/badge/Flask-3.0.0-blue.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)

Screenshots

Home Section
![Home Section](static/images/screenshots/home.png)

Portfolio Section
![Portfolio Section](static/images/screenshots/portfolio.png)

Contact Section
![Contact Section](static/images/screenshots/contact.png)

Features

Core Functionality
- Responsive Design - Mobile-first approach that works on all devices
- Dynamic Navigation - Smooth scrolling with animated section transitions
- Interactive Portfolio - Project showcase with detailed popup modals
- Contact Form - Functional form with backend validation and database storage
- GitHub Integration - Direct links to project repositories
- Modern UI/UX - Glassmorphism effects and smooth animations

Technical Features
- Custom CSS animations and transitions
- Section-based navigation system
- Fully responsive layout
- SQLite database integration
- Server-side form validation
- Fast page load times

Technologies Used

Backend
- Flask --> Lightweight Python web framework
- SQLite --> Embedded database for contact form data
- Jinja2 --> Template engine for dynamic HTML rendering

Frontend
- HTML5 --> Semantic markup
- CSS3 --> Modern styling with animations
- JavaScript (ES6) --> Interactive functionality
- Bootstrap 5 --> Responsive grid system
- Font Awesome --> Icon library
- jQuery --> DOM manipulation

Design
- Glassmorphism --> Modern UI design trend
- Gradient Backgrounds --> Eye-catching color schemes
- Custom Animations --> Smooth transitions and effects

Project Structure
portfolio-website/
│
├── app.py                      # Flask application entry point
├── data.db                     # SQLite database
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with common elements
│   ├── index.html             # Main portfolio page
│   └── success.html           # Form submission success page
│
└── static/                     # Static assets
    ├── css/
    │   └── style.css          # Custom styles and animations
    ├── js/
    │   └── script.js          # Interactive features
    └── images/
        ├── pfp.jpg            # Profile picture
        ├── CVE.webp           # Project thumbnail
        ├── Crypt.png          # Project thumbnail
        └── Qubit.png          # Project thumbnail



