import discord
import requests
import io
import imghdr

# Replace with your actual bot token
BOT_TOKEN = 'INSERT-TOKEN-HERE'


image_path = './img.png'  
# Replace with the actual path - can be any supported type
# Specify the path to your image file
def change_bot_avatar(image_path):
    with open(image_path, 'rb') as image:
        image_data = image.read()
        image_type = imghdr.what(None, h=image_data)

    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
        "Content-Type": f"image/{image_type}" 
    }

    url = f"https://discord.com/api/v10/users/@me"  # API endpoint to modify bot user

    try:
        response = requests.patch(url, data=image_data, headers=headers)
        response.raise_for_status()  # Raise an exception for error status codes

        print('Avatar changed successfully!')

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")




 
