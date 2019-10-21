# sentence = input("Sentence: ")
# symbol = input("Symbol: ")
# new_sentence = sentence.replace(symbol, '')
# print(new_sentence)

sentence = input("Sentence: ")
symbol = input("Symbol: ")

new_s = ''
for ch in sentence:
    if ch != symbol:
        new_s = ch
print(new_s)
