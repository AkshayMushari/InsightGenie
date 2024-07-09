
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Langchain environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Data:\n{data}\n\nQuestion: {question}")
    ]
)

# Streamlit framework
st.title('Langchain Demo With LLAMA2 API')

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
input_text = st.text_input("Ask a question about the data")

if uploaded_file:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Data preview:")
    st.write(df.head())

    # Initialize Ollama Llama2 LLM
    llm = Ollama(model="llama2")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    if input_text:
        formatted_prompt = {"data": df.to_string(index=False), "question": input_text}
        response = chain.invoke(formatted_prompt)
        st.write(response)

    # Histograms for all numeric columns
    st.write("Histograms:")
    numeric_columns = df.select_dtypes(include=['number']).columns
    for column in numeric_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], bins=30, kde=True)
        plt.title(f'Histogram of {column}')
        st.pyplot(plt.gcf())

    # Scatter plots for numeric columns
    st.write("Scatter Plots:")
    for i, column1 in enumerate(numeric_columns):
        for column2 in numeric_columns[i+1:]:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=df[column1], y=df[column2])
            plt.title(f'Scatter Plot: {column1} vs {column2}')
            st.pyplot(plt.gcf())

    # Line plots for numeric columns
    st.write("Line Plots:")
    for column in numeric_columns:
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df[column])
        plt.title(f'Line Plot of {column}')
        st.pyplot(plt.gcf())

    # Generate pair plot for both numeric and non-numeric data
    st.write("Pair Plot:")
    pair_plot = sns.pairplot(df, kind='scatter', diag_kind='kde')
    st.pyplot(pair_plot.fig)

    # Generate heatmap for numeric data correlations
    if numeric_columns.shape[0] > 1:
        st.write("Correlation Heatmap:")
        plt.figure(figsize=(10, 6))
        sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")
        st.pyplot(plt.gcf())

    # Count plots for categorical data
    st.write("Categorical Data Distributions:")
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for column in categorical_columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(y=column, data=df, order=df[column].value_counts().index)
        plt.title(f'Distribution of {column}')
        st.pyplot(plt.gcf())
