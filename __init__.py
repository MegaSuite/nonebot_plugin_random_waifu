from nonebot.adapters.onebot.v11 import Bot, Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot,Event
import requests

pic=on_keyword({'抽老婆'})
@pic.handle()
async def _(bot:Bot,event:Event,state:T_State):
    msg = await suijitu()
    await pic.send(Message(msg))

async def suijitu():
    url='https://moe.anosu.top/img/'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti