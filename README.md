# Aspect-sentiment-analysis-in-tunisian-dialect

this work aims to study the use of deep machine learning on the analysis of the opinions of the data collected from the social networks (YouTube) in Tunisian dialect to detect the  polarity of each  aspect.
The methodology  consists to  extract of aspects using morphological labeling and ontology 
Scrapping from Youtube.
Pre-processing: Transliteration : We transliterate all Tunisian Arabizi comments into Tunisian Arabic
                Light Stemming. The light stemming consists of eliminating both prefixes and suf-fixes of the word.
                Data cleaning. The aim of the Data cleaning is to remove words, signs and punctua-tions that have no interest for sentiment analysis and that could make                               the learning process time consuming. Thus, we remove all stop words (i.e. also called empty words), URLs, user mentions, punctuation signs                              and duplicated or redundant letters in words. 
 Aspect extraction :	POS based method 
 ![image](https://user-images.githubusercontent.com/104040980/204161099-1a273c4b-5257-44e2-9a5a-cb9caa5bd8d4.png)
                    Ontology based method
  Training with LSTM 
  
![image](https://user-images.githubusercontent.com/104040980/204160869-2d9b9a64-511b-4a8a-8944-c13ff1a33984.png)
