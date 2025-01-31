# TikTok-video-download-import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

TOKEN = os.getenv("'7844562505:AAEdUo3axyJbLefUEw_sI_OvTJp5G0RZ1q4'")  # Railway থেকে টোকেন নেবে
API_URL = "https://www.tikwm.com/api/"  # TikTok ভিডিও ডাউনলোডার API

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Send me a TikTok video link, and I'll download it for you!")

def download_tiktok(update: Update, context: CallbackContext):
    url = update.message.text
    if "tiktok.com" in url:
        update.message.reply_text("Downloading video...")

        # TikTok API দিয়ে ভিডিও ডাউনলোড করা
        try:
            response = requests.get(API_URL, params={"url": url})
            data = response.json()

            if data.get("status") == 200:  # নিশ্চিত হওয়া যে রেসপন্স সফল
                video_url = data["data"]["play"]
                update.message.reply_text(f"Here is your video: {video_url}")
            else:
                update.message.reply_text("Failed to download the video. Try another link.")
        except Exception as e:
            update.message.reply_text(f"An error occurred: {str(e)}")
    else:
        update.message.reply_text("Please send a valid TikTok link.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_tiktok))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
