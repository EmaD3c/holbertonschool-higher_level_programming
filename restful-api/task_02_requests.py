#!/usr/bin/python3
'''
Write a basic Python script to fetch posts
from JSONPlaceholder using requests.get()
'''
import requests
import csv


def fetch_and_print_posts():
    '''
    Print post
    '''
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {response.status_code}')

    if response.status_code == 200:
        # Récupère les données JSON dans une variable
        data = response.json()

        # Parcours les données et affiche chaque titre
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    '''
    Fetch posts and save them to posts.csv
    '''
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        # Récupère les données JSON dans une variable
        data = response.json()

        # Crée une liste de dictionnaires avec les données nécessaires
        posts_data = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in data
        ]

        # Écrire dans le fichier CSV
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Écrire l'en-tête des colonnes
            writer.writerows(posts_data)  # Écrire les lignes de données

    else:
        print("Request failed with status code:", response.status_code)
