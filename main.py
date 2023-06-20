import random
import string
from grafo import Grafo, Vertice
import re
import os


def get_palavra_from_texto(text_path):
    with open (text_path, 'r') as f:
        text = f.read()

        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))


    palavras = text.split()
    return palavras


def make_grafo (palavras):
    g = Grafo()

    previous_palavra = None

    for palavra in palavras:
        palavra_vertice = g.get_vertice(palavra)

        if previous_palavra:
            previous_palavra.incrementar_borda(palavra_vertice)

        previous_palavra = palavra_vertice

    g.generate_probabilidade()

    return g

def compor (g , palavras , length = 50):
    compor = []
    palavra = g.get_vertice(random.choice(palavras))
    for _ in range (length):
        compor.append(palavra.valor)
        palavra = g.get_next_palavra(palavra)

    return compor

def main (artista):
    #palavras  =get_palavra_from_texto('texts/hp_sorcerer_stone.txt')
    palavras = []
    for song_file in os.listdir(f'songs/{artista}'):
        if song_file == '.DS_Store':
            continue
        song_palavras = get_palavra_from_texto(f'songs/{artista}/{song_file}')
        palavras.extend(song_palavras)


    g = make_grafo(palavras)
    coposicao = compor(g , palavras, 100)
    return ' '.join(coposicao)

if __name__ == '__main__':
    print(main('queen'))




