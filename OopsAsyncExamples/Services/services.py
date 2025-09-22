
# Import the asyncio library for asynchronous programming
import asyncio

# Define a class to group related service tasks
class services:
    @staticmethod
    async def service_task(name, delay):
        """
        Simulates an asynchronous service task.
        Args:
            name (str): The name of the service.
            delay (int or float): The number of seconds to wait (simulate work).
        Returns:
            str: A message indicating completion.
        """
        # Simulate a delay to represent asynchronous work
        await asyncio.sleep(delay)
        print(f"Service {name} complete")
        return f"Service {name} completed after {delay} seconds"