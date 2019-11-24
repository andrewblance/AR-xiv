FROM python:3.6-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python arxiv.py

# docker build -t arxiv:latest .
# docker run -d -p 5000:5000 arxiv
# -d: detach, -p: post select
#
