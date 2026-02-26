# PlevenFishing Atlas

### A Full-Stack Geospatial Directory for Anglers in Pleven Region, Bulgaria

***PlevenFishing***  is a robust web platform that centralizes angling intelligence for the Pleven region.
It bridges the gap between static location data and dynamic user needs through a custom-built filtering system and Google Maps integration.


## Key Technical Features

- ***Filtering Engine*** :  Leverages Django's ORM to filter locations by criteria (water body, type, fishing methods) using optimized `ManyToMany` queries.
- ***Relational Data Structure*** :  Link fishing reports (Posts) to specific locations using Django `ForeignKey`.
- ***Geospatial Integration*** :  Embedded ***Google Maps API*** for precise location tracking.
- ***Secure Configuration*** :  ***Implemented*** industry-standard security by decoupling settings from credentials using Environment Variables.
- ***SEO & UX Focused*** :  Responsive design (Flexbox/Grid) with optimized typography (Google Fonts).


## Tech Stack

- ***Backend*** :  Python , Django 
- ***Database*** :  PostgreSQL
- ***Frontend*** :  HTML, CSS (Flexbox and Grid), JavaScript
- ***Environment Management*** :  Python-dotenv for secure credential handling.
- ***API*** :  Google Maps JavaScript API


## What I Learned

- ***API Integration*** :  Gained experience in integrating and customizing third-party services like the Google Maps JavaScript API for real-world applications.
- ***Querying*** :  Using a Django's `filter()` and `exclude()` methods to ***handle*** complex many-to-many relationships in a user-friendly way.
- ***Environment Security*** :  ***Learned the importance of securing sensitive data*** (API keys, DB credentials) using `python-dotenv` to follow ***industry best practices***.
- **Data Modeling** :  ***Understood how to design a relational schema*** that connects geographical locations with user-contributed reports and fishing methods.


## Instructions to setup

- Clone or download the repository :
- ```bash
- git clone https://github.com/ivailoiliev89-netizen/Pleven-Fishing.git
- ***Create*** a .env file and populate it with your DB credentials (see settings.py for required keys)
- pip install -r requirements.txt
- python manage.py makemigrations 
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver


##  Usage
  
- ***Explore Locations*** :  ***Navigate*** through the curated database of fishing spots in the Pleven region.
- ***Geospatial Navigation*** :  Click on the embedded Google Maps links to ***get precise GPS directions*** to each spot.
- ***Filter by Method*** :  Use the ***dynamic filter buttons*** to find spots suitable for specific techniques like "Spinning" or "Feeder".
- ***Manage Content*** :  Access the Django Admin panel to add new locations, update photos, or manage fishing reports.


## Future Improvements

- ***Integration***  with a ***Weather API*** for real-time fishing conditions.
- ***Interactive***  "Catch Map" using ***Leaflet.js***.


