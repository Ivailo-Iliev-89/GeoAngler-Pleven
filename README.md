# PlevenFishing Atlas
A Full-Stack Geospatial Directory for Anglers

## Overview
PlevenFishing is a specialized web platform designed for the angling community in the Pleven region, Bulgaria.
It provides a curated database of fishing locations, categorized by water body type and fishing methods,
integrated with Google Maps for precise navigation.

## Key Features
- Dynamic Content Management: Fully managed via Django Admin.
- Advanced Filtering: Custom-built logic to filter locations by methods (Feeder, Spinning, etc.) using Django ManyToMany relationships.
- Geospatial Integration: Embedded Google Maps API for real-time location tracking.
- SEO & UX Focused: Clean, semantic HTML5, responsive CSS (Flexbox/Grid), and optimized typography (Google Fonts).

## Technical Stack
- Backend: Python , Django Rest Framework
- Database: PostgreSQL
- Frontend: HTML, CSS, JavaScript
- Environment Management: Python-dotenv for secure credential handling.

## Installation & Setup
- ```bash
- git clone 
- After installation, the user must log in to /admin and add objects with photos
- Create a .env file and populate it with your DB credentials (see settings.py for required keys).
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver

## Future Improvements
- Integration with a Weather API for real-time fishing conditions.
- User-submitted fishing reports with photo uploads.
- Interactive "Catch Map" using Leaflet.js.


