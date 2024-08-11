import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="Chatbot", page_icon=":cake:", layout="wide")
st.title("Chatbot")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# get response


def get_response(query, chat_query):
    template = """
    You are a helpful assistant, help me answer the question
    Chat history: {chat_history}
    User question: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI()
    chain = prompt | llm | StrOutputParser()
    chain.invoke({
        'chat_history': chat_query,
        'user_question': query

    })


# conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message('Human'):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message('AI'):
            st.markdown(message.content)

user_query = st.chat_input("Your message: ")
st.write("Bot: Hello! How can I help you today?")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message('Human'):
        st.markdown(user_query)

    with st.chat_message('AI'):
        ai_response = get_response(user_query, st.session_state.chat_history)
        st.markdown(ai_response)
    st.session_state.chat_history.append(AIMessage(ai_response))
