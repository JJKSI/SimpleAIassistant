import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import subprocess,sys
import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():  # this function nis useful for taking the input fom the user
    r= sr.Recognizer()# taking input from user
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
           query=r.recognize_google(audio,language='en-in')
           print(f'User said {query}')
           return query
        except Exception as e:
            return 'There is some error'

if __name__ == '__main__':
    print('Pycharm')
    say('hello i am your assistant how may i help you')
    while True: #todo: add more sites
        print('Listening....')
        query = takecommand()
        sites=[['youtube','https://www.youtube.com/'],['whatsapp','https://web.whatsapp.com/'],['github','https://github.com/'],['chatgpt','https://chat.openai.com/']]
        for site in sites:
            if f'Open {site[0]}'.lower() in query.lower():
                say(f'Opening {site[0]}')
                webbrowser.open(site[1])
        if 'open video' in query:
            videopath='D:/Movies and Series/A Miracle'
            opener='open' if sys.platform =='darwin' else 'xdg-open'
            subprocess.call([opener,videopath])
        if 'the time' in query:
            strf=datetime.datetime.now().strftime("%H:%M")
            say(f'the time is {strf}')
        if 'The project'.lower() in query.lower():# todo add more paths of your os system
            projectpath = 'D:/Personals/!_Projects'
            subprocess.Popen(['explorer', projectpath])
        if 'search' in query.lower():
            search_query = query.split('search', 1)[1].strip()
            say(f'Searching for {search_query}')
            webbrowser.open(f'https://www.google.com/search?q={search_query}')
        if 'play music' in query.lower():
            search_query = query.split('play music', 1)[1].strip()
            say('Opening music from YouTube')
            playlist_url = 'https://www.youtube.com/playlist?list=LL'
            webbrowser.open(playlist_url)
           
            # Extract the video ID from the playlist URL
            video_id = playlist_url.split('list=LL')[1].split('&')[0]

            # Open the URL of the first video separately
            video_url = f'https://www.youtube.com/watch?v=oRGDhgITetc&list=LL&index=1&ab_channel=ProvedRecords'
            webbrowser.open(video_url)
            
            current_index = 1  # Index of the current video

            while True:
                if 'next music' in query.lower():
                    current_index += 1
                    video_url = f'{playlist_url}&index={current_index}'
                    webbrowser.open(video_url)
                    break
                else:
                    query = takecommand()    
        # say(query)'
