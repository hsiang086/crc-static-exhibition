from moviepy.editor import *
import pygame

clip = VideoFileClip('images/RAnggyu.mp4')
newclip = clip.volumex(0.1)
newclip.preview()
 
pygame.quit()