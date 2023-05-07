import asyncio
import time, json

job_dict = {
    "ping": None,
    "send_message": None,
    "recive_message": None,
    "checksum": None,
    "mail": None,
    "vulnurability check": None,
    "grep data": None,
    "data process": None,
    "delete files": None,
    "git push": None,
    "jenkins spin up": None,
    "check system": None
    }

async def job_check(job_name, time):
    global job_dict
    await asyncio.sleep(time)
    job_dict[job_name] = 'success'
    with open('jobs.json', 'w') as file:
        json.dump(job_dict, file, indent=2)
    return

async def main():
    print(f"started at {time.strftime('%X')}")
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(job_check('send_message', 2))
        task2 = tg.create_task(job_check('recive_message', 3))
        task3 = tg.create_task(job_check('ping', 1))
        task4 = tg.create_task(job_check('grep data', 5))
        task5 = tg.create_task(job_check('check system', 10))
        task6 = tg.create_task(job_check('mail', 3))
        task7 = tg.create_task(job_check('checksum', 1))
        task8 = tg.create_task(job_check('vulnurability check', 4))
        task9 = tg.create_task(job_check('data process', 6))
        task10 = tg.create_task(job_check('delete files', 7))
        task11 = tg.create_task(job_check('git push', 8))
        task12 = tg.create_task(job_check('jenkins spin up', 9))
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())