import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} подняд {i} шар')
    print(f'Силач {name} завершил соревнование')

async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Апполон', 5))
    strongman2 = asyncio.create_task(start_strongman('Геракл', 3))
    strongman3 = asyncio.create_task(start_strongman('Витя', 2))

    await strongman1
    await strongman2
    await strongman3

start = time.time()
asyncio.run(start_tournament())
end = time.time()
print(f'Соревнование продлилось {end - start} секунд')