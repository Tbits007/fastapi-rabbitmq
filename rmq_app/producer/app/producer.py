import aio_pika
from app.config import settings
from aio_pika.abc import AbstractRobustConnection


async def create_connection() -> AbstractRobustConnection:
    connection = await aio_pika.connect_robust(
        settings.amqp_url,
    )
    return connection


async def produce(routing_key: str, data: bytes) -> None:
    connection = await create_connection()

    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=data),
            routing_key=routing_key,
        )
