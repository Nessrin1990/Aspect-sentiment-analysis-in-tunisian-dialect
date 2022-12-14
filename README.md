# Aspect-sentiment-analysis-in-tunisian-dialect

this work aims to study the use of deep machine learning on the analysis of the opinions of the data collected from the social networks (YouTube) in Tunisian dialect to detect the  polarity of each  aspect.


The methodology  consists to  extract of aspects using morphological labeling and ontology 
Scrapping from Youtube.
  ![image](https://user-images.githubusercontent.com/104040980/204160869-2d9b9a64-511b-4a8a-8944-c13ff1a33984.png)             


Pre-processing: Transliteration : We transliterate all Tunisian Arabizi comments into Tunisian Arabic.

                Light Stemming. The light stemming consists of eliminating both prefixes and suf-fixes of the word.
                Data cleaning. The aim of the Data cleaning is to remove words, signs and punctua-tions that have no interest for sentiment analysis and that could make                               the learning process time consuming. Thus, we remove all stop words (i.e. also called empty words), URLs, user mentions, punctuation signs                              and duplicated or redundant letters in words. 
                
                
 Aspect extraction :	POS based method 
 
 ![image](https://user-images.githubusercontent.com/104040980/204161099-1a273c4b-5257-44e2-9a5a-cb9caa5bd8d4.png)
                    
 Ontology based method
                    
 
 ![image](https://user-images.githubusercontent.com/104040980/211174144-4e879413-6bd5-4f2b-8945-648e19318c7f.png)

 Training with LSTM 
  
  
  ![image](https://user-images.githubusercontent.com/104040980/211173908-751ad811-654b-4284-8c21-77294b66aa9b.png)

  Training with Bi-GRU


![image](https://user-images.githubusercontent.com/104040980/211173901-d03b27f7-1747-4f2d-8f99-fbc4e5e769dd.png)


Django Application to resume the project.
![image](https://user-images.githubusercontent.com/104040980/211173928-79c898a1-26e0-488d-940a-0a3c1925f783.png)
![image](https://user-images.githubusercontent.com/104040980/211174021-e5b53468-64f9-495c-8d5d-4364762f2b7f.png)


