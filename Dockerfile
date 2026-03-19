FROM  python:3.12-slim

WORKDIR /app

COPY . .

RUN RUN apt-get update && apt-get install -y tk8.6

CMD ["python", "Code/Expense-tracker-app.py"] 
