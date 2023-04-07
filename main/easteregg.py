from moviepy.editor import *
import pygame


def run():
    clip = VideoFileClip('images/RAnggyu.mp4')
    clip.preview()
    pygame.quit()
run()