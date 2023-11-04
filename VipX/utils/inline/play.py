import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, GROUP_USERNAME, CHANNEL_USERNAME
from VipX import app

import config
from VipX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    vip = math.floor(percentage)
    if 0 < vip <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < vip < 4:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= vip < 6:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 6 <= vip < 8:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 8 <= vip < 10:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـ♡ﮩﮩ٨ـ"
    elif 10 <= vip < 12:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 12 <= vip < 14:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 14 <= vip < 16:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= vip < 18:
        bar = "ﮩ٨♡ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 18 <  vip < 20:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= vip < 22:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 22 <= vip < 24:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= vip < 26:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 26 <= vip < 28:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 28 <= vip < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨♡ـﮩﮩ٨ـ"
    elif 30 <= vip < 32:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 32 <= vip < 34:
        bar = "ﮩ٨ـﮩﮩ٨♡ـﮩ٨ـﮩﮩ٨ـ"
    elif 34 <= vip < 36:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= vip < 38:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 38 <= vip < 40:
        bar = "ﮩ٨ـ♡ﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= vip < 42:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 42 <= vip < 44:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 44 <= vip < 46:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 46 <= vip < 48:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 48 <= vip < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= vip < 52:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 52 <= vip < 54:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 54 <= vip < 56:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= vip < 58:
        bar = "ﮩ٨♡ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 58 <= vip < 60:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= vip < 62:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 62 <= vip < 64:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= vip < 66:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 66 <= vip < 68:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 68 <= vip < 70:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨♡ـﮩﮩ٨ـ"
    elif 70 <= vip < 72:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= vip < 74:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 74 <= vip < 76:
        bar = "ﮩ٨♡ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 <= vip < 78:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 78 <= vip < 80:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 80 <  vip < 82:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 82 <= vip < 84:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨♡ـ"
    elif 84 <= vip < 86:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 86 <= vip < 88:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 88 <= vip < 90:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨♡ـﮩﮩ٨ـ"
    elif 90 <= vip < 92:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 92 <= vip < 94:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 94 <= vip < 96:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= vip < 98:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 98 <= vip < 100:
        bar = "ﮩ٨ـ♡ﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    vip = math.floor(percentage)
    if 0 < vip <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < vip < 4:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= vip < 6:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 6 <= vip < 8:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 8 <= vip < 10:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـ♡ﮩﮩ٨ـ"
    elif 10 <= vip < 12:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 12 <= vip < 14:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 14 <= vip < 16:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= vip < 18:
        bar = "ﮩ٨♡ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 18 <  vip < 20:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= vip < 22:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 22 <= vip < 24:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= vip < 26:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 26 <= vip < 28:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 28 <= vip < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨♡ـﮩﮩ٨ـ"
    elif 30 <= vip < 32:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 32 <= vip < 34:
        bar = "ﮩ٨ـﮩﮩ٨♡ـﮩ٨ـﮩﮩ٨ـ"
    elif 34 <= vip < 36:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= vip < 38:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 38 <= vip < 40:
        bar = "ﮩ٨ـ♡ﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= vip < 42:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 42 <= vip < 44:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 44 <= vip < 46:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 46 <= vip < 48:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 48 <= vip < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= vip < 52:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 52 <= vip < 54:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 54 <= vip < 56:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= vip < 58:
        bar = "ﮩ٨♡ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 58 <= vip < 60:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= vip < 62:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 62 <= vip < 64:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= vip < 66:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 66 <= vip < 68:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 68 <= vip < 70:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨♡ـﮩﮩ٨ـ"
    elif 70 <= vip < 72:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= vip < 74:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 74 <= vip < 76:
        bar = "ﮩ٨♡ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 <= vip < 78:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 78 <= vip < 80:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"
    elif 80 <  vip < 82:
        bar = "♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 82 <= vip < 84:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨♡ـ"
    elif 84 <= vip < 86:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ♡٨ـ"
    elif 86 <= vip < 88:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 88 <= vip < 90:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨♡ـﮩﮩ٨ـ"
    elif 90 <= vip < 92:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ♡٨ـﮩﮩ٨ـ"
    elif 92 <= vip < 94:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 94 <= vip < 96:
        bar = "ﮩ٨ـﮩﮩ♡٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= vip < 98:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 98 <= vip < 100:
        bar = "ﮩ٨ـ♡ﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons