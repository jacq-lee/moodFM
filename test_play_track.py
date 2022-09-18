import requests
user_id = "hpmu6h0ms4l2w600tc3v26oqd"

from requests_toolbelt.utils import dump

def logging_hook(response, *args, **kwargs):
    data = dump.dump_all(response)
    print(data.decode('utf-8'))

http = requests.Session()
http.hooks["response"] = [logging_hook]

GET_AVALIABLE_DEVICES_URL = "https://api.spotify.com/v1/me/player/devices"
GAD_ACCESS_TOKEN = "BQDeh79qgXvmxWwUWUUJm-mesF0jxzU35hJIXVkYXKadL6uOk7FKOwbe2COp5gxddDZ9hBbQtu98eJXaGUMla9UczOa7WoGR5H42a6bVlRKcQLokGIl7sdsIYhBGS0UdrfTAMqkOrK1ozyRZvXW4iecxmHsSp4PKZnnhuQPtkmAVFFLdn4vB_5mirBhKxSZrzCokX2xTI2Y"

def get_avaliable_devices():
    response = requests.get(
        GET_AVALIABLE_DEVICES_URL,
        headers={
            "Authorization": f"Bearer {GAD_ACCESS_TOKEN}"
        }
    )
    json_response = response.json()
    device_id = json_response["devices"][0]["id"]
    return device_id

SKIP_TO_NEXT = 	"https://api.spotify.com/v1/me/player/next"
STN_ACCESS_TOKEN = "BQATmVWVyvUrSPa9g_GyJYgDUypkwjS7Z2AWTdXXxLWdXugk6u2bIPyt20sWQNFoHJ74xkOHIp7WAWdpc7SI3LLsuLzgL9NOiPCfxWK8vnBdNMEf9igp8YP9jJUTbryMlZXW7VVlm3mFeg9blluibDxUJFpH4jRvDL_Ctd-mfVUlVAFZHDsffgytaRPEkycnM8s28xU"

def skip_to_next():
    params={"device_id": "337a5a74f4247f040ab6e594c687da4004dfbc07" }

    response = requests.post(
        GET_AVALIABLE_DEVICES_URL,
        headers={
            "Authorization": f"Bearer {STN_ACCESS_TOKEN}"
        },
        params=params

    )
    print(response.request)
    json_resp = response.json()
    return json_resp

def main():
    #device_id = get_avaliable_devices()
    skip_to_next()

    
if __name__ == '__main__':
    main()
