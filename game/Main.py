#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Jogo criado com python3, chamado  de  Battle of the Kingdoms."""

from pygame import *
from sys import exit
from random import randint

cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_verde = (0, 100, 0)

def arvore(janela, x, y):
    arvore_imagem = image.load("img/arvore.png")
    janela.blit(arvore_imagem, (x, y))

def arqueiro(janela, x, y):
    arqueiro_imagem = image.load("img/arqueiro.png")
    janela.blit(arqueiro_imagem, (x, y))

def tela():
    init()

    tamanho = largura, altura = 800, 600

    janela = display.set_mode(tamanho)
    display.set_caption("Battle of the Kingdoms")

    tempo = time.Clock()

    quantidade = randint(10, 100)
    x = [randint(0, 600) for numero in range(quantidade)]
    y = [randint(0, 800) for numero in range(quantidade)]

    x_arqueiro = 100
    y_arqueiro = 100

    while True:
        for evento in event.get():
            if evento.type == QUIT:
                exit()
            if evento.type == KEYDOWN and evento.key == K_w:
                y_arqueiro -= 2
            if evento.type == KEYDOWN and evento.key == K_s:
                y_arqueiro += 2
            if evento.type == KEYDOWN and evento.key == K_a:
                x_arqueiro -= 2
            if evento.type == KEYDOWN and evento.key == K_d:
                x_arqueiro += 2
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            y_arqueiro -= 2
        if keys_pressed[K_s]:
            y_arqueiro += 2
        if keys_pressed[K_a]:
            x_arqueiro -= 2
        if keys_pressed[K_d]:
            x_arqueiro += 2

        janela.fill(cor_verde)

        for cont in range(quantidade):
            arvore(janela, x[cont], y[cont])

        arqueiro(janela, x_arqueiro, y_arqueiro)

        tempo.tick(60)

        display.flip()




if __name__ == '__main__':
    tela()