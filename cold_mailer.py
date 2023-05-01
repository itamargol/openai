from dotenv import load_dotenv
load_dotenv()
import re
import streamlit as st
from langchain import PromptTemplate
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.llms import OpenAI
from langchain.utilities.zapier import ZapierNLAWrapper


llm = OpenAI(temperature=0.7)

zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)

tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(tools + toolkit.get_tools(), llm, agent="zero-shot-react-description")

st.title('ColdMailer')

product = st.text_input('What is the name of the product you\'re selling?')
function = st.text_input('What does your product do?')
prospect = st.text_input('Who is the person you\'re selling to?')
email = st.text_input('Enter the recipient email address', value='elon.musk@gmail.com')

if st.button('Do the magic!'):
    if not product or not function or not prospect:
        st.warning('Please fill in all fields')
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.warning('Please enter a valid email address')
    else:
        try:
            template = """
            # You are Coldy, a cold email outreach expert which is selling {product} with the function {function}.
            Search for a person called {prospect} and craft a cold email with 3 paragraphs that contains introduction about them, how {product} can help them, and book a meeting. Do not label the paragraphs, make sure to start a new line after each paragraph. Send it as email to: {email}.

            (Note: Replace {product}, {function}, {prospect} and {email} with the relevant information before running this code.)"""

            prompt = PromptTemplate(
                input_variables=["product", "function", "prospect", "email"],
                template=template,
            )

            formattedPrompt = prompt.format(product=product, function=function, prospect=prospect, email=email)

            agent.run(formattedPrompt)

            st.success('Email sent successfully!')

        except Exception as e:
            st.error('An error occurred while sending the email: {}'.format(str(e)))
