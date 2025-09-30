from agents import Runner,trace
from assistant import first_agent 
import asyncio
async def main():
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        with trace("find answer"):
            response = await Runner.run(first_agent,
            user_input
            )
            #print("Final response:", response)
            print("Result is "+response.final_output)
        
if __name__ == "__main__":
    asyncio.run(main())

