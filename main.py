from opentele.td import TDesktop
from opentele.api import API, UseCurrentSession
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest,GetMessagesViewsRequest
import asyncio,os,os.path,time
from telethon import events
from inviteandview import main as view
# Variables
folder = "D:\\Работа\\tg_bots"
charactersLimit = 30
accounts_count = len([name for name in os.listdir(folder+"\\accounts")])
channelname = "invbotsjuonior"

async def main(account_num):
    
    tdataFolder = folder+"\\accounts\\tdata"+str(account_num)
    tdesk = TDesktop(tdataFolder)
    
    assert tdesk.isLoaded()
    oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old_tdata")


    # flag=UseCurrentSession CreateNewSession
    # Convert TDesktop to Telethon using the current session.
    
    client = await tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)
    @client.on(events.NewMessage)
    async def my_event_handler(message):
        if message.post == True:
            me = await client.get_me()
            if type(me.last_name) == str:
                BotName  = me.first_name +" "+me.last_name
            else:
                BotName  = me.first_name
            views_before = (await client(GetMessagesViewsRequest(peer=message.peer_id,id=[message.id],increment=True,))).views[0].views
            if type(views_before) is int:
                await asyncio.sleep(0.2)
                views_after = (await client(GetMessagesViewsRequest(peer=message.peer_id,id=[message.id],increment=True,))).views[0].views
            status = "Increase views" if views_after > views_before else "Already Seen"
            print(f"[1/{accounts_count}] [{status}] {views_before} >>> {views_after} | Bot: {BotName} | Message: {message.message.message[:charactersLimit]} ")
            for i in range(50,accounts_count+1):
                await view(i,channelname,message)

    await client.connect()
    await client.run_until_disconnected()
asyncio.run(main(1))
