import datetime
import colorama
import asyncio
import random

def main():
    lim = 20
    print("Running standard loop with {:,} actions.".format(lim*20))
    ts = datetime.datetime.now()
    
    loop = asyncio.get_event_loop()
    data = asyncio.Queue()

    # task1 = loop.create_task(generate_data(lim, data))
    # task2 = loop.create_task(generate_data(lim, data))
    # task3 = loop.create_task(process_data(2 * lim, data))

    # final_task = asyncio.gather(task1, task2, task3)

    # loop.run_until_complete(final_task)
    
    task = asyncio.gather(
        generate_data(10, data),
        generate_data(10, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data)
    )

    loop.run_until_complete(task)

    dt = datetime.datetime.now() - ts
    print(colorama.Fore.GREEN + "Exiting, time taken: {:,.2f} sec".format(dt.total_seconds()), flush=True)


async def generate_data(num: int, data: asyncio.Queue):
    for i in range(1, num + 1):
        item = i * i
        await data.put((item, datetime.datetime.now()))
        print(colorama.Fore.RED + " --- generated item {}".format(i), flush=True)
        await asyncio.sleep(0)

async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        item = await data.get()
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t
        processed += 1
        print(colorama.Fore.CYAN +
              " +++ Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        await asyncio.sleep(0)

if __name__ == '__main__':
    main()