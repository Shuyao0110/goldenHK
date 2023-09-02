#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:27:46 2022

@author: heshuyao
"""

import sys
import pygame
from pygame.constants import *
import time

def main():
    #创建一个窗口
    screen=pygame.display.set_mode((486,648),0,32)
    #创建一个图片，当做背景
    background=pygame.image.load('飞机大战背景图.webp')
    player=pygame.image.load('plane3.png')
    #创建一个图片当做背景
    background=pygame.image.load('./飞机大战背景图.webp')
    
    #飞机速度
    speed=10
    x=190
    y=533
    while True:
        #将背景图片粘贴到窗口
        screen.blit(background,(0,0))
        screen.blit(player, (x,y))
        #获取事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
             # elif event.type==pygame.KEYDOWN:
                  #if event.key==K_a or event.key==K_LEFT:
                    #  print('左')
                  #elif event.key==K_d or event.key==K_RIGHT:
                  #    print('右')
                 # elif event.key==K_SPACE:
                      #print('空格')
       
        
        #监听键盘事件
        key_pressed=pygame.key.get_pressed()
        
        if key_pressed[K_w] or key_pressed[K_UP]:
            print('上')
            y-=speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print('下')
            y+=speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print('左')
            x-=speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print('右')
            x+=speed
        if key_pressed[K_SPACE]:
            print('空格')
            
        #显示窗口中的内容
        pygame.display.update()
        time.sleep(0.01)

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    