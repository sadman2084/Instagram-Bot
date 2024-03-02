from instabot import Bot

bot = Bot()  # calling the bot by creating variable named "bot"
try:
    un = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    bot.login(username=un, password=password)

    # Enter the Instagram id that you want to follow
    fl = input("Enter the Instagram id you want to follow: ")
    bot.follow(fl)

    # Enter the Path of the photo that you want to upload
    photo_path = input("Enter the file path of the photo you want to upload: ")
    caption = input("Enter your caption for the photo: ")
    bot.upload_photo(photo_path, caption=caption)

    # Enter the Instagram id that you want to unfollow
    fl = input("Enter the Instagram id you want to unfollow: ")
    bot.unfollow(fl)

    # To send messages to someone
    recipients = input(
        "Enter the usernames of users you want to send messages to (comma-separated): "
    ).split(",")
    message = input("Enter the text you want to send: ")
    bot.send_message(message, recipients)

    # Getting info of followers
    followers = bot.get_user_followers("user1_name")
    for follower in followers:
        print(bot.get_user_info(follower))

    # Getting info of following
    following = bot.get_user_following("user1_name")
    for Following in following:
        print(bot.get_user_info(Following))

except Exception as e:
    print("An error occurred:", e)
