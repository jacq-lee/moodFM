import requests

SKIP_TO_NEXT = 	f"https://api.spotify.com/v1/me/player/next"
STN_ACCESS_TOKEN = "BQAEtkuhuxEU88D0TvNKSW-isU9U_gR-V-ZJSVRKm5LpjtCBTFGgyLR9FvRdkew-szqcijpJkUNFtFH0d-APYV3hB83EAU6cM3yQopCtVhLoYpx2AQqrY_IMKiO9fv2t5CwkDtpALNyDSzkqNL-VsWVeVfiMQqHXOwn26YXfCRDtpViX2db9M31S1Ek0sVGnIgZ3DQc"

def skip_to_next():

    response = requests.post(
        SKIP_TO_NEXT,
        headers={
            "Authorization": f"Bearer {STN_ACCESS_TOKEN}"
        },
        params={"device_id": "337a5a74f4247f040ab6e594c687da4004dfbc07"}
    )

def main():
    skip_to_next()

    
if __name__ == '__main__':
    main()
