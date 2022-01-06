FROM python:3.9

COPY ./backend /backend

RUN pip install -e ./backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]