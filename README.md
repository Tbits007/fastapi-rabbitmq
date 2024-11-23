RabbitMQ Producer-Consumer Example with FastAPI
🚀 A simple implementation of the Producer-Consumer pattern using RabbitMQ and FastAPI.

This repository demonstrates how to build asynchronous communication between services using RabbitMQ message queues.

🔧 Technologies
FastAPI: A modern, fast web framework for building APIs with Python.
RabbitMQ: A robust message broker for asynchronous communication.
aio-pika: An asynchronous library for interacting with RabbitMQ.
📜 Features
Producer:

Sends messages to a RabbitMQ queue.
Supports custom data submission through an API.
Consumer:

Processes messages from a RabbitMQ queue.
Demonstrates asynchronous data handling.
Logging:

Clear and concise logs to track message flow and processing status.
📂 Project Structure
producer/ — Producer implementation that sends data to RabbitMQ.
consumer/ — Consumer implementation that reads and processes messages.
docker-compose.yml — A quick setup for RabbitMQ using Docker.
README.md — Detailed project documentation with usage examples.
🚀 How to Run?
Make sure Docker and Docker Compose are installed.
Start RabbitMQ via Docker:
bash
Копировать код
docker-compose up -d
Run the producer and consumer:
bash
Копировать код
python producer/main.py
python consumer/main.py
Send messages through the producer's FastAPI endpoint and watch the consumer process them.
🎯 Project Goals
Introduce developers to the basics of asynchronous communication between services.
Showcase the practical use of RabbitMQ for implementing the Producer-Consumer pattern.
Provide a ready-to-use foundation for building more complex message-driven systems.
✨ Feel free to contribute and leave a star! 🌟
