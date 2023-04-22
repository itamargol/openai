from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain import PromptTemplate
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.llms import OpenAI
from langchain.utilities.zapier import ZapierNLAWrapper

llm = OpenAI(temperature=0)
zapier = ZapierNLAWrapper()

toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
llm = OpenAI(temperature=0.9)

tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(tools + toolkit.get_tools(), llm, agent="zero-shot-react-description", verbose=True)

st.title('Send cold emails with AI')

product = st.text_input('Name of the product youre selling: ') # Launchman
function = st.text_input('What does the product do: ') # Automate your content marketing
prospect = st.text_input('Who is the person youre selling to: ') # Sukh from Launchman

if st.button('Do the magic!'):
  template = """
  # You are Marko, a cold email outreach expert selling {product} with the function {function}.
  Search for a person named {prospect} and craft a cold email with 3 paragraphs that contains introduction about them, how {product} can help them, and book a meeting. Do not label the paragraphs, make sure to start a new line after each paragraph. Send it as email to: sunnyashiin@gmail.com."""

  prompt = PromptTemplate(
      input_variables=["product", "function", "prospect"],
      template=template,
  )

  formattedPrompt = prompt.format(product=product, function=function, prospect=prospect)

  agent.run(formattedPrompt)
