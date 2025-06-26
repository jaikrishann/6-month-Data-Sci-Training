import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import time

# Page configuration
st.set_page_config(
    page_title="Streamlit Function Demo",
    page_icon="🧪",
    layout="wide"
)

# Session state example
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Title and text elements
st.title("🧪 Streamlit All-in-One Demo")
st.header("1. Text Elements")
st.subheader("Markdown, Code, LaTeX")
st.markdown("**Bold**, *italic*, and `code` text")
st.code("print('Hello Streamlit!')", language='python')
st.latex(r"E = mc^2")

st.divider()

# Metrics and messages
st.header("2. Metrics and Status")
st.metric(label="Revenue", value="$120K", delta="+10%")
st.success("Success message")
st.info("Info message")
st.warning("Warning message")
st.error("Error message")
try:
    raise ValueError("This is a test exception")
except Exception as e:
    st.exception(e)

st.divider()

# Data display
st.header("3. Data Display")
df = pd.DataFrame({
    "A": np.random.randn(5),
    "B": np.random.rand(5),
})
st.write("Write function detects types:", df)
st.dataframe(df)
st.table(df.head(3))
st.json({"name": "Streamlit", "version": 1.32, "features": ["widgets", "charts"]})

st.divider()

# Charts
st.header("4. Charts and Visualization")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

chart = alt.Chart(df.reset_index()).mark_line().encode(
    x='index', y='A'
)
st.altair_chart(chart, use_container_width=True)

fig, ax = plt.subplots()
ax.plot(df["A"])
st.pyplot(fig)

st.divider()

# Widgets
st.header("5. Input Widgets")

with st.form("input_form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age", 1, 100)
    mood = st.radio("Your mood", ["Happy", "Neutral", "Sad"])
    languages = st.multiselect("Languages you know", ["Python", "Java", "C++", "JS"])
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Hi {name}, age {int(age)}. Mood: {mood}, Languages: {languages}")

col1, col2 = st.columns(2)
with col1:
    number = st.slider("Choose a number", 0, 100)
with col2:
    color = st.color_picker("Pick a color", "#00f900")

st.text_area("Write something...")
file = st.file_uploader("Upload a file")
st.date_input("Pick a date")
st.time_input("Pick a time")

if st.button("Increment Counter"):
    st.session_state.counter += 1
st.write("Counter value:", st.session_state.counter)

st.divider()

# Media
st.header("6. Media")
st.image("https://picsum.photos/400", caption="Random Image")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.divider()

# Sidebar and layout
st.sidebar.title("Sidebar Menu")
option = st.sidebar.selectbox("Choose section", ["Intro", "Charts", "Widgets"])

st.header("7. Layout: Columns, Containers, Expanders")

with st.container():
    st.write("This is inside a container")

col1, col2 = st.columns(2)
col1.write("Column 1")
col2.write("Column 2")

with st.expander("Click to expand"):
    st.write("Hidden content inside expander")

st.divider()

# Cache
st.header("8. Cached Function Demo")

@st.cache_data
def load_data():
    time.sleep(2)
    return pd.DataFrame(np.random.randn(100, 3), columns=["X", "Y", "Z"])

if st.button("Load Cached Data"):
    data = load_data()
    st.success("Data loaded (with caching)")
    st.dataframe(data.head())

st.divider()

# Toast & Spinner
st.header("9. Feedback")

with st.spinner("Loading..."):
    time.sleep(1)
st.toast("Done loading!", icon="🎉")

st.divider()

# Query params (basic example)
st.header("10. URL Query Parameters")
params = st.query_params
st.write("Query params:", params)

st.page_link("https://streamlit.io", label="Open Streamlit site", icon="🌐")

st.success("✅ Demo completed!")
