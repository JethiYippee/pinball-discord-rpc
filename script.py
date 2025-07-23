import time
import psutil
from pypresence import Presence

GAME_NAME = "pinball.exe"

CLIENT_ID = "0000000000000000000"  # Replace with your actual Discord Application ID
RPC = Presence(CLIENT_ID)
RPC.connect()

# Customize
DETAILS = "Windows XP Pinball"
LARGE_IMAGE = "https://i.imgur.com/yRi1xna.png"
LARGE_TEXT = "3D Space Cadet Pinball"
SMALL_IMAGE = "https://i.imgur.com/e6M2tNb.png"
SMALL_TEXT = "Pinball"

def is_game_running(exe_name=GAME_NAME):
    """Check if the game is running"""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and exe_name.lower() in proc.info['name'].lower():
            return True
    return False

active = False
print("🎯 Waiting for pinball.exe to launch...")

while True:
    if is_game_running():
        if not active:
            print("✅ Game started! Setting Rich Presence.")
            RPC.update(
                details=DETAILS,
                large_image=LARGE_IMAGE,
                large_text=LARGE_TEXT,
                small_image=SMALL_IMAGE,
                small_text=SMALL_TEXT
            )
            active = True
    else:
        if active:
            print("❌ Game closed! Clearing Rich Presence.")
            RPC.clear()
            active = False
    time.sleep(5)
