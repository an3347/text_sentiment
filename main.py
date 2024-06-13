import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer

st.title("Identify the sentiments by Paragraph(s)")

analyzer = SentimentIntensityAnalyzer()

paragraphs = st.text_area("Input the text to analyze sentiment: ")
findings = paragraphs.split("\n")

i = 0
output = ""
for key, value in enumerate(findings):
    if value == "":
        i += 1
    else:
        score = analyzer.polarity_scores(value)
        if score["pos"] > score["neg"]:
            output += f"paragraph {key + 1 - i} is a positive paragraph" + "\n"
        elif score["neg"] > score["pos"]:
            output += f"paragraph {key + 1 - i} is a negative paragraph" + "\n"
        else:
            output += f"paragraph {key + 1 - i} is a neutral paragraph" + "\n"

st.text(output)

if paragraphs != "":
    score = analyzer.polarity_scores(paragraphs)
    if score["pos"] > score["neg"]:
        st.text("overall it is a positive text")
    elif score["neg"] > score["pos"]:
        st.text("overall it is a negative text")
    else:
        st.text("overall it is a neutral text")

    # print(findings)
