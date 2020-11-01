import asyncio
from aiohttp import ClientSession

async def my_coroutine(num):
    print("Started for: ", num)
    await asyncio.sleep(2)
    print("Finished for: ", num)
    return str(num)

async def f2():
    print("Started F2")
    await asyncio.sleep(2)
    print("Finished F2")
    

async def f1():
    print("Started F1")
    await f2()
    print("Finished F1")


async def fetch(url):
    async with ClientSession() as s, s.get(url) as res:
        ret  = await res.read()
        print(ret)
        return ret

async def print_when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print(await res)

if __name__ == '__main__':        
    # c = my_coroutine(3) 
    # task = asyncio.ensure_future(c)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(task)
    # loop.close()

    # many = asyncio.gather(
    #     my_coroutine(1),
    #     my_coroutine(2),
    #     my_coroutine(3)
    # )

    loop = asyncio.get_event_loop()
    # loop.run_until_complete(many)
    # loop.close()

    # loop.run_until_complete(f1())
    # loop.close()

    # loop.run_until_complete(fetch("https://timesofindia.indiatimes.com/"))
    # loop.close()

    corors = [
        fetch("http://www") for i in range(100_000_000)
    ]

    # 3.7
    # task = asyncio.create_task(c)
    # asyncio.run(my_coroutine(3))
