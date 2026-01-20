from openai import OpenAI
import streamlit as st

user = OpenAI(api_key="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")
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