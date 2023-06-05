# Overview
This project is aimed at demonstrating the user of Django and Python in web development, specifically how it facilitates the development and deployment of web based applications. This project was meant to help me build a foundational knowlegde usng Django and Python to develop and host web applications.

For this project, I opted to write a calorie tracker application, which is meant to make tracking your daily caloric intake easier. To be able to start a test server, you only needs to install the modules found in the 'requirements.txt' file and run the server by typing 'python manage.py runserver' in the terminal. The test server will begin and you will need to navitage to 'http://127.0.0.1:8000/' to see the application.

The purpose behind writing this software, was to use what I've learned in Django and Python to implement a web application that can accurately track your daily caloric intake. The application will take user input and add/subtract from a total counter for calories. The user will also be able to set caloric goals, and save their entries.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

This web appliction functions much like a diary, in the sense that you will have the opportunity to make an entry for each meal that you want to add. The home page of the project displays the entries that have been added to the local sqlite database. Each entry is displayed with a title and the date that the meal was entered. Clicking on the title of an entry will take the user to another page that displays the details of the entry, which can be whatever the user entered. In this details page, the user will also have the option to either delete or update the entry by clicking on a button. If the user clicks on the update button, they will be taken to a new page where the description and title fields can be edited and saved. Clicking on the delete button will take the user to a new page that will ask the user to confirm that they want to delete the entry. Finally, going back to the home page the user also has the option to add a new entry to the page by clicking on the add meal button. Clicking on that button will take the user to a new page where they will be able to populate the fields for their entry and save it.

# Development Environment
Visual Studio Code
Python 3.11
Django 4.2.1
HTML
CSS

# Useful Websites
Django Documentation and Tutorial
Django Tutorial in Visual Studio Code

# Future Work
* Edit Meal functionality is not working as expected, need to troubleshoot and fix the problem
