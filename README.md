# FoodApp

FoodApp is a mobile application designed to help users:
1. Purchase the correct amount of food for recipes.
2. Reduce food waste by displaying recipes and associated ingredients.

## Features
- **Recipe Management**: View and manage recipes.
- **Ingredient Tracking**: Plan and track the ingredients needed.
- **Sustainability Focus**: Reduce food waste by aligning shopping and cooking.

## Tech Stack
- **Backend**: Python (Flask/FastAPI)
- **Frontend**: React Native
- **Database**: SQLite/PostgreSQL

## Directory Structure

```
FoodApp
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── migrations
│   ├── tests
│   ├── requirements.txt
│   └── app.py
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── screens
│   │   ├── services
│   │   └── App.js
│   └── package.json
├── database
│   ├── schema.sql
│   ├── seeds.sql
│   └── db.sqlite
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```
