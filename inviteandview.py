from opentele.td import TDesktop
from opentele.api import API, UseCurrentSession
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest,GetMessagesViewsRequest
import asyncio,os,os.path,time


# Variables
folder = "D:\\Работа\\tg_bots"
charactersLimit = 30
accounts_count = len([name for name in os.listdir(folder+"\\accounts")])

async def main(account_num,channelname,message):
    
    tdataFolder = folder+"\\accounts\\tdata"+str(account_num)
    tdesk = TDesktop(tdataFolder)
    
    assert tdesk.isLoaded()
    oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old_tdata")


    # flag=UseCurrentSession CreateNewSession
    # Convert TDesktop to Telethon using the current session.
    client = await tdesk.ToTelethon(session="view.session", flag=UseCurrentSession)
    async with await client.start():


        # Get BOT Info
        me = await client.get_me()

        if type(me.last_name) == str:
            BotName  = me.first_name +" "+me.last_name
        else:
            BotName  = me.first_name

        channel= await client.get_entity(channelname)
        invite = await client(JoinChannelRequest(channel))
        result = await client(GetHistoryRequest(peer=channel,offset_id=0,offset_date=None,add_offset=0,limit=1,max_id=0,min_id=0,hash=0))
        views_before = (await client(GetMessagesViewsRequest(peer=channel,id=[message.id],increment=True,))).views[0].views
        if type(views_before) is int:
            await asyncio.sleep(0.1)
            views_after = (await client(GetMessagesViewsRequest(peer=channel,id=[message.id],increment=True,))).views[0].views
            status = "Increase views" if views_after > views_before else "Already Seen"
            print(f"[{account_num}/{accounts_count}] [{status}] {views_before} >>> {views_after} | Bot: {BotName} | Message: {message.message.message[:charactersLimit]} ")

    await client.disconnect()
# for i in range(1,accounts_count+1):
#     asyncio.run(main(i))