# Django Library Management

Mini app de librairie avec CRUD, Search, Login, Register.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Description

Ce dépôt contient une application web de gestion de bibliothèque développée avec Django. L'application permet de gérer les livres, les utilisateurs, et de fournir des fonctionnalités de recherche, d'inscription et de connexion.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete books.
- **Search Functionality**: Search for books by title, author, or genre.
- **User Authentication**: Login and Register functionalities for users.
- **Responsive Design**: User-friendly interface with HTML, CSS, and JavaScript.

## Installation

Pour installer et exécuter cette application localement, suivez ces étapes :

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/acelest/django-library-management.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd django-library-management
    ```
3. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows: env\Scripts\activate
    ```
4. Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```
5. Appliquez les migrations :
    ```bash
    python manage.py migrate
    ```
6. Créez un superutilisateur pour accéder à l'interface d'administration :
    ```bash
    python manage.py createsuperuser
    ```
7. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

## Usage

- Accédez à l'application via `http://127.0.0.1:8000/`.
- Utilisez l'interface d'administration via `http://127.0.0.1:8000/admin/` pour gérer les livres et les utilisateurs.
- Connectez-vous ou inscrivez-vous pour accéder aux fonctionnalités de recherche et de gestion des livres.

## Contributing

Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre ces étapes :

1. Fork le dépôt.
2. Créez une branche pour votre fonctionnalité ou correction de bug :
    ```bash
    git checkout -b feature-nom
    ```
3. Effectuez vos modifications et committez-les :
    ```bash
    git commit -m 'Ajout de la fonctionnalité X'
    ```
4. Poussez vers la branche :
    ```bash
    git push origin feature-nom
    ```
5. Ouvrez une Pull Request.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contact

Pour toute question ou suggestion, vous pouvez nous contacter à :
- **Nom**: ACELST
- **Email**: aubingta@icloud.com

## Acknowledgements

Nous tenons à remercier les ressources et individus suivants pour leur soutien et leurs contributions :
- [Resource 1](https://example.com)
- [Resource 2](https://example.com)
- [Individual 1](https://github.com/individual1)
- [Individual 2](https://github.com/individual2)
