a = 0
text = "toto je text ktery s vypisuje"

for b in range(len(text)):
    if b == 3:
        raise Exception("error")
    print(text[b])
