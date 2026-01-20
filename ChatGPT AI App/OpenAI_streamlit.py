from openai import OpenAI
import streamlit as st

# user add openIA Key Token
gptmodel = "gpt-3.5-turbo"
userrole = "user"

pre_prompt = "teach me the following concept: "

response =""

st.title("ProfessorGPT APP")
st.divider()
prompt = st.text_input("What do you want to learn?")
gptbutton = st.button("Teach Me")
st.caption("ProfessorGPT will work when you press the button" )
st.divider()

if gptbutton:
        with st.spinner("I am preparing your lecture"):
                response = user.chat.completions.create(
                model = gptmodel, 
                messages= [
                        {"role": userrole, "content": pre_prompt + prompt}
                ]

                )
        st.balloons()
        st.write(response.choices[0].message.content)