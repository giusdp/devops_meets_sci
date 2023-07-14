FROM python:latest

WORKDIR /app
COPY . .

CMD ["/bin/bash"]
