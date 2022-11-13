import os
import openai

openai.api_key ='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'

def whole_program():

  prompt=input("whats you question..?\n")

  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.4,
    max_tokens=32,
  )
  output=response['choices']
  outputNeeded=output[0]

  print(outputNeeded['text'])

while True:
  whole_program()
  if input("have more questions..?\n") == "No":
    break



