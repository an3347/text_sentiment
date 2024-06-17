import streamlit as st
import nltk
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
st.title("Identify the sentiments by Paragraph(s)")

analyzer = SentimentIntensityAnalyzer()

paragraphs = st.text_area("Input the text to analyze sentiment: ")
findings = paragraphs.split("\n")

negative = []
positive = []
neutral = []
para_count = []
i = 0
p = 0
output = ""
for key, value in enumerate(findings):
    if value == "":
        i += 1
    else:
        score = analyzer.polarity_scores(value)
        p += 1
        positive.append(score["pos"] * 100)
        negative.append(score["neg"] * 100)
        neutral.append(score["neu"] * 100)
        para_count.append(p)
        if score["pos"] > score["neg"]:
            output += f"paragraph {key + 1 - i} is a positive paragraph" + "\n"
        elif score["neg"] > score["pos"]:
            output += f"paragraph {key + 1 - i} is a negative paragraph" + "\n"
        else:
            output += f"paragraph {key + 1 - i} is a neutral paragraph" + "\n"

if paragraphs != "":
    score = analyzer.polarity_scores(paragraphs)

    st.subheader("Positive Sentiment Chart of Paragraph")
    pos_figure_p = px.line(x=para_count, y=positive, labels={"x": "Paragraph ", "y": "Positivity"})
    st.plotly_chart(pos_figure_p)

    st.subheader("Neutral Sentiment Chart of Paragraph")
    pos_figure_p = px.line(x=para_count, y=negative, labels={"x": "Paragraph ", "y": "Neutrality"})
    st.plotly_chart(pos_figure_p)

    st.subheader("Negative Sentiment Chart of Paragraph")
    pos_figure_n = px.line(x=para_count, y=negative, labels={"x": "Paragraph ", "y": "Negativity"})
    st.plotly_chart(pos_figure_n)

    st.text(output)

    if score["pos"] > score["neg"]:
        st.text("overall it is a positive text")
    elif score["neg"] > score["pos"]:
        st.text("overall it is a negative text")
    else:
        st.text("overall it is a neutral text")


    # print(findings)
