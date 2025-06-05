import  streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # kind of like makes a new variable that puts what is writen in text_input
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a todo app")
st.write("This app is to improve productivity")


for index , todo in enumerate(todos):
     checkbox = st.checkbox(todo, key=todo)
     if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo",
              on_change=add_todo, key= 'new_todo')

print("hello")

st.session_state

