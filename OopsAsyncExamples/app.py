
# Import asyncio for asynchronous programming
import asyncio
# Import the services class and Utility class from their respective modules
from Services.services import services
from utils.utility import Utility

# Define the main asynchronous function
async def main():
    # Create async tasks for services and utilities
    service1 = services.service_task("A", 2)  # Service A with 2s delay
    service2 = services.service_task("B", 3)  # Service B with 3s delay
    utility1 = Utility.async_task("X", 1)     # Utility X with 1s delay
    utility2 = Utility.async_task("Y", 4)     # Utility Y with 4s delay

    # Run all tasks concurrently and wait for all to finish
    results = await asyncio.gather(service1, service2, utility1, utility2)
    # Print the result of each completed task
    for result in results:
        print(result)

# Run the main async function using asyncio's event loop
asyncio.run(main())