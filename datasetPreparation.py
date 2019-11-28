# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:58:03 2019

@author: Sakshu
"""
import os, shutil
#import easygui

af=0
an=0
di=0
ha=0
ne=0
sa=0
su=0

path='C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\KDEF'
for files in os.listdir():
    for file in os.listdir(files):
        print(file)
        
        if files+'AF' in file:
            new= path+'\\'+files+'\\'+'Afraid_'+str(af)+'.jpg'
            os.rename(path+'\\'+files+'\\'+file, new)
            shutil.copy(new,'C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\Afraid')
            af+= 1
            
        if 'AN' in file:
            new= path+'\\'+files+'\\'+'Angry_'+str(an)+'.jpg'
            os.rename(path+'\\'+files+'\\'+file, new)
            shutil.copy(new,'C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\Angry')
            an+= 1
    
        if 'DI' in file:
            new= path+'\\'+files+'\\'+'Disgusted_'+str(di)+'.jpg'
            os.rename(path+'\\'+files+'\\'+file, new)
            shutil.copy(new,'C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\Disgusted')
            di+= 1
            
        if 'HA' in file:
            new= path+'\\'+files+'\\'+'Happy_'+str(ha)+'.jpg'
            os.rename(path+'\\'+files+'\\'+file, new)
            shutil.copy(new,'C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\Happy')
            ha+= 1
        
        if 'NE' in file:
            new= path+'\\'+files+'\\'+'Neutral_'+str(ne)+'.jpg'
            os.rename(path+'\\'+files+'\\'+file, new)
            shutil.copy(new,'C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\Neutral')
            ne+= 1
            
        if 'SA' in file:
            new= path+'\\'+files+'\\'+'Sad_'+str(sa)+'.jpg'
            os.rename(path+'\\'+files+'\\'+file, new)
            shutil.copy(new,'C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\Sad')
            sa+= 1
        
        if 'SU' in file:
            new= path+'\\'+files+'\\'+'Suprised_'+str(su)+'.jpg'
            os.rename(path+'\\'+files+'\\'+file, new)
            shutil.copy(new,'C:\\Users\\Sakshu\\Desktop\\EmotionClassifer\\New folder\\Suprised')
            su+= 1
#    
#    print(files)