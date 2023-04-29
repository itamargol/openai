### This file sets up a conversational agent that uses OpenAI's language model and Meta's SAM image segmentation to describe the appearance of Waldo in a given image. 
### The user inputs a prompt asking to find Waldo and the agent provides a response with a description of his appearance.

import pathlib
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from gradio_tools.tools import SAMImageSegmentationTool
from langchain.memory import ConversationBufferMemory

llm = OpenAI(temperature=0)

# Initialize a ConversationBufferMemory object to store the chat history
memory = ConversationBufferMemory(memory_key="chat_history") 

# Initialize a list of tools to use in the agent
tools = [SAMImageSegmentationTool().langchain]

# Specify the path to the Waldo image
waldo = pathlib.Path(__file__).parent / "waldo.jpeg" 

# Initialize the agent using the specified tools and memory, and set verbose=True to print debug messages
agent = initialize_agent(tools, llm, memory=memory, agent="conversational-react-description", verbose=True) 

# Prompt the user to find Waldo in the image and provide a description of his appearance
output = agent.run(input=(f"Please find Waldo in this image: {waldo}. "
                         "Waldo is a man with glasses wearing a sweater with red and white stripes."))

# Print the agent's response
print(output)
