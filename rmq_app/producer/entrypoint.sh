#!/bin/sh

echo "Waiting for RabbitMQ..."

# Проверяем доступность порта 5672 (стандартный порт для RabbitMQ)
while ! nc -z $RABBITMQ_HOST $RABBITMQ_PORT; do
    echo "waiting for rabbitmq..."
    sleep 0.1
done

echo "RabbitMQ started"

exec "$@"
