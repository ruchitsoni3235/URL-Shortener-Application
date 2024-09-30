Flask URL Shortener
This is a simple URL shortening web application built using the Flask framework in Python. It allows users to enter a long URL and receive a shortened version, which can be used to redirect back to the original URL.

Features
URL Shortening: Enter a long URL, and the application generates a short, unique URL.
Redirect Functionality: Users visiting the shortened URL will be automatically redirected to the original long URL.
URL Validation: The app validates the input to ensure that only valid URLs are shortened.
Error Handling: If the user submits an invalid URL or leaves the input blank, appropriate error messages are shown.

Getting Started
Prerequisites
To run this application, you need to have the following installed:

Python 3.x
Flask

Usage:
Open your web browser and navigate to http://127.0.0.1:5000/.
Enter the long URL you want to shorten in the input box.
Press the "shorten" button to generate a shortened URL.
Use the generated short URL to be redirected to the original long URL.
URL Validation
The application uses a regular expression to validate URLs. It accepts URLs with http://, https://, and various domain formats. If an invalid URL is submitted, the application will display an error message.

Example
Original URL: https://www.google.com
Shortened URL: http://127.0.0.1:5000/R7lBcx


Flash Messages
The app uses Flask's flash function to display feedback to the user. This includes:

Success messages when a URL is successfully shortened.
Error messages if the input URL is empty or invalid.
Redirect Handling
When a user visits a shortened URL, the app checks if the short URL exists in its records:

If found, it redirects the user to the corresponding long URL.
If not found, it returns a 404 page indicating that the short URL doesn't exist.
Future Improvements
Database Support: Currently, the shortened URLs are stored in a Python dictionary. In the future, support for a database (like SQLite, MySQL, or MongoDB) can be added for persistent storage.
User Accounts: Allow users to create accounts and manage their shortened URLs.
Analytics: Track how many times a shortened URL is accessed.
