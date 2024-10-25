import telebot
import instaloader
from instaloader import Post

# Bot token
TOKEN = '7122697425:AAF8FF98LNg-QoLICco6D7xQ4Kp2weJ4NDY'
bot = telebot.TeleBot(TOKEN)

# Initialize Instaloader with session ID
L = instaloader.Instaloader()
L.context._session.cookies.update({'sessionid': 'YOUR_INSTAGRAM_SESSION_ID'})

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to Instagram Downloader Bot! Send an Instagram post link, and I'll download it for you.")

@bot.message_handler(func=lambda message: True)
def download_instagram_content(message):
    url = message.text.strip()
    
    # Check if the message is a valid Instagram link
    if 'instagram.com' in url:
        bot.send_message(message.chat.id, "Processing your link 🔗...")
        
        try:
            # Extract shortcode from the URL
            shortcode = url.split("/")[-2]
            post = Post.from_shortcode(L.context, shortcode)
            
            # Download the post content based on its type
            if post.is_video:
                bot.send_video(message.chat.id, post.video_url, caption=post.caption)
            else:
                bot.send_photo(message.chat.id, post.url, caption=post.caption)
        
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {str(e)}")
    else:
        bot.send_message(message.chat.id, "Please send a valid Instagram post link.")

# Start polling
bot.polling()
