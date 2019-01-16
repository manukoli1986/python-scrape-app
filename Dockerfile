FROM python:3.4-alpine
ADD scrape.py /code/
WORKDIR /code/
RUN pip3 install Flask requests
CMD ["python3", "scrape.py"]
