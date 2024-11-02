import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):  # Каждый силач поднимает 5 шаров
        delay = 1 / power  # Задержка обратно пропорциональна мощности
        await asyncio.sleep(delay)
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Pasha', 3)),
        asyncio.create_task(start_strongman('Denis', 4)),
        asyncio.create_task(start_strongman('Apollon', 5))
    ]
    await asyncio.gather(*tasks)

# Запускаем турнир
asyncio.run(start_tournament())