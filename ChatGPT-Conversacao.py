# DOCUMENTAÇÃO
# https://beta.openai.com/docs/introduction/overview
# https://gitpython.readthedocs.io/en/stable/intro.html
# https://pypi.org/project/openai/

# BAIXANDO OPEN-AI 
# pip install openai
# pip install openai[embeddings] --user 

# BAIXANDO SPEECHRECOGNITION - RECONHECIMENTO DE FALA
#pip install SpeechRecognition

# BIBLIOTECAS NECESSÁRIAS (CASO OCORRA ALGUM ERRO)

# pytorch
# conda install pytorch torchvision -c pytorch

# PyAudio - Microfone
# conda install -c pytorch pytorch

# whisper
# pip install whisper

# pip install pyttsx3

import openai
import speech_recognition as sr
import pyttsx3 
from datetime import datetime as date

#lista os modelos de IA
#openai.Model.list()

#Carrega a chave da API
#openai.api_key = "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"
openai.api_key = "sua chave key chatgpt"

# Lista microfones de entrada
# print(sr.Microphone().list_microphone_names())    

def retornoOpenai(entrada):
    
    resposta = openai.Completion.create(model="text-davinci-003",  #modelo de IA
                                        prompt= entrada,           #entrada para o modelo
                                        temperature=0.8,           #ajuste da resposta
                                        max_tokens=256)            #limita caracteres retorno
    return resposta

entrada = ""

while(True):       
    
    engine = pyttsx3.init() 
    engine.say(retornoOpenai("Oi, português, por favor!")["choices"][0]["text"]) 
    engine.runAndWait()
    
    # recebo a pergunta
    rec = sr.Recognizer()
    with sr.Microphone(device_index=1) as mic:
        rec.adjust_for_ambient_noise(source=mic)        
        audio = rec.listen(mic)
        texto= rec.recognize_google(audio, language="pt-BR")
        
        # executa, caso audio captado
        if texto.split() != '':
            #chama OPENAI
            temp_retorno= retornoOpenai(texto)   
            
            # valida se houve um retorno de OPENAI   
            if temp_retorno != ' ':
                
                # transformo o texto em audio
                engine = pyttsx3.init() 
                engine.say(temp_retorno["choices"][0]["text"]) 
                engine.runAndWait()
                
            else:
                # trata retorno vazio openai           
                engine = pyttsx3.init() 
                engine.say("Nenhum retorno obtido de OPEN AI")
                engine.runAndWait()
                break
                
        else:
            # trata nenhum audio captado
            engine = pyttsx3.init() 
            engine.say("Nenhum audio captado") 
            engine.runAndWait()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            