# Discord Rich Presence for Windows XP Pinball

## 🎨 Preview
![Preview](https://i.imgur.com/xhqgPq3.png)

## 📜 Description
This script sets up a Discord Rich Presence for the classic Windows XP Pinball.

It detects when the game is running and updates the user's Discord Rich Presence accordingly.

## ❓ How it works

1. Detects if `pinball.exe` is running. 

    (You can change the executable name in the script.)

2. Updates the Discord Rich Presence with the game's details, large image, and small image.

    (You can customize the images and text in the script.)

3. Automatically updates the Rich Presence when the game starts or stops.

## ⚙️ Setup

1. Install the required libraries:
   ```bash
   pip install pypresence psutil
   ```
2. Replace `CLIENT_ID` in the script with your actual Discord Application ID.

3. Customize the images and text in the script as needed.
4. Run the script:
   ```bash
   python script.py
   ```

Or just run the exe file in the release section.

## 🎮 Get the game

You can download the game [here](https://archive.org/download/pinball_202412/Pinball.zip).

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.