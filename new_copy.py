import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
import uuid
from github import Github
from dotenv import load_dotenv
import os
import collections

import utils



#*************************************#
# Set up github access for "Open in Colab" button.
# TODO: Maybe refactor this to another file.
load_dotenv()  # load environment variables from .env file
if os.getenv("GITHUB_TOKEN") and os.getenv("REPO_NAME"):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(os.getenv("REPO_NAME"))
    colab_enabled = True

    def add_to_colab(notebook):
        """Adds notebook to Colab by pushing it to Github repo and returning Colab link."""
        notebook_id = str(uuid.uuid4())
        repo.create_file(
            f"notebooks/{notebook_id}/generated-notebook.ipynb",
            f"Added notebook {notebook_id}",
            notebook,
        )
        colab_link = f"http://colab.research.google.com/github/{os.getenv('REPO_NAME')}/blob/main/notebooks/{notebook_id}/generated-notebook.ipynb"
        return colab_link


else:
    colab_enabled = False
   



img_dirs = pd.DataFrame()
img_dirs['dir'] = ['Messi','Obama','Jackie_Chan','Daw_Su']

template_dirs = pd.DataFrame()
# list_dir = []
# for f in os.scandir("templates"):
#     for img in os.scandir(f):
#         list_dir.append(img)
# template_dirs['dir'] = list_dir



with st.side_bar:
    option = st.sidebar.selectbox(
    'Select One Person',img_dirs['dir'])    
    
    if (option == 'Messi'):
        for f in os.scandir("templates"):
            if (f is_dir() and f.name == 'Messi'):
                list_dir = []
                for img in os.scandir(f):
                    list_dir.append(img)
        template_dirs['dir'] = list_dir

    if (option == 'Obama'):
        for f in os.scandir("templates"):
            if (f is_dir() and f.name == 'Obama'):
                list_dir = []
                for img in os.scandir(f):
                    list_dir.append(img)
        template_dirs['dir'] = list_dir        
        
    if (option == 'Jackie_Chan'):
        for f in os.scandir("templates"):
            if (f is_dir() and f.name == 'Jackie_Chan'):
                list_dir = []
                for img in os.scandir(f):
                    list_dir.append(img)
        template_dirs['dir'] = list_dir
        
    if (option == 'Daw_Su'):
        for f in os.scandir("templates"):
            if (f is_dir() and f.name == 'Daw_Su'):
                list_dir = []
                for img in os.scandir(f):
                    list_dir.append(img)
        template_dirs['dir'] = list_dir       
                 
    st.selectbox("Choose any one image", template_dirs['dir'])
    st.info(
        "🎈 **NEW:** Add your own code template to this site!"
    )
    


