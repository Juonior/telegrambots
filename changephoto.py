from opentele.td import TDesktop
from opentele.api import API, UseCurrentSession
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest,DeletePhotosRequest
from telethon.tl.types import InputPhoto
import asyncio,os,os.path
import urllib.request, random

# Variables
accounts_folder = r"D:\Работа\tg_bots\accounts"
charactersLimit = 30
accounts_count = len([name for name in os.listdir(accounts_folder)])
channelname = "invbotsjuonior"

# DELETE ALL PHOTOS
names = ["Ivan", "Евгений Раевский", "Дмитрий", "Sergey", "Даниил", "Виктор Селезнев", "Артем", "Петр", "Ярослав Прокофьев", "Виктория"]
biography = [
    "Founder GlobalGoods.",
    "Loigstic EastTrade.",
    "Delivery Solutions",
    "Юрист EasyExport",
    "Восточнаяпоставка.\nsalofeev@vostochnyapostavka.com",
    "Co-Founder SupplyMart.",
    "По вопросам сотрудничества -cooperation@goodlink.com",
    "TradeWave. Logistic Engineer",
    "Senior Software Engineer at ABC Company",
    "Project Manager at GHI Technologies.",
]
async def main(account_num):
    
    tdataFolder = r"D:\Работа\tg_bots\accounts\tdata"+str(account_num)
    tdesk = TDesktop(tdataFolder)
    
    assert tdesk.isLoaded()
    oldAPI = API.TelegramDesktop.Generate(system="windows", unique_id="old_tdata")



    # flag=UseCurrentSession CreateNewSession
    # Convert TDesktop to Telethon using the current session.
    client = await tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)
    await client.start()
    # urllib.request.urlretrieve("https://boredhumans.com/faces2/"+str(random.randint(1,800))+".jpg", r'D:\Работа\tg_bots\images\avatar.jpg')
    # photo = await client.upload_file("D:\\Работа\\tg_bots\\images\\"+str(account_num)+".jpg")
    # g = await client(UploadProfilePhotoRequest(file=photo))


    args = names[account_num-1].split()
    if len(args)==1:
        result = await client(UpdateProfileRequest(
            first_name=args[0],
            last_name="",
            about=biography[account_num-1]
        ))
    elif len(args)==2:
        result = await client(UpdateProfileRequest(
            first_name=args[0],
            last_name=args[1],
            about=biography[account_num-1]
        ))
    print(result)
    # Get BOT Info
    me = await client.get_me()
    # photos = await client.get_profile_photos('me')
    # for photo in photos:
    #     result = await client(DeletePhotosRequest(
    #         id=[InputPhoto(
    #             id=photo.id,
    #             access_hash=photo.access_hash,
    #             file_reference=photo.file_reference
    #         )]
    #     ))
    #     print(result)


    if type(me.last_name) == str:
        BotName  = me.first_name +" "+me.last_name
    else:
        BotName  = me.first_name
    print(BotName)

    await client.disconnect()
for i in range(1,accounts_count+1):
    asyncio.run(main(i))