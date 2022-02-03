import requests
import os
import json
import pandas as pd
import numpy as np
import IPython
import warnings
warnings.filterwarnings("ignore")

def get_info(params):
    """
    Get the fullest information from the latest trending gifs online, including info such as unique ID,
    name of the gif, author, and url.

    Parameters
    ----------
    api_key : (required) a string, personal API Key obtained through GIPHY;
    limit   : an integer, maximum number of objects to return;
    rating  : a string, filtering the results by rating g, pg, pg-13, and r (No specification = no filter);
            
    Returns
    -------
    A dataframe containing Gif ID, Title, Rating, Author, Date created on, URL, Source URL.
    

    Examples
    --------
    >>> from giphygiphy import giphygiphy
    >>> params = {'api_key':MY_KEY, 'limit': 5, "rating": "g"}
    >>> giphygiphy.get_info(params)
    ID	Title	Rating	Author	Created on	URL	Source URL
    0	nSDfhKd9gU4iCK9o2n	Jason Statham Manager GIF by Operation Fortune	g	OperationFortune	2021-12-10 00:01:09 https://gph.is/g/4DMxxvP	
    1	PLiW6toBco3wu2lqY0	Tired Good Night GIF by Muffin & Nuts	g	muffinnuts	2021-07-16 08:42:03	https://gph.is/g/Zr8lOey	
    2	PCzENn4nBHUnvsLJUN	Will Forte Snl GIF by MacGruber	g	MacGruber	2021-11-15 20:37:45	https://gph.is/g/E1BQB01	https://www.peacocktv.com/
    3	xUOxfcsFhVkd0UOsdW	Happy Birthday Reaction GIF	g		2017-11-06 21:40:24	http://gph.is/2ha7xvc	https://media.giphy.com/media/6nuiJjOOQBBn2/gi...
    4	h0RyoXY6Pp5O5nrl2K	I Love You GIF	g	dotdave	2021-11-11 11:52:45	https://gph.is/g/ZlrQq5K	https://www.3danimatedgifs.com/
    """
    
    try:
        r = requests.get('http://api.giphy.com/v1/gifs/trending', params = params)
        r.raise_for_status()
        
    except:
        print("There is something wrong with your input!")
        
    else:
        gif = r.json()
        gifinfo = pd.DataFrame(gif["data"])
        gifinfo_new = gifinfo[["id","title", "rating", "username", "import_datetime","bitly_url", "source", "embed_url"]]
        gifinfo_new.rename(columns = {"id":"ID", "title":"Title","rating":"Rating",
                                      "username":"Author", "import_datetime":"Created on",
                                      "bitly_url":"URL", "source":"Source URL", "embed_url":"Embed URL"}, inplace = True)
        return gifinfo_new
    
def search(params):
    """
    Get the fullest useful information for gifs online based on the user search term, including info such as unique ID,
    name of the gif, author, and url.

    Parameters
    ----------
    api_key : (required) a string, personal API Key obtained through GIPHY
    q       : (required) a string, search query term or phrase
    limit   : an integer, maximum number of objects to return
    rating  : a string, filtering the results by rating include g, pg, pg-13, r. No specification = no filter
            
    Returns
    -------
    A dataframe containing Gif ID, Title, Rating, Author, Date created on, URL, Source URL.
    

    Examples
    --------
    >>> from giphygiphy import giphygiphy
    >>> params = {'api_key':MY_KEY, 'q': "finals week", "limit":3}
    >>> giphygiphy.search(params)
    ID	Title	Rating	Author	Created on	URL	Source URL
    0	lChoLVeVhUDYYSOECk	Studying Sun Devils GIF by Arizona State Unive...	g	ASUofficial	2020-12-03 22:46:45	https://gph.is/g/Z2po3AW	www.asu.edu
    1	uovsUbA0WPcSQ	study hard college life GIF by MTVU	pg	MTVU	2017-05-09 21:06:10	http://gph.is/2psYd7r	
    2	gJMLefNc8YpSW3wIYD	School College GIF by GIPHY Studios Originals	g	studiosoriginals	2021-05-05 22:13:44	https://gph.is/g/4wYQoG2	
    
    """
    
    try:
        r = requests.get('http://api.giphy.com/v1/gifs/search', params = params)
        r.raise_for_status()
        
    except Exception as err:
        print(f'Other error occurred: {err}')
        
    else:
        gif = r.json()
        gifinfo = pd.DataFrame(gif["data"])
        gifinfo_new = gifinfo[["id","title", "rating", "username", "import_datetime","bitly_url", "source", "embed_url"]]
        gifinfo_new.rename(columns = {"id":"ID", "title":"Title","rating":"Rating",
                                      "username":"Author", "import_datetime":"Created on",
                                      "bitly_url":"URL", "source":"Source URL", "embed_url":"Embed URL"}, inplace = True)
        return gifinfo_new
    

def display_by(params):
    """
    Display a most relevant gif in jupyter notebook based on words or phrases inputed by the users, could be adjust by 'weirdness'.

    Parameters
    ----------
    api_key  : (required) a string, personal API Key obtained through GIPHY
    s        : (required) a string, search query term or phrase
    weirdness: an int, 0-10 scale, the higher it is the weirder it goes

    Returns
    -------
    Displaying a gif embeded in jupyter notebook with URL displayed
    
    
    Examples
    --------
    >>> from giphygiphy import giphygiphy
    >>> params = {'api_key':MY_KEY, 's': "dog in fire", "weirdness":0}
    >>> giphygiphy.display_by(params)
    https://giphy.com/embed/UKF08uKqWch0Y
    <gif displayed here>
    """
    
    try:
        r = requests.get('http://api.giphy.com/v1/gifs/translate', params = params)
        r.raise_for_status()
        
    except:
        print("There is something wrong with your input!")
        
    else:
        import IPython
        gif = r.json()
        gifinfo = pd.DataFrame(gif["data"])
        URL = gifinfo[["embed_url"]].iloc[0]["embed_url"]
        iframe = '<iframe src=' + URL + ' width=700 height=350></iframe>'
        print(URL)

        return IPython.display.HTML(iframe)
    

def random(params):
    """
    Get information for a completely random gif in GIPHY library

    Parameters
    ----------
    api_key : (required) a string, personal API Key obtained through GIPHY
            
    Returns
    -------
    A one row dataframe containing Gif ID, Title, Rating, Author, Date created on, URL, Source URL, Embed URL.
    

    Examples
    --------
    >>> from giphygiphy import giphygiphy
    >>> params = {'api_key':MY_KEY}
    >>> giphygiphy.random(params)
    	ID	Title	Rating	Author	Created on	URL	Source URL	Embed URL
        hd	AvPJoxrwK1UmkQNuEj	Womens Basketball GIF by Basketfem	g	basketfem	2021-09-19 08:53:27	https://gph.is/g/Z7v95Dp		https://giphy.com/embed/AvPJoxrwK1UmkQNuEj
    """
    
    try:
        r = requests.get('http://api.giphy.com/v1/gifs/random', params = params)
        r.raise_for_status()
        
    except:
        print("There is something wrong with your input!")
        
    else:
        gif = r.json()
        gifinfo = pd.DataFrame(gif["data"])
        gifinfo_new = gifinfo[["id","title", "rating", "username", "import_datetime","bitly_url", "source", "embed_url"]]
        gifinfo_new.rename(columns = {"id":"ID", "title":"Title","rating":"Rating",
                                      "username":"Author", "import_datetime":"Created on",
                                      "bitly_url":"URL", "source":"Source URL", "embed_url":"Embed URL"}, inplace = True)
        return gifinfo_new.iloc[[0]]
    
def display_random(params):
    """
    Display a completely random gif in the GIPHY library

    Parameters
    ----------
    api_key  : (required) a string, personal API Key obtained through GIPHY

    Returns
    -------
    Displaying a gif embeded in jupyter notebook with URL displayed
    
    
    Examples
    --------
    >>> from giphygiphy import giphygiphy
    >>> params = {'api_key':MY_KEY}
    >>> giphygiphy.display_random(params)
    https://giphy.com/embed/Z2A5txD62TwE5JeBua
    <gif displayed here>
    """
    
    try:
        r = requests.get('http://api.giphy.com/v1/gifs/random', params = params)
        r.raise_for_status()
        
    except:
        print("There is something wrong with your input!")
        
    else:
        import IPython
        gif = r.json()
        gifinfo = pd.DataFrame(gif["data"])
        URL = gifinfo[["embed_url"]].iloc[0]["embed_url"]
        iframe = '<iframe src=' + URL + ' width=700 height=350></iframe>'
        print(URL)

        return IPython.display.HTML(iframe)
    
def id_info(params):
    """
    Get information for specific Gifs based on the specified IDs input by the users

    Parameters
    ----------
    api_key : (required) a string, personal API Key obtained through GIPHY;
    ids     : (required) a string, filters results by specificed GIF IDs, separated by commas;
            
    Returns
    -------
    A dataframe containing Gif ID, Title, Rating, Author, Date created on, URL, Source URL.
    

    Examples
    --------
    >>> from giphygiphy import giphygiphy
    >>> params = {'api_key':MY_KEY, "ids":"xT4uQulxzV39haRFjG, AvPJoxrwK1UmkQNuEj"}
    >>> giphygiphy.id_info(params)
        ID	Title	Rating	Author	Created on	URL	Source URL	Embed URL
        0	xT4uQulxzV39haRFjG	Happy Cinco De Mayo GIF by Ethan Barnowsky	pg	ethanbarnowsky	2016-05-05 14:25:59	http://gph.is/1ZhShKr	www.ethanbarnowsky.com	https://giphy.com/embed/xT4uQulxzV39haRFjG
        1	AvPJoxrwK1UmkQNuEj	Womens Basketball GIF by Basketfem	g	basketfem	2021-09-19 08:53:27	https://gph.is/g/Z7v95Dp		https://giphy.com/embed/AvPJoxrwK1UmkQNuEj
    """
    
    try:
        r = requests.get('http://api.giphy.com/v1/gifs', params = params)
        r.raise_for_status()
        
    except:
        print("There is something wrong with your input!")
        
    else:
        gif = r.json()
        gifinfo = pd.DataFrame(gif["data"])
        gifinfo_new = gifinfo[["id","title", "rating", "username", "import_datetime","bitly_url", "source", "embed_url"]]
        gifinfo_new.rename(columns = {"id":"ID", "title":"Title","rating":"Rating",
                                      "username":"Author", "import_datetime":"Created on",
                                      "bitly_url":"URL", "source":"Source URL", "embed_url":"Embed URL"}, inplace = True)
        return gifinfo_new
    
    
def trending(params):
    """
    Get a list of most popular trending search terms on GIPHY network

    Parameters
    ----------
    api_key : (required) a string, personal API Key obtained through GIPHY;
            
    Returns
    -------
    A dataframe containing Rankings and Trending Terms
    

    Examples
    --------
    >>> from giphygiphy import giphygiphy
    >>> params = {'api_key':MY_KEY}
    >>> giphygiphy.trending(params)
        Rankings Trending Term
            1   grateful
            2	friday morning
            3	happy friday
            4	fri-yay
            5	happy anniversary
            6	good morning
            7	buenosdias
            8	spiderman
            9	merry christmas
            10	beautiful
            11	congratulations
            12	prayers
            13	thank
            14	birthday
            15	love
            16	kiss
            17	daniel
            18	i love
            19	dancing
            20	christmas
    """
    try:
        r = requests.get('http://api.giphy.com/v1/trending/searches', params = params)
        r.raise_for_status()
        
    except:
        print("There is something wrong with your input!")
        
    else:
        gif = r.json()
        gifinfo = pd.DataFrame(gif["data"])
        gifinfo.index = gifinfo.index+1
        gifinfo_new = gifinfo.reset_index()
        gifinfo_new.rename(columns = {"index": "Rankings", 0:"Trending Term"}, inplace = True)

        return gifinfo_new
   