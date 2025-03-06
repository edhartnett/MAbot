from langchain_community.tools import WikipediaQueryRun 
from langchain_community.utilities import WikipediaAPIWrapper
import streamlit as st
import pandas as pd

class MAbot:
    def __init__(self):
        print("MAbot initialized")

    def main(self):
        print("MAbot main function")
        # api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
        # tool = WikipediaQueryRun(api_wrapper=api_wrapper)
        # results = tool.run("Machine Learning")
        # print(results)
        # st.write(results)
        

if __name__ == "__main__":
    my = MAbot()
    my.main()