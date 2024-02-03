import streamlit as st
import pickle
import os
import os.path
import pandas as pd
import psycopg2
import psycopg2.extras as extras
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from tabulate import tabulate
import warnings
warnings.filterwarnings("ignore")

HOST= st.secrets["HOST"]
DATABASE= st.secrets["DATABASE"]
USER= st.secrets["USER"]
PORT= st.secrets["PORT"]
PASSWORD= st.secrets["PASSWORD"]

BACKUP_CRED= st.secrets["BACKUP_CRED"]
with open('credentials.json', 'w') as fp:
    json.dump(json_cred, fp)

st.write("Hello-world!")