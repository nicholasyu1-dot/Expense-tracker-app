FROM  python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install tk

CMD ["python", "Code/Expense-tracker-app.py"] 
