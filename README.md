# My Personal Portfolio Site (2025 MLH/Meta PE Fellowship)

Welcome to my personal portfolio website! I built this Flask-based portfolio during my MLH x Meta Production Engineering Fellowship to showcase my work, education, and interests. This site serves as a comprehensive overview of who I am and what I've accomplished.

## What I've Built

I've created a dynamic portfolio site that includes multiple pages and features to tell my story. Here's what I've implemented:

### Portfolio Features

- [x] Personal photo and introduction
- [x] Detailed "About Me" section
- [x] Professional work experience showcase
- [x] Hobbies and interests with images
- [x] Educational background
- [x] Interactive map of places I've visited

### Technical Implementation

- [x] Flask web application with multiple routes
- [x] Jinja templating for dynamic content rendering
- [x] Timeline page with posts/comments, MySQL database integration, and API endpoints
- [x] Dedicated hobbies page with image galleries
- [x] Responsive navigation menu
- [x] Clean, modern styling with CSS

## Getting Started

My DigitalOcean VPS is currently spun down, but want to run my portfolio locally? Here's how to get it up and running on your machine.

## Installation

First, make sure you have Python 3 and pip installed on your system. I recommend creating a virtual environment to keep dependencies organized:

```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Running the Portfolio

To run my portfolio locally, you'll need to set up the environment:

1. Create a `.env` file using the `example.env` template (copy the variables from the template)

2. Start the Flask development server:

```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:

```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser!

_Note: The site will only be accessible on your local machine while the Flask server is running. I'm planning to redeploy it to the cloud soon! (was previously deployed to DigitalOcean VPS during the MLH x Meta Fellowship)_

## About This Project

This portfolio represents my journey in web development and showcases my technical skills. I built it using Flask, HTML templates, and CSS to create a responsive and interactive experience. Feel free to explore the code and see how I've structured the application.

If you have any questions about the implementation or would like to contribute improvements, I'd love to hear from you!
