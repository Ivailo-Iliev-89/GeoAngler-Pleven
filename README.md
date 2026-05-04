# GeoAngler Pleven

### A Full-Stack Geospatial Directory for Anglers in Pleven Region, Bulgaria

***GeoAngler***  is a robust web platform that centralizes angling intelligence for the Pleven region.
It bridges the gap between static location data and dynamic user needs through a custom-built filtering system and Google Maps integration.


## Key Technical Features

- ***Filtering Engine*** :  Leverages ***Django's ORM to filter*** locations by criteria (water body, type, fishing methods) using optimized `ManyToMany` queries.
- ***Relational Data Structure*** :  Link fishing reports (Posts) to specific locations using Django `ForeignKey`.
- ***Geospatial Integration*** :  Embedded ***Google Maps API*** for precise location tracking.
- ***Secure Configuration*** :  ***Implemented*** industry-standard security by decoupling settings from credentials using Environment Variables.
- ***SEO*** :  Responsive design (Flexbox/Grid) with optimized typography (Google Fonts).
- ***Discovery System*** :  ***Integrated*** a "Discover" module with intelligent filtering by water body, categories and fishing techniques.
- ***Smart Search*** :  ***Implemented*** a robust search engine using ***Django Q*** objects to perform Locations and Fishing Methods.
- ***Enhanced UX Interaction*** :  ***Developed*** a custom JavaScript dropdown navigation with smart hover-delay logic to prevent accidental menu closures.
- ***Real-time Weather*** :  ***Integrated OpenWeatherMap API*** to fetch live meteorological data (wind speed, temperature and sky) based on GPS coordinates for each fishing place.
- ***Containerization*** :  ***Fully Dockerized application using Docker Compose*** to manage multi-container architecture (Django, PostgreSQL, Nginx).
- ***Production-ready Web Server***:  ***Configured Nginx as a reverse proxy*** to handle static file serving and enhance application security and performance.
- ***Automated Testing*** :  ***Implemented Unit Tests*** for core business logic, including search functionality, pagination, and URL resolution to ensure code stability.


## Preview

#### Interactive Landing Page (Parallax & Custom Navigation)
![Home Page](screenshots/geoangler-home.png)

#### Secure Authentication (User Onboarding & Security Hints)
![Auth](screenshots/geoangler-register.png)

#### Detailed Spot Overview (Google Maps & Related Techniques)
![Location Detail](screenshots/geoangler-location-detail.png)

#### Technique Encyclopedia (Related Locations & Data Mapping)
![Fishing Methods Detail](screenshots/geoangler-method.png)

#### Complex Filtering & Search Results
![Search Filters](screenshots/geoangler-search.png)

#### Secure Community Feedback (User Reports)
![User Reports](screenshots/geoangler-report.png)


## Tech Stack

- ***Backend*** :  Python , Django 
- ***Database*** :  PostgreSQL
- ***Frontend*** :  HTML, CSS ( Flexbox and Grid ), JavaScript (Custom Interactive Components)
- ***Environment Management*** :  Python-dotenv for secure credential handling
- ***API*** :  Google Maps API, OpenWeatherMap API
- ***DevOps & Deployment*** :  Docker, Docker Compose, Nginx, GitHub Codespaces
- ***Testing*** :  Django TestCase (Unit Testing)


## What I Learned

- ***API Integration*** :  Gained experience in integrating and customizing third-party services like the Google Maps API for real-world applications.
- ***Querying*** :  Using a Django's `filter()` and `exclude()` methods to ***handle*** complex many-to-many relationships.
- ***Environment Security*** :  ***Learned the importance of securing sensitive data*** (API keys, DB credentials) using `python-dotenv` to follow ***best practices***.
- ***Data Modeling*** :  ***Understood how to design a relational schema*** that connects geographical locations with user-contributed reports and fishing methods.
- ***Query Logic*** :  Use a Django Q objects for complex OR statements, allowing users to search across multiple database models from a single input.
- ***UI Patterns*** :  ***Implemented*** hover logic in CSS and ***timeout-delay in JavaScript*** to create stable navigation menus.
- ***Filtering via URL*** :  ***Learned*** how to use request.GET to filter database results dynamically, without creating multiple redundant views.
- ***Containerization*** :  Process of containerizing a Python/Django app, ***managing volumes for data persistence, and networking between containers***.
- ***Reverse Proxy Config***: ***Learned how to set up Nginx to sit in front of Gunicorn***, managing static assets and routing traffic securely.
- ***TestsCases***: ***Understood how to isolate logic*** using a database for automated testing, ensuring that new features ***don't break existing functionality***.
- ***AJAX/Dynamic Loading***: ***Implemented asynchronous requests (AJAX) to handle pagination*** and filtering without full page reloads, improving UX.



## Instructions to setup

- ***To get a local copy up and running, follow these steps !*** :

- `1.` **Docker and Docker Compose installed on your machine**.
- `1.1.` (OPTIONAL) *Python 3.12 version (if you running without Docker)*.

- `2.` ***Clone the repo and run these commands in bash terminal (gitbash/powershell)*** :
- `2.1` ```bash ---> **git clone https://github.com/Ivailo-Iliev-89/GeoAngler-Pleven.git**
- `2.2` ```bash ---> **cd GeoAngler-Pleven**

- `3.` ***Environment Variables***:
- `3.1` **Create a .env file in the root directory and add your credentials**:
- **DEBUG=True**
- **SECRET_KEY=(your_secret_key)**
- **DB_NAME=postgres(your_db)**
- **DB_USER=postgres(your_username)**
- **DB_PASSWORD=(your_password)**
- **DB_HOST=(localhost/your localhost)**
- **DB_PORT=(5432/5433/your_local_port)**
- **GOOGLE_MAPS_API_KEY=(your_api_key)**
- **OPENWEATHER_API_KEY=(your_weather_key)**

- `4.` ***Run with Docker(Recommended)***:
- `4.1` **This command builds the images and starts the Django app, PostgreSQL, and Nginx**:
- `4.2` ```bash ---> **docker-compose up --build**

- `5.` ***Initialize Database***:
- `5.1` **In a new terminal window run the migrations and create a superuser**:
- `5.2` - ```bash ---> **docker-compose exec web python manage.py migrate**
- `5.3` - ```bash ---> **docker-compose exec web python manage.py createsuperuser**

- `6.` ***Run Automated Tests***:
- `6.1` **Ensure everything is working correctly**:
- `6.2` ```bash ---> **docker-compose exec web python manage.py test**


##  Usage
  
- ***Explore Locations*** :  ***Navigate*** through the curated database of fishing spots in the Pleven region.
- ***Geospatial Navigation*** :  Click on the embedded Google Maps links to ***get precise GPS directions*** to each spot.
- ***Filtering by Method*** :  Use the ***dynamic filter buttons*** to find spots suitable for specific techniques like "Spinning" or "Feeder".
- ***Manage Content*** :  Access the Django Admin panel to add new locations, update photos, or manage fishing reports.
- ***Search*** :  Use the ***global search bar*** to find spots by name, description, or specific fish species and methods.
- ***Interactive Discovery*** :  Use the "Discover" dashboard to ***quickly jump into categories*** like Rivers, Lakes, or specialized techniques.
- ***Real-time Conditions*** :  View live weather updates (temperature, wind speed, conditions) for each spot, powered by the OpenWeatherMap API.
- ***Community Reports*** :  Registered users can submit fishing reports (posts) with photos, creating a live feedback loop for each location.
- ***Automated Deployment*** :  Launch the entire environment (App, DB, Proxy) with a single command using ***Docker Compose***.


## Future Improvements

- ***Interactive***  "Catch Map" using ***Leaflet.js***.