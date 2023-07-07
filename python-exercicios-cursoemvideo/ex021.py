"""
    Esse exercício é referente a aula 08 do curso de Python do Curso em vídeo:

    Desafio 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

    Esse programa abre um arquivo MP3 e reproduz usando a biblioteca pygame

    By: José Brenon - 15/04/2023
"""
import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
