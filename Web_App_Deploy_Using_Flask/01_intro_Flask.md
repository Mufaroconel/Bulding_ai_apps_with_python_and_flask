# Introduction to Flask

## Overview
After watching this video, you will be able to:
- Define the Flask web framework.
- Describe its main features.
- Explain how to install Flask.
- Understand the main differences between Flask and Django.

## What is Flask?
- **Flask** is a micro framework for creating web applications.
- It is not opinionated and does not bind the user to specific tools.
- Flask provides minimal dependencies, making it lightweight and flexible.

## History
- Created by **Armin Ronacher** in 2004 as an April Fool's joke.
- Gained popularity for its ease of use and extensibility.

## Installation
- **Flask Version:** 2.2.2 (requires Python 3.7+).
- **Installation:** 
  - Recommended to use a virtual environment.
  - Install using `pip install Flask==2.2.2`.

## Main Features of Flask
- **Web Server:** Runs applications in development mode.
- **Debugger:** Shows interactive traceback and stack trace in the browser.
- **Logging:** Uses standard Python logging; custom logs can be added.
- **Testing:** Supports test-driven development (TDD) using frameworks like `pytest`.
- **Request and Response:** Access and customize request and response objects.
- **Static Assets:** Supports static files (CSS, JS, images).
- **Templating:** Uses Jinja for dynamic page rendering.
- **Routing:** Supports dynamic URLs and RESTful services.
- **Error Handling:** Global error handlers can be written.
- **Session Management:** Supports user session management.

## Popular Flask Extensions
- **Flask-SQLAlchemy:** Adds SQLAlchemy ORM support.
- **Flask-Mail:** Enables SMTP mail server setup.
- **Flask-Admin:** Adds admin interfaces.
- **Flask-Uploads:** Customized file uploading.
- **Flask-CORS:** Handles Cross-Origin Resource Sharing.
- **Flask-Migrate:** Adds database migrations.
- **Flask-User:** Adds user authentication and management.
- **Marshmallow:** Supports object serialization/deserialization.
- **Celery:** Task queue for background tasks and schedules.

## Dependencies of Flask
- **Werkzeug:** Implements WSGI (Web Server Gateway Interface).
- **Jinja:** Template language for rendering pages.
- **MarkupSafe:** Escapes untrusted input to prevent injection attacks.
- **ItsDangerous:** Securely signs data and protects session cookies.
- **Click:** Framework for writing command-line applications.

## Flask vs. Django
- **Flask:** A micro framework, light and flexible, with minimal dependencies.
- **Django:** A full-stack, opinionated framework that includes everything needed for full-stack development.
- **Flexibility:** Flask allows plug-and-play extensions, while Django makes most decisions for the developer.

## Summary
- Flask is a micro framework with minimal dependencies, ideal for lightweight and flexible web applications.
- It can be extended with numerous community extensions.
- Flask can be installed via pip, and it's essential to manage dependencies carefully.
- Compared to Django, Flask is more lightweight and flexible, while Django is more comprehensive and opinionated.
