# Articles ETL Project by Milen Georgiev

## Setup and Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/MilenPlamenov/django_etl.git
    cd django_etl
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply Django migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

6. To run the Scrapy spiders and populate the database:
    ```sh
    cd articles_scraper
    scrapy crawl restofworld
    scrapy crawl capitalbrief
    ```

## API Endpoints

- `GET /api/articles/` - Get all articles.
- `GET /api/article/<id>/` - Get a single article by ID.
- `POST /api/article/create/` - Create a new article.
- `PUT /api/article/update/<id>/` - Update an article.
- `DELETE /api/article/delete/<id>/` - Delete an article.

## TODO in the future

- Add custom templates for the rest API
- Implement ArticleSpider class so CapitalBriefSpider and RestOfWorldSpider can inherit from it
- Improve the scraping to be able to scrape more
- Add NER (spacy lib) for the entities crawl
- Improve the project structure
- code refactor in the scraper pipelines.py
