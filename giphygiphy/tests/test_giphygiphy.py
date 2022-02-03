from giphygiphy import giphygiphy

import requests
import os
import json
import pandas as pd
import numpy as np
import IPython
import warnings
from IPython.display import Image, HTML
from dotenv import load_dotenv, find_dotenv
load_dotenv()
MY_KEY = os.environ.get("giphy_api_key")
warnings.filterwarnings("ignore")


def test_get_info():
    params = {'api_key':MY_KEY, 'limit': 5, "rating": "g"}
    actual = giphygiphy.get_info(params)
    print(actual)
    assert type(actual) == pd.DataFrame, "Failed - not a pd.DataFrame"
    
def test_search():
    params = {'api_key':MY_KEY, 'q': "finals week", "limit":3}
    actual = giphygiphy.search(params)
    
    assert type(actual) == pd.DataFrame, "Failed - not a pd.DataFrame"

def test_display_by():
    params = {'api_key':MY_KEY, 's': "dog in fire", "weirdness":0}
    actual = giphygiphy.display_by(params)
    
    assert type(actual) == type(HTML()), "Failed - not a HTML"
    
def test_random():
    params = {'api_key':MY_KEY}
    actual = giphygiphy.random(params)
    
    assert type(actual) == pd.DataFrame, "Failed - not a pd.DataFrame"
    
def test_display_random():
    params = {'api_key':MY_KEY}
    actual = giphygiphy.display_random(params)
    
    assert type(actual) == type(HTML()), "Failed - not a HTML"
    
def test_id_info():
    params = {'api_key':MY_KEY, "ids":"xT4uQulxzV39haRFjG, AvPJoxrwK1UmkQNuEj"}
    actual = giphygiphy.id_info(params)
    
    assert type(actual) == pd.DataFrame, "Failed - not a pd.DataFrame"
    
def test_trending():
    params = {'api_key':MY_KEY}
    actual = giphygiphy.trending(params)
    
    assert type(actual) == pd.DataFrame, "Failed - not a pd.DataFrame"
    
    
    