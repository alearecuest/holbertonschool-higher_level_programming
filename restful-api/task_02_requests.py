#!/usr/bin/python3
"""
Description:
    This module contains functions to interact with the JSONPlaceholder API.
    It demonstrates how to fetch data from a RESTful API using
    the requests library and process the JSON response.
    It also shows how to convert the data to CSV format.

Functions:
    - fetch_and_print_posts(): Fetches posts and prints their titles
    - fetch_and_save_posts(): Fetches posts and saves them to a CSV file
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Function that fetches all posts from JSONPlaceholder,
    prints the status code and then the titles of the posts.
    """
    response = requests.get('htps://jsonplacerholder.typicode.com/posts')

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Function that fetches all posts from JSONPlaceholder
    and saves them to a CSV file.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        simplified_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(simplified_posts)
