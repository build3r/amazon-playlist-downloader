# Amazon Music Playlist Downloader
A script to download and generate playist file from Amazon music

## Steps to use
1. To amazon music app, open your playlist and click on share playlist
2. open the playlist on a browswer
3. Open DevTools (F12) and go to network tab.
4. Reload the page 
5. Look for entry `showHome` , right click and copy request as curl.  
    ![image](https://user-images.githubusercontent.com/6481548/212118731-ba18104f-033f-4af0-af5b-f0babc5bde93.png)
6. Open terminal and paste the curl request and save the response to a file called **playlist.json**. (The output is huge so better always save to file)  
  ex:  
  ```
    <curl req from step 5> -o playlist.json
  ```
