import pathlib
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from gradio_tools.tools import SAMImageSegmentationTool
from langchain.memory import ConversationBufferMemory


# Initialize a ConversationBufferMemory object to store the chat history
memory = ConversationBufferMemory(memory_key="chat_history")

# Initialize a list of tools to use in the agent
image_segmentation_tool = SAMImageSegmentationTool().langchain
tools = [image_segmentation_tool]

# Specify the path to the Waldo image
waldo = pathlib.Path(__file__).parent / "waldo.jpeg"

# Initialize the agent using the specified tools and memory, and set verbose=True to print debug messages
language_model = OpenAI(temperature=0)
agent = initialize_agent(tools, language_model, memory=memory, agent="conversational-react-description", verbose=True)

try:
    # Prompt the user to find Waldo in the image and provide a description of his appearance
    prompt = f"Please find Waldo in this image: {waldo}. Waldo is a man with glasses wearing a sweater with red and white stripes."
    agent_response = agent.run(input=prompt)

    # Print the agent's response
    print(agent_response)

except Exception as e:
    print(f"An error occurred: {str(e)}")
