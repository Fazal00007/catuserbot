"""
Memes Plugin for Userbot
usage = .meme someCharacter //default delay will be 3
By : - @Zero_cool7870

"""
from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.meme", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return   
    memeVar = event.text
    sleepValue = 5
    memeVar = memeVar[6:] 
           
    await event.edit("-------------"+memeVar)
    await event.edit("------------"+memeVar+"-")
    await event.edit("-----------"+memeVar+"--")
    await event.edit("----------"+memeVar+"---")
    await event.edit("---------"+memeVar+"----")    
    await event.edit("--------"+memeVar+"-----")
    await event.edit("-------"+memeVar+"------")
    await event.edit("------"+memeVar+"-------")
    await event.edit("-----"+memeVar+"--------")
    await event.edit("----"+memeVar+"---------")
    await event.edit("---"+memeVar+"----------")
    await event.edit("--"+memeVar+"-----------")
    await event.edit("-"+memeVar+"------------")
    await event.edit(memeVar+"-------------")
    await event.edit("-------------"+memeVar)
    await event.edit("------------"+memeVar+"-")
    await event.edit("-----------"+memeVar+"--")
    await event.edit("----------"+memeVar+"---")
    await event.edit("---------"+memeVar+"----")    
    await event.edit("--------"+memeVar+"-----")
    await event.edit("-------"+memeVar+"------")
    await event.edit("------"+memeVar+"-------")
    await event.edit("-----"+memeVar+"--------")
    await event.edit("----"+memeVar+"---------")
    await event.edit("---"+memeVar+"----------")
    await event.edit("--"+memeVar+"-----------")
    await event.edit("-"+memeVar+"------------")
    await event.edit(memeVar+"-------------")
    await event.edit(memeVar)
    await asyncio.sleep(sleepValue)

"""
Bonus : Flower Boquee Generater
usage:- .flower

"""
@borg.on(events.NewMessage(pattern=r"\.lp", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return   
    lp =" 🍭"
    sleepValue = 5
           
    await event.edit(lollipop+"        ")
    await event.edit(lollipop+lollipop+"       ")
    await event.edit(lollipop+lollipop+lollipop+"      ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+"     ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+"    ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+"   ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+"  ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+" ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop)
    await event.edit(lollipop+"        ")
    await event.edit(lollipop+lollipop+"       ")
    await event.edit(lollipop+lollipop+lollipop+"      ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+"     ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+"    ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+"   ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+"  ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+" ")
    await event.edit(lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop+lollipop)
    await asyncio.sleep(sleepValue)
    
    
@borg.on(events.NewMessage(pattern=r"\.flower", outgoing=True))
async def meme(event):
    if event.fwd_from:
        return   
    flower =" 🌹"
    sleepValue = 10
           
    await event.edit(flower+"        ")
    await event.edit(flower+flower+"       ")
    await event.edit(flower+flower+flower+"      ")
    await event.edit(flower+flower+flower+flower+"     ")
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await event.edit(flower+"        ")
    await event.edit(flower+flower+"       ")
    await event.edit(flower+flower+flower+"      ")
    await event.edit(flower+flower+flower+flower+"     ")
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)        
    
