# eskom-water-dashboard
Water monitoring dashboard system built with Python and web technologies.

# Eskom Water Monitoring Dashboard

## Description
A monitoring dashboard designed to track water usage in power plant cooling systems.

## Features
- Water consumption monitoring
- Cooling system performance tracking
- Leak detection
- Predictive analytics
- Maintenance reporting

## Technologies
Python
Flask
HTML
CSS
JavaScript

## Project Structure
backend - server logic
templates - HTML pages
static - CSS and images

## How to Run
1. Install Python
2. Open a command prompt (CMD) and navigate to the folder containing your project files (for example, if it’s on the Desktop in a folder called Eskom Project, use cd %USERPROFILE%\Desktop\Eskom Project). 
3. It’s recommended to create a virtual environment to isolate project dependencies by running python -m venv venv and then activating it with venv\Scripts\activate on Windows CMD. 
4. Once the environment is active, install the required libraries with pip install Flask pandas flask-cors  and pip install openmeteo-requests requests-cache retry-requests pandas 
5.Make sure your folder structure is correct, with app.py and data_simulation.py in the main folder, dashboard.html in a templates folder, and style.css and any images inside a static folder. 
6. To run the dashboard, execute python app.py in CMD, and the server should start with an address like http://127.0.0.1:5000/. Open this URL in a web browser to view the dashboard. If anything doesn’t appear, check that all static files are in place, Chart.js is properly loaded, and the browser console shows no errors. To stop the server, press Ctrl + C in CMD. Following these steps ensures the dashboard runs correctly on any computer.
