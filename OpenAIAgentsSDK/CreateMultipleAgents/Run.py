#import necessary libraries
from agents import Runner,trace
from front_end_agents import front_end_architect_agent
import asyncio
# Define the main function to run the agent
async def main():    
    # Continuously prompt the user for input until they choose to exit
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break       
        response = await Runner.run(front_end_architect_agent,
        user_input
        )
            #print("Final response:", response)
        print("Result is "+response.final_output)
# Run the main function using asyncio's event loop       
if __name__ == "__main__":
    asyncio.run(main())