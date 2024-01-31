# Voting App

The Voting App is a web application that allows employees to vote for their favorite dishes for lunch from different restaurants. The menu with the most votes will be chosen for the day.

## Features

- **Authentication:** Users can log in and log out securely.
- **Restaurant Management:** Admin users can create/delete and manage restaurant details.
- **Menu Management:** Admin users can upload/delete menus for restaurants.
- **Employee Management:** Admin users can add/remove employees from the system.
- **Voting:** All employees can vote for their favorite dishes.
- **Results:** Display results for the current day, ensuring fairness by not allowing the same restaurant to win for three consecutive working days.

## Project Structure

- **authentication/:** Django app containing models and views.
- **restaurant_lunch_vote/:** Django app containing models and views.
- **static/:** Static files such as CSS.
- **templates/:** HTML templates.
- **db.sqlite3:** SQLite database file.

## ER Diagram
[![ER Diagram](https://i.postimg.cc/NfsFVqv8/Screenshot-2024-02-01-031058.png)](https://postimg.cc/7bRqGR6b)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/prantanath/Voting_app.git

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Apply database migration:
   
   ```bash
   python manage.py migrate

4. Run the server:

   ```bash
   python manage.py runserver

5. Create an admin to get access to Admin Dashboard:

   ```bash
   python manage.py createsuperuser

## Screenshots
1. Login Page
   
   [![Login Page](https://i.postimg.cc/hPVF9h5p/Screenshot-2024-02-01-034502.png)](https://postimg.cc/N5GPtGYH)
   
2. Admin Dashboard
   
   [![Admin Dashboard](https://i.postimg.cc/bJ4Mnj07/Screenshot-2024-02-01-034550.png)](https://postimg.cc/KkrJXwHf)
   
3. Employee Dashboard
   
   [![Employee Dashboard](https://i.postimg.cc/dt2Xhphf/Screenshot-2024-02-01-034822.png)](https://postimg.cc/3dw96LCj)
   
4. Results Page
   
   [![Results Page](https://i.postimg.cc/6QvC3J32/Screenshot-2024-02-01-035630.png)](https://postimg.cc/cKdv9zf0)

## Future Ideas
- 1.Implement a notification system to alert users about voting results.
- 2.Implement a rating system for the menus to disqualify bad menus in future.
   
