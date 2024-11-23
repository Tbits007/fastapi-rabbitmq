import aio_pika
from app.config import settings
from aio_pika.abc import AbstractRobustConnection


async def create_connection() -> AbstractRobustConnection:
    connection = await aio_pika.connect_robust(
        settings.amqp_url,
    )
    return connection


async def consume() -> None:
    connection = await create_connection()
    queue_name = "test_queue"

    async with connection:
        # Creating channel
        channel = await connection.channel()
        # Will take no more than 10 messages in advance
        await channel.set_qos(prefetch_count=10)
        # Declaring queue
        queue = await channel.declare_queue(queue_name, auto_delete=True)
        
        while True:
            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        print(message.body.decode())
