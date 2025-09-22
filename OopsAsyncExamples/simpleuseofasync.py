
# Import asyncio for asynchronous programming
import time
import asyncio

# Define three async functions, each simulating a task with a different delay
async def function1():
    await asyncio.sleep(2)  # Wait for 2 seconds
    print("Function 1 complete")
    return "Result from function 1"

async def function2():
    await asyncio.sleep(3)  # Wait for 3 seconds
    print("Function 2 complete")
    return "Result from function 2"

async def function3():
    await asyncio.sleep(1)  # Wait for 1 second
    print("Function 3 complete")
    return "Result from function 3" 

# Main async function to demonstrate parallel and sequential execution
async def main():
    # Run all functions concurrently and wait for all to finish
    values = await asyncio.gather(
        function1(),    
        function2(),
        function3()
    )
    print(values)  # Print the results from all functions

    # If you want to run them sequentially, uncomment the lines below and comment the asyncio.gather above
    # await function1()
    # await function2()
    # await function3()

# Start the async event loop and run main()
asyncio.run(main())


