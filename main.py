import vk_api
import config
import time
import datetime
import requests

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

session = vk_api.VkApi(token = config.TOKEN)
vk = session.get_api()

def wetherStatus():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                            params={'id': config.city_id, 'units': 'metric', 'lang': 'en', 'APPID': config.OPENWEATHER_TOKEN})
        data = res.json()
        weatherStatus=data['weather'][0]['main']
        statusInfo=' '

        statusInfo+='{0:+3.0f} '.format(data['main']['temp'])

        weatherEmojiStatus=['⛈️','🌧️','🌦️','❄️','😶‍🌫️','😷','🌵','🌪️','🌋','☀️','🌙','☁️']
        if weatherStatus=="Thunderstorm":
            statusInfo+=weatherEmojiStatus[0]
        elif weatherStatus=="Drizzle":
            statusInfo+=weatherEmojiStatus[1]
        elif weatherStatus=="Rain":
            statusInfo+=weatherEmojiStatus[2]
        elif weatherStatus=="Snow":
            statusInfo+=weatherEmojiStatus[3]
        elif weatherStatus=="Mist":
            statusInfo+=weatherEmojiStatus[4]
        elif weatherStatus=="Smoke":
            statusInfo+=weatherEmojiStatus[5]
        elif weatherStatus=="Haze":
            statusInfo+=weatherEmojiStatus[4]
        elif weatherStatus=="Dust":
            statusInfo+=weatherEmojiStatus[6]
        elif weatherStatus=="Fog":
            statusInfo+=weatherEmojiStatus[4]
        elif weatherStatus=="Sand":
            statusInfo+=weatherEmojiStatus[6]
        elif weatherStatus=="Ash":
            statusInfo+=weatherEmojiStatus[8]
        elif weatherStatus=="Squall":
            statusInfo+=weatherEmojiStatus[7]
        elif weatherStatus=="Clear":
            statusInfo+=weatherEmojiStatus[9]
        elif weatherStatus=="Clouds":
            statusInfo+=weatherEmojiStatus[11]
        else:
            statusInfo+='🏖️'

        return statusInfo


    except Exception:
        return -2

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    try:
        json_resp = response.json()
        track_id = json_resp['item']['id']
        track_name = json_resp['item']['name']
        artists = [artist for artist in json_resp['item']['artists']]
        link = json_resp['item']['external_urls']['spotify']

        artist_names = ', '.join([artist['name'] for artist in artists])
        current_track_info = {
            "id": track_id,
            "track_name": track_name,
            "artists": artist_names,
            "link": link
        }
    except Exception:
        return -1
    return current_track_info

def spotifyStatus():
    current_track_info = get_current_track(config.SPOTIFY_TOKEN)
    if current_track_info != -1:
        #pprint(current_track_info, indent=4)
        statusInfo=f"Spotify: {current_track_info['track_name']} — {current_track_info['artists']} 🎵"
    else:
        statusInfo=-1
    return statusInfo



def timeStatus():
    dt=datetime.datetime.now()
    statusInfo=""
    # print(dt.strftime("%d.%m.%Y %H:%M (UTC +7)"))
    statusEmojiClock = ['🕛','🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚']
    statusEmojiNum = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
    
    # if dt.strftime("%I")=="12":
    #     statusInfo=statusEmojiClock[0]
    # elif dt.strftime("%I")=="01":
    #     statusInfo=statusEmojiClock[1]
    # elif dt.strftime("%I")=="02":
    #     statusInfo=statusEmojiClock[2]
    # elif dt.strftime("%I")=="03":
    #     statusInfo=statusEmojiClock[3]
    # elif dt.strftime("%I")=="04":
    #     statusInfo=statusEmojiClock[4]
    # elif dt.strftime("%I")=="05":
    #     statusInfo=statusEmojiClock[5]
    # elif dt.strftime("%I")=="06":
    #     statusInfo=statusEmojiClock[6]
    # elif dt.strftime("%I")=="07":
    #     statusInfo=statusEmojiClock[7]
    # elif dt.strftime("%I")=="08":
    #     statusInfo=statusEmojiClock[8]
    # elif dt.strftime("%I")=="09":
    #     statusInfo=statusEmojiClock[9]
    # elif dt.strftime("%I")=="10":
    #     statusInfo=statusEmojiClock[10]
    # elif dt.strftime("%I")=="11":
    #     statusInfo=statusEmojiClock[11]

    if dt.strftime("%H")[0]=="0":
        statusInfo+=statusEmojiNum[0]
    elif dt.strftime("%H")[0]=="1":
        statusInfo+=statusEmojiNum[1]
    elif dt.strftime("%H")[0]=="2":
        statusInfo+=statusEmojiNum[2]
    elif dt.strftime("%H")[0]=="3":
        statusInfo+=statusEmojiNum[3]
    elif dt.strftime("%H")[0]=="4":
        statusInfo+=statusEmojiNum[4]
    elif dt.strftime("%H")[0]=="5":
        statusInfo+=statusEmojiNum[5]
    elif dt.strftime("%H")[0]=="6":
        statusInfo+=statusEmojiNum[6]
    elif dt.strftime("%H")[0]=="7":
        statusInfo+=statusEmojiNum[7]
    elif dt.strftime("%H")[0]=="8":
        statusInfo+=statusEmojiNum[8]
    elif dt.strftime("%H")[0]=="9":
        statusInfo+=statusEmojiNum[9]

    if dt.strftime("%H")[1]=="0":
        statusInfo+=statusEmojiNum[0]
    elif dt.strftime("%H")[1]=="1":
        statusInfo+=statusEmojiNum[1]
    elif dt.strftime("%H")[1]=="2":
        statusInfo+=statusEmojiNum[2]
    elif dt.strftime("%H")[1]=="3":
        statusInfo+=statusEmojiNum[3]
    elif dt.strftime("%H")[1]=="4":
        statusInfo+=statusEmojiNum[4]
    elif dt.strftime("%H")[1]=="5":
        statusInfo+=statusEmojiNum[5]
    elif dt.strftime("%H")[1]=="6":
        statusInfo+=statusEmojiNum[6]
    elif dt.strftime("%H")[1]=="7":
        statusInfo+=statusEmojiNum[7]
    elif dt.strftime("%H")[1]=="8":
        statusInfo+=statusEmojiNum[8]
    elif dt.strftime("%H")[1]=="9":
        statusInfo+=statusEmojiNum[9]

    statusInfo+="🔹"

    if dt.strftime("%M")[0]=="0":
        statusInfo+=statusEmojiNum[0]
    elif dt.strftime("%M")[0]=="1":
        statusInfo+=statusEmojiNum[1]
    elif dt.strftime("%M")[0]=="2":
        statusInfo+=statusEmojiNum[2]
    elif dt.strftime("%M")[0]=="3":
        statusInfo+=statusEmojiNum[3]
    elif dt.strftime("%M")[0]=="4":
        statusInfo+=statusEmojiNum[4]
    elif dt.strftime("%M")[0]=="5":
        statusInfo+=statusEmojiNum[5]
    elif dt.strftime("%M")[0]=="6":
        statusInfo+=statusEmojiNum[6]
    elif dt.strftime("%M")[0]=="7":
        statusInfo+=statusEmojiNum[7]
    elif dt.strftime("%M")[0]=="8":
        statusInfo+=statusEmojiNum[8]
    elif dt.strftime("%M")[0]=="9":
        statusInfo+=statusEmojiNum[9]

    if dt.strftime("%M")[1]=="0":
        statusInfo+=statusEmojiNum[0]
    elif dt.strftime("%M")[1]=="1":
        statusInfo+=statusEmojiNum[1]
    elif dt.strftime("%M")[1]=="2":
        statusInfo+=statusEmojiNum[2]
    elif dt.strftime("%M")[1]=="3":
        statusInfo+=statusEmojiNum[3]
    elif dt.strftime("%M")[1]=="4":
        statusInfo+=statusEmojiNum[4]
    elif dt.strftime("%M")[1]=="5":
        statusInfo+=statusEmojiNum[5]
    elif dt.strftime("%M")[1]=="6":
        statusInfo+=statusEmojiNum[6]
    elif dt.strftime("%M")[1]=="7":
        statusInfo+=statusEmojiNum[7]
    elif dt.strftime("%M")[1]=="8":
        statusInfo+=statusEmojiNum[8]
    elif dt.strftime("%M")[1]=="9":
        statusInfo+=statusEmojiNum[9]

    return statusInfo

def main():
        while True:
            statusInfo = spotifyStatus()
            if statusInfo==-1:
                statusInfo=timeStatus()
                if wetherStatus()!=2:
                    statusInfo+=wetherStatus()
            statusOut = vk.status.set(text = statusInfo)
            if (statusOut!=1):
                print("Error status")
            else:
                print(f"Status: {statusInfo}")
            time.sleep(30)

while True:
    main()