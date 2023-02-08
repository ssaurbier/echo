import os
import openai

from credentials import apikey

openai.api_key = f'{apikey}'

'''
openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens, however you requested 
4268 tokens (3559 in your prompt; 709 for the completion). Please reduce your prompt; or completion length.
'''

# make text
def make_article(body):
    with open(body,'r') as file:
        articlebody = file.read()

    if len([*articlebody]) > 3559:
        articlebody = ''.join([*articlebody][:3558])

    return articlebody 

article = make_article('text.txt')

# make query
query = '"What are the political biases in the following article?'

# make call
response = openai.Completion.create(
engine="text-davinci-002",
prompt=f"{query} {article}",
temperature=0.7,
max_tokens=709,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)

# get response
print(response.choices[0].text)