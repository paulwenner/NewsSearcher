# NEWSSEARCHER

#### Video Demo: [Watch the Demo](https://youtu.be/FsQAlZOAmLQ)

## Description:

NEWSSEARCHER is a web application built with Flask that allows users to search for news articles based on specific keywords and optional language preferences. It utilizes the NewsAPI to retrieve and display relevant news articles.

### Features:

- **Search News**: Users can enter a search query to find news articles related to their interests.
- **Language Preferences**: Users have the option to specify the language in which they want to search for news articles.
- **Cleaned Content**: The application removes unnecessary HTML tags and character markers from the article content for a better reading experience.
- **Responsive Design**: The web application is designed to be responsive and accessible on various devices.

## Getting Started:

To run the NEWSSEARCHER application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain an API key from [NewsAPI](https://newsapi.org/) and replace `"AddKeyHere"` in the code with your actual API key.
4. Run the Flask application using `python --app project.py run`.
5. Open a web browser and navigate to `http://localhost:5000` to use the application.

## Usage:

1. Enter a search query in the provided input field.
2. Optionally, select a language preference from the dropdown menu.
3. Click the "Search" button to retrieve and display relevant news articles.
4. Browse the list of articles, which includes titles and cleaned content.
5. Click on an article title to view the full article on the source website.

## Dependencies:

- Flask: Web framework for building the application.
- NewsAPI: Used for fetching news articles.
- Python requests: Used for making HTTP requests to the NewsAPI.
- Python re: Used for regular expressions to clean article content.
- HTML, CSS, and JavaScript: Used for front-end web development.

## Credits:

This project was created by Paul Wenner




