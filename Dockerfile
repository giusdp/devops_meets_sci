FROM python:latest

COPY . .

WORKDIR /app

CMD ["/bin/bash"]
