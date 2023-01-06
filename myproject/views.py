from django.http import HttpResponse
from collections import Counter

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
import pickle
import numpy as np
from gtts import gTTS
import os
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import webbrowser
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import nltk
# import required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
import pandas as pd
import time
import re


def getSentiment(request):
    if request.method == 'POST':
        sentence = request.POST.get('selectBox')
        sentence = str(sentence).lower()
        twt = sentence

        twt = [sentence]
        with open('tokenizer11.pickle', 'rb') as handle:
            loaded_tokenizer = pickle.load(handle)

        seq = loaded_tokenizer.texts_to_sequences(twt)
        padded = pad_sequences(seq, maxlen=196, dtype='int32', value=0)

        model = load_model('sent1.h5')
        model1 = load_model('asp1.h5')

        sentiment = model.predict(padded, batch_size=1, verbose=2)[0]
        aspect = model1.predict(padded, batch_size=1, verbose=2)[0]

        if (np.argmax(sentiment) == 0) & (np.argmax(aspect) == 2):
            return render(request, "home/index.html"
                          , {'twt': sentence, 'result': 'Sentiment is Negative ', 'result1': 'aspect is اكل',
                             })
        elif (np.argmax(sentiment) == 2) & (np.argmax(aspect) == 2):
            return render(request, "home/index.html"
                          , {'twt': sentence, 'result': 'Sentiment is Neutre ', 'result1': 'aspect is اكل'
                             })
        elif (np.argmax(sentiment) == 1) & (np.argmax(aspect) == 2):
            output = gTTS(text=sentence, lang='ar', slow=True)
            output.save("output.wav")
            os.system("start output.wav")
            time.sleep(10)
            output2 = gTTS(text='Sentiment is Positive', lang='en', slow=True)
            output2.save("output2.wav")
            os.system("start output2.wav")
            time.sleep(5)
            output1 = gTTS(text='aspect is ', lang='en', slow=True)
            output1.save("output1.wav")
            os.system("start output1.wav")
            time.sleep(5)
            output11 = gTTS(text='اكل', lang='ar', slow=True)
            output11.save("output11.wav")
            os.system("start output11.wav")
            time.sleep(5)

            return render(request, "home/index.html"
                          , {'twt': sentence, 'result': 'Sentiment is Positive', 'result1': 'aspect is أكل',
                             })
        ####################################################################################################
        elif (np.argmax(sentiment) == 1) & (np.argmax(aspect) == 11):
            output = gTTS(text=sentence, lang='ar', slow=True)
            output.save("output.wav")
            os.system("start output.wav")
            time.sleep(6)
            output2 = gTTS(text='Sentiment is Negative', lang='en', slow=True)
            output2.save("output2.wav")
            os.system("start output2.wav")
            time.sleep(5)
            output1 = gTTS(text='aspect is ', lang='en', slow=True)

            output1.save("output1.wav")
            os.system("start output1.wav")
            time.sleep(5)
            output11 = gTTS(text='سوم', lang='ar', slow=True)

            output11.save("output11.wav")
            os.system("start output11.wav")
            time.sleep(5)
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Negative ', 'result1': 'aspect is سوم',
                           })
        elif (np.argmax(sentiment) == 0) & (np.argmax(aspect) == 11):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Neutre ', 'result1': 'aspect is سوم',
                           })

        elif (np.argmax(sentiment) == 2) & (np.argmax(aspect) == 11):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Positive', 'result1': 'aspect is سوم',
                           })

        ############################################################################

        elif (np.argmax(sentiment) == 0) & (np.argmax(aspect) == 21):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Negative ',
                           'result1': 'aspect is RESTAURANT#GENERAL'})
        elif (np.argmax(sentiment) == 1) & (np.argmax(aspect) == 21):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Neutre', 'result1': 'aspect is RESTAURANT#GENERAL',
                           })
        elif (np.argmax(sentiment) == 2) & (np.argmax(aspect) == 21):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Positive'
                              , 'result1': 'aspect is RESTAURANT#GENERAL'})

        elif (np.argmax(sentiment) == 0) & (np.argmax(aspect) == 0):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Negative ', 'result1': 'aspect is GENERAL',
                           })
        elif (np.argmax(sentiment) == 2) & (np.argmax(aspect) == 0):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Neutre ', 'result1': 'aspect is GENERAL',
                           'result2': 'global prediction is Neutre'})

        elif (np.argmax(sentiment) == 1) & (np.argmax(aspect) == 0):
            return render(request, "accounts/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Positive', 'result1': 'aspect is GENERAL',
                           })

        elif (np.argmax(sentiment) == 0) & (np.argmax(aspect) == 24):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Negative '
                              , 'result1': 'aspect is RESTAURANT#LOCALISATION',
                           })

        elif (np.argmax(sentiment) == 1) & (np.argmax(aspect) == 24):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Positive'
                              , 'result1': 'aspect is RESTAURANT#LOCALISATION',
                           })
        elif (np.argmax(sentiment) == 2) & (np.argmax(aspect) == 24):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Neutre'
                              , 'result1': 'aspect is RESTAURANT#LOCALISATION',
                           })

        elif (np.argmax(sentiment) == 1) & (np.argmax(aspect) == 5):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Negative '
                              , 'result1': 'aspect is RESTAURANT#SERVICE'})

        elif (np.argmax(sentiment) == 2) & (np.argmax(aspect) == 5):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Neutre'
                              , 'result1': 'aspect is RESTAURANT#SERVICE'
                           })
        elif (np.argmax(sentiment) == 0) & (np.argmax(aspect) == 5):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Positive'
                              , 'result1': 'aspect is '})

        elif (np.argmax(sentiment) == 0) & (np.argmax(aspect) == 20):
            output = gTTS(text=sentence, lang='ar', slow=True)
            output.save("output.wav")
            os.system("start output.wav")
            time.sleep(6)
            output2 = gTTS(text='Sentiment is Negative', lang='en', slow=True)
            output2.save("output2.wav")
            os.system("start output2.wav")
            time.sleep(5)
            output1 = gTTS(text='aspect is نظافة', lang='ar', slow=True)
            output1.save("output1.wav")
            os.system("start output1.wav")
            time.sleep(5)
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Negative '
                              , 'result1': 'aspect is RESTAURANT#cleanliness',
                           })
        elif (np.argmax(sentiment) == 2) & (np.argmax(aspect) == 20):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Neutre'
                              , 'result1': 'aspect is RESTAURANT#cleanliness',
                           })
        elif (np.argmax(sentiment) == 1) & (np.argmax(aspect) == 20):
            return render(request, "home/index.html",
                          {'twt': sentence, 'result': 'Sentiment is Positive'
                              , 'result1': 'aspect is RESTAURANT#cleanliness',
                           })
        ####################################################################################################################


def code(request):
    if request.method == 'POST':
        data = []
        with Chrome(executable_path=r'C:\Users\DELL\Desktop\chromedriver') as driver:
            wait = WebDriverWait(driver, 15)
            driver.get("https://www.youtube.com/watch?v=JVouIGogAe0")
            for item in range(50):
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
                time.sleep(15)
            for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
                data.append(comment.text)
        df = pd.DataFrame(data, columns=['comment'])
        df.head()
        df.to_csv(r'C:\Users\DELL\Desktop\commentaires.csv', index=False, header=True)
        print(df)


#dict ={}
def index(request):

    context = {}
    global attribute

    if request.method == 'POST':

        uploaded_file = request.FILES['document']
        attribute = request.POST.get('attributeid')

        print(attribute)

        #check if this file ends with csv
        if uploaded_file.name.endswith('.csv'):
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file) #gets the name of the file
            print(name)


            #we need to save the file somewhere in the project, MEDIA
            #now lets do the savings

            d = os.getcwd() # how we get the current dorectory
            file_directory = d+'\media\\'+name #saving the file in the media directory
            print(file_directory)
            readfile(file_directory)

            request.session['attribute'] = attribute

            if attribute not in data.axes[1]:
                messages.warning(request, 'Please write the column name correctly')
            else:
                print(attribute)
                return redirect(results)

        else:
            messages.warning(request, 'File was not uploaded. Please use .csv file extension!')


    return  render(request, 'home/index.html', context)


            #project_data.csv
def readfile(filename):

    #we have to create those in order to be able to access it around
    # use panda to read the file because i can use DATAFRAME to read the file
    #column;culumn2;column
    global rows,columns,data,my_file,missing_values
     #read the missing data - checking if there is a null
    missingvalue = ['?', '0', '--']

    my_file = pd.read_csv(filename)

    data = pd.DataFrame(data=my_file, index=None)
    print(data)

    rows = len(data.axes[0])
    columns = len(data.axes[1])


    null_data = data[data.isnull().any(axis=1)] # find where is the missing data #na null =['x1','x13']
    missing_values = len(null_data)



def results(request):
    # prepare the visualization
                                #12
    message = 'I found ' + str(rows) + ' rows and ' + str(columns) + ' columns. Missing data: ' + str(missing_values)
    messages.warning(request, message)

    dashboard = [] # ['A11','A11',A'122',]
    for x in data[attribute]:
        dashboard.append(x)

    my_dashboard = dict(Counter(dashboard)) #{'A121': 282, 'A122': 232, 'A124': 154, 'A123': 332}

    print(my_dashboard)

    keys = my_dashboard.keys() # {'A121', 'A122', 'A124', 'A123'}
    values = my_dashboard.values()

    listkeys = []
    listvalues = []

    for x in keys:
        listkeys.append(x)

    for y in values:
        listvalues.append(y)

    print(listkeys)
    print(listvalues)

    context = {
        'listkeys': listkeys,
        'listvalues': listvalues,
    }

    return render(request, 'results.html', context)
