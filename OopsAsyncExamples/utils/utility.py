import asyncio

class Utility:
    @staticmethod
    async def async_task(name, delay):
        await asyncio.sleep(delay)
        print(f"Task utility :{name} complete")
        return f"Task {name} completed after {delay} seconds"