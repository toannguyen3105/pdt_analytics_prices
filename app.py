import os
import csv
from dotenv import load_dotenv

from analytics.etopfun import get_items_etopfun
from analytics.loot import update_items_loot
from analytics.recommend import recommend_all_price
from analytics.swap import update_items_swap
from analytics.tradeit import update_items_trade_it
from loggingUtil import logger

load_dotenv()

# Access environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_items_in_bag(a):
    get_items_etopfun(a)


def update_items_in_bag(a):
    update_items_trade_it(a)
    update_items_swap(a)
    update_items_loot(a)


def recommend_price():
    recommend_all_price()


ACTIVE_USER = 1
logger.warning('===== START APP =====')

accounts = [
    {
        "id": 1,
        "etopfun_cookie": "_ga=GA1.1.511772697.1696864201; locale=en; DJSP_UUID=18b14fcec853fde4e50eb5e3; SCRIPT_VERSION=29.31.06; Hm_lvt_1cb9c842508c929123cd97ecd5278a28=1697284553,1697373177,1697470874,1697555234; JSESSIONID=D2FEF6211E5D22FD08BC63BD5223596A; DJSP_USER=fELYbixIZp9V2JhJwh3kWSsptjlkwq7e9%2BsWHUlNnjSXnXTKib4Rei9lBAmUrcf1fk3KxpxRrU8o26aFfI1t8HcWSC6M2OuIK0yQ9WvfmB8%3D; _ga_TDF3LV246N=GS1.1.1697555233.10.1.1697558796.0.0.0; Hm_lpvt_1cb9c842508c929123cd97ecd5278a28=1697558797",
        "tradeit_cookie": "i18n_redirected=en; sessionid=s%3A5DfJ7lwyHb0MYCKsN3oHoePM8jUNUDSf.K7zTCm2vZAjVIawKBHnkpEMy%2F0XdbJo00MGmXPae0pk; vuex={%22inventory%22:{%22siteInventory%22:{%22filters%22:{%22gameId%22:730}}%2C%22userInventory%22:{%22filters%22:{}}}%2C%22users%22:{%22analyticsAttributes%22:null}}; _scid=f81ecde9-5fe5-48bd-9bc0-c385c8cef05e; _rdt_uuid=1696864378078.0a117833-2935-4bfa-8766-12a9884a7a66; _ga=GA1.1.732810977.1696864378; _tt_enable_cookie=1; _ttp=nHVC9TvT31m4O7dv1opqERbV8Uh; _fbp=fb.1.1696864379586.145798163; _ym_uid=1696864381635544595; _ym_d=1696864381; socketuuid=d678b20e-ca7e-4a55-bdfb-b4a5a5c4a789; __stripe_mid=bb7c0385-5eba-4fd3-bd10-6c8a6148303496cda7; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22emthichuongbohuc3%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%2276561199008080537%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22f76562a5-b425-4463-a421-71463afaa6ce%22%2C%22deviceAdded%22%3Atrue%7D; tmr_lvid=85c8b9c690c3ff5b8c8558e8b16154f3; tmr_lvidTS=1697037871050; SETUP_TIME=1697037874603; _sctr=1%7C1697389200000; OPT_IN_SHOWN_TIME=1697471003373; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22dismissed%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _ym_isad=2; moe_uuid=f76562a5-b425-4463-a421-71463afaa6ce; __stripe_sid=fa770966-aabc-4e7b-9f7d-ffb7423e98de3800e9; tmr_detect=0%7C1697556397797; _uetsid=72df1bd06c3a11eea51e5b90ebed426b; _uetvid=545b61b066b611eeab716faf685f623c; _ga_RFHNPQTN51=GS1.1.1697555337.9.1.1697557095.60.0.0; _scid_r=f81ecde9-5fe5-48bd-9bc0-c385c8cef05e",
        "status": 1
    },
    {
        "id": 2,
        "etopfun_cookie": "_ga=GA1.1.161229482.1696864621; locale=en; DJSP_UUID=18b150352b63fd72685740f0; SCRIPT_VERSION=29.31.06; DJSP_USER=fELYbixIZp8L0ejGnrHKxh%2FrtkQiV0L3CyNIWKie%2BNyJH88i8ss2dMJUNStqWWIGXlUmc6qJzAa4MgSNqHG1xHcWSC6M2OuIK0yQ9WvfmB8%3D; Hm_lvt_1cb9c842508c929123cd97ecd5278a28=1697366651,1697372439,1697471071,1697641456; Hm_lpvt_1cb9c842508c929123cd97ecd5278a28=1697641456; JSESSIONID=31E0B42D553CB46B3D9B26B9E7F75AA6; _ga_TDF3LV246N=GS1.1.1697641455.7.0.1697641464.0.0.0",
        "tradeit_cookie": "i18n_redirected=en; sessionid=s%3Au5vqJCU0S20khkxNhlVnbM-sLvBAbhHw.bgJ8bXJ4nqelEnhZzVA4V9jMZpj5cp7PKQQmOsFL5xk; vuex={%22inventory%22:{%22siteInventory%22:{%22filters%22:{%22gameId%22:730}}%2C%22userInventory%22:{%22filters%22:{}}}%2C%22users%22:{%22analyticsAttributes%22:null}}; _scid=b42c81ad-92af-4127-8e4d-ab054ff4a2a5; _rdt_uuid=1696864640106.6239eaf5-ef7b-433a-82af-fecdd11e4aa5; _fbp=fb.1.1696864640259.750163842; _ga=GA1.1.1001498749.1696864640; _tt_enable_cookie=1; _ttp=cBO-oCdx_OmflHQybN6R74oTsqD; socketuuid=e861b121-fa6e-496d-a552-0739cc568030; _ym_uid=1696865315509383007; _ym_d=1696865315; USER_DATA=%7B%22attributes%22%3A%5B%7B%22key%22%3A%22USER_ATTRIBUTE_USER_EMAIL%22%2C%22value%22%3A%22emthichuongbohuc2%40gmail.com%22%7D%2C%7B%22key%22%3A%22USER_ATTRIBUTE_UNIQUE_ID%22%2C%22value%22%3A%2276561199007886826%22%7D%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%22b8a85f83-c801-4e53-a61d-bf7f6865e4b2%22%2C%22deviceAdded%22%3Atrue%7D; tmr_lvid=9e82cb45465407bd62f9dabcb90e974d; tmr_lvidTS=1697366654888; __stripe_mid=9da05cd3-97c6-4dfa-b621-ee44fe4623283a6e59; OPT_IN_SHOWN_TIME=1697366854200; SOFT_ASK_STATUS=%7B%22actualValue%22%3A%22shown%22%2C%22MOE_DATA_TYPE%22%3A%22string%22%7D; _sctr=1%7C1697562000000; _ym_isad=2; moe_uuid=b8a85f83-c801-4e53-a61d-bf7f6865e4b2; tmr_detect=0%7C1697641463814; __stripe_sid=c9bf26a1-f20d-469a-a51e-68da246b44de15c9ec; _scid_r=b42c81ad-92af-4127-8e4d-ab054ff4a2a5; _uetsid=9cbbc9a06dc711ee9935f3992ebd4341; _uetvid=edd17c1066b611ee8795dfaa17116556; _ga_RFHNPQTN51=GS1.1.1697641459.3.1.1697641510.9.0.0",
        "status": 1
    }
]
for account in accounts:
    logger.warning('Cookie etopfun: {}'.format(account['etopfun_cookie']))

    if account['status'] == ACTIVE_USER:
        # Lay thong tin item trong bag cua etopfun
        get_items_in_bag(account)

        # Cap nhat gia cua tradeit, swap, lootfarm
        update_items_in_bag(account)

        # Cap nhat goi y
        recommend_price()

logger.warning('===== END APP =====')
