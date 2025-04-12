import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 20978010
API_HASH = "2d29a7675f8d2e0d4b63fe9af52c239b"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7832977288:AAH151T-EdUd2RNp9UNpXyiF5DDr_pxNfZg"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Arjunpal07:Arjunpal07@cluster0.pdvsztf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002501859678

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 8037473436

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/alka_musicbot"
SUPPORT_GROUP = "https://t.me/alka_musicbot"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQAf70YAdgT4H41JgcQEAB3Wx5O93ChGsStIwDs1aas082j97JBtuCfIvoRuEbqcyPQuoYuUCBF97jIk6NX1PUUdYSIZX3H40Oth8DqaZ06VADv_ny5Vbmp0jquPbk1msZOnNWfXRRrSSVhjER8mgZckpYr4hLT1VL8saLVl4-UBWstG_sTDZwPSFrdoRFWNhuw278GVa24qicaIYMI4rygkU3USLtypH-S-r0AHN_wUgrUpjyY4tCv2Sygd40-DUnJONJN6Ka9IL-GPFPW2tVxb_hFis6s73A9BvNGgqn1KC4HoHQTnSq51gn-WeAoJ4vWNygGDvtJTozY0wYE5DJpXkctkZwAAAAHfEhycAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"

PING_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"
STATS_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/3640163c01c2431585152-d3f91bb7cbaae10afd.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
