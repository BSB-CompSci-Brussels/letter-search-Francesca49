# Write code that counts the number of anyLetter in anyText
def countLetters(anyText:str,anyLetter:str)->int:
  counter = 0
  anyText = input("what is your text?")
  anyLetter = input("what letter are you looking for?")
  if anyLetter in anyText: 
    print("yes, it is in the word. ")
  else:
    print("no, it is not in the word. ")
  return counter
