import os
import openai

openai.api_key ='secret_key'

def whole_program():

  prompt=input("whats you question..?\n")

  response = openai.Completion.create(
    model="text-davinci-002",          #you can change your model here...
    prompt=prompt,
    temperature=0.4,
    max_tokens=32,  # increase the tokens you will get more breif answers
  )
  output=response['choices']
  outputNeeded=output[0]

  print(outputNeeded['text'])

while True:
  whole_program()
  if input("have more questions..?\n") == "No":
    break



