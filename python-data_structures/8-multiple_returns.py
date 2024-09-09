#!/usr/bin/python3
def multiple_returns(sentence):
    # Si la chaîne est vide, renvoyer None
    if len(sentence) == 0:
        return (0, None)

    # Sinon, renvoyer la longueur et le premier caractère de la phrase
    return (len(sentence), sentence[0])
