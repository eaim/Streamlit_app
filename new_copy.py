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






# template_dict = collections.defaultdict(dict)
# template_dirs = [
#     f for f in os.scandir("templates") if f.is_dir() and f.name != "example"
# ]
# # TODO: Find a good way to sort templates, e.g. by prepending a number to their name
# #   (e.g. 1_Image classification_PyTorch).
# template_dirs = sorted(template_dirs, key=lambda e: e.name)
# for template_dir in template_dirs:
#     try:
#         # Templates with task + framework.
#         task, framework = template_dir.name.split("_")
#         template_dict[task][framework] = template_dir.path
#     except ValueError:
#         # Templates with task only.
#         template_dict[template_dir.name] = template_dir.path
# # print(template_dict)


# template_dirs = pd.DataFrame()
# template_dirs['dir'] = [
#     f for f in os.scandir("templates") if f.is_dir() 
# ]

# # template_dirs= sorted(template_dirs, key=lambda e: e.name)
# st.write(template_dirs['dir'])

for f in os.scandir("templates"):
    if f.is_dir():
        st.write(f)
    else:
        st.write('nothing')
        
     

                      



# with st.sidebar:
#     st.info(
#         "🎈 **NEW:** Add your own code template to this site! [Guide](https://github.com/jrieke/traingenerator#adding-new-templates)"
#     )
#     # st.error(
#     #     "Found a bug? [Report it](https://github.com/jrieke/traingenerator/issues) 🐛"
#     # )
#     st.write("## Task")
#     task = st.selectbox(
#         "Which problem do you want to solve?", template_dirs['dir']
#     )
#     if isinstance(template_dict[task], dict):
#         framework = st.selectbox(
#             "In which framework?", list(template_dict[task].keys())
#         )
#         template_dir = template_dict[task][framework]
#     else:
#         template_dir = template_dict[task]
#*************************************#
# st.header('Here are some of the countries data in each region')

