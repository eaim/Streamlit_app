import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
# import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf
# from jinja2 import Environment, FileSystemLoader
# import uuid
# from github import Github
# from dotenv import load_dotenv
import os
# import collections

# import utils



#*************************************#
# Set up github access for "Open in Colab" button.
# TODO: Maybe refactor this to another file.
# load_dotenv()  # load environment variables from .env file
# if os.getenv("GITHUB_TOKEN") and os.getenv("REPO_NAME"):
#     g = Github(os.getenv("GITHUB_TOKEN"))
#     repo = g.get_repo(os.getenv("REPO_NAME"))
#     colab_enabled = True

#     def add_to_colab(notebook):
#         """Adds notebook to Colab by pushing it to Github repo and returning Colab link."""
#         notebook_id = str(uuid.uuid4())
#         repo.create_file(
#             f"notebooks/{notebook_id}/generated-notebook.ipynb",
#             f"Added notebook {notebook_id}",
#             notebook,
#         )
#         colab_link = f"http://colab.research.google.com/github/{os.getenv('REPO_NAME')}/blob/main/notebooks/{notebook_id}/generated-notebook.ipynb"
#         return colab_link


# else:
#     colab_enabled = False
   
#*************************************#

#*************************************#


img_dirs = pd.DataFrame()
img_dirs['dir'] = ['Messi','Obama','Jackie_Chan','Daw_Su']

template_dirs = pd.DataFrame()
template_dirs['dir'] = None
# list_dir = []
# for f in os.scandir("templates"):
#     for img in os.scandir(f):
#         list_dir.append(img)
# template_dirs['dir'] = list_dir



with st.sidebar:
    option = st.sidebar.selectbox(
    'Select One Person',img_dirs['dir'])
    
    def load_img(name):
        for f in os.scandir("templates"):
            if (f.is_dir() and f.name == name):
                list_dir = []
                for img in os.scandir(f):
                    list_dir.append(img.name)
        template_dirs['dir'] = list_dir
    
    load_img(option)
                        
    img_file = st.selectbox("Choose any one image", template_dirs['dir'])
    st.info("Copyright@Anonymous")





#*****************************************#
#loading model file and test

# import urllib.request
# import zipfile
# from io import BytesIO

#url = 'https://github.com/Rajkap/Streamlit_app/blob/691694146b2baf55ed03dead842aa2b2d3e90224/model_file.zip'
#z = zipfile.ZipFile(BytesIO(urllib.request.urlopen(url).read()))
#z.extractall()



import os
from zipfile import ZipFile
work_dir = os.getcwd()                                                  #Saves the current working directory.
print(work_dir)
# st.write(work_dir)
with ZipFile(os.path.join(work_dir ,'model_file.zip'),'r') as zipobject:
  zipobject.extractall() 
path = os.scandir(work_dir)
# st.write(path)
model_path = None
for f in path:
     if f.name == 'model_face_recog_eg1 - Copy.h5':
         model_path = f


model_file = tf.keras.models.load_model(model_path)


#path = input('Enter the path of your image in order to predict:')
img_path = 'https://github.com/Rajkap/Streamlit_app/blob/691694146b2baf55ed03dead842aa2b2d3e90224/templates/'+option+'/'+img_file
st.write(img_path)
import matplotlib.pyplot as plt
img = tf.keras.preprocessing.image.load_img(path, target_size=(160,160))
plt.imshow(tf.keras.preprocessing.image.load_img(path))
dictionary = {0:'Daw Aung San SuuKyi',1:'Jackie Chan',2:'Messi',3:'Barack Obama'}
x = tf.keras.preprocessing.image.img_to_array(img)
x = np.expand_dims(x,axis=0)
x /= 255.0
images = np.vstack([x])
classes = model_file.predict(x)
y_classes=classes.argmax(axis=-1)
label = y_classes[0]#9
#print(label)
print("Model မှခန့်မှန်း လိုက်သော အဖြေမှာ ",dictionary[label], "ဖြစ်ပါသည်။")
