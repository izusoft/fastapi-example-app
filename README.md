# FastApi-example-app
App example FastApi + Redis + Docker with environment settings via .env file
### Installing
```
git clone https://github.com/zubarevski/fastapi-example-app
cd fastapi-example-app
```
Then create `.env` file (or rename and modify `.env.example`) in project root and set environment variables for application.
### Deploy with Docker:
```
docker-compose build
docker-compose up -d
```

Application will be available on `http://127.0.0.1:5000` in your browser.  
All routes are available on `/docs` or `/redoc` paths with Swagger or ReDoc.
