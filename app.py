import streamlit as st
import pandas as pd
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

st.set_page_config(layout="wide")
st.title('A web app that can help you get individual videos links of a YouTube playlist')
url = st.text_input('Enter YouTube playlist URL here:', '')


if len(url) != 0:
  
  query = parse_qs(urlparse(url).query, keep_blank_values=True)
  playlist_id = query["list"][0]
  youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyBMbhy2LT47Y_ovvahfYSmsjp8-whtFgco")

  request = youtube.playlistItems().list(
      part = "snippet",
      playlistId = playlist_id,
      maxResults = 50
  )
  response = request.execute()

  playlist_items = []
  while request is not None:
      response = request.execute()
      playlist_items += response["items"]
      request = youtube.playlistItems().list_next(request, response)


  for t in playlist_items:
    link = 'https://www.youtube.com/watch?v=' + t["snippet"]["resourceId"]["videoId"] + '&list=' + t["id"] + '&t=0s'
    name = t["snippet"]["title"]
    st.write(f'{[name]}(%s)' % link)
