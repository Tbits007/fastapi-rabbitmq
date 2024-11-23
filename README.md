# RabbitMQ Producer-Consumer Example with FastAPI

🚀 A simple implementation of the Producer-Consumer pattern using RabbitMQ and FastAPI.

This repository demonstrates how to build asynchronous communication between services using RabbitMQ message queues.

---

## 🔧 Technologies

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **RabbitMQ**: A robust message broker for asynchronous communication.
- **aio-pika**: An asynchronous library for interacting with RabbitMQ.

---

## 📜 Features

### Producer:
- Sends messages to a RabbitMQ queue.
- Supports custom data submission through an API.

### Consumer:
- Processes messages from a RabbitMQ queue.
- Demonstrates asynchronous data handling.

---

## 📂 Project Structure

- `producer/` — Producer implementation that sends data to RabbitMQ.
- `consumer/` — Consumer implementation that reads and processes messages.
- `docker-compose.yml` — A quick setup for RabbitMQ using Docker.
- `README.md` — Detailed project documentation with usage examples.

---

## 🚀 How to Run?

1. Make sure Docker and Docker Compose are installed.
2. Start RabbitMQ via Docker:
   
   ```bash
   docker-compose up --build
   
---

✨ Feel free to contribute and leave a star! 🌟
