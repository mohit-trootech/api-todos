from django.utils.translation import gettext_noop as _
from enum import Enum
from dotenv import dotenv_values


# Settings Constants
# =====================================================
class Settings(Enum):
    ROOT_URL = "todos.urls"
    TEMPLATE = "templates/"
    STATIC_URL = "static/"
    STATICFILES_DIRS = "templates/static/"
    STATIC_ROOT = "assets/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    DEBUG_TOOLBAR_IP = "127.0.0.1"
    CACHE_TABLE_NAME = "cache_table"
    FIRESTORE_CERTIFICATE_PATH = ".json/certificate.json"
    STORAGE_BUCKET = "STORAGE_BUCKET"


# Status
# =====================================================
class Status(Enum):
    STATUS_INACTIVE = False
    STATUS_ACTIVE = True
    STATUS_200 = 200
    STATUS_202 = 202
    STATUS_204 = 204
    STATUS_400 = 400
    STATUS_404 = 404
    STATUS_500 = 500


# Admin Action Description
# =====================================================
class AdminAction(Enum):
    USER_ADMIN_STATUS_UNACTIVE_DESCRIPTION = _("Mark Selected Items Unactive")
    USER_ADMIN_STATUS_ACTIVE_DESCRIPTION = _("Mark Selected Items Active")
    USER_INACTIVE_SUCCESS_MESSAGE = _("%d users were successfully been inactive.")
    USER_ACTIVE_SUCCESS_MESSAGE = _("%d users were successfully been active.")


# Error Messages
# =====================================================
class Errors(Enum):
    INVALID_JSON = _("Invalid JSON data")
    LOGIN_ERROR = _("Failed to Login Try Again with Correct Credentials")
    PASSWORD_NOT_MATCH = _("Please Check Passwords are Not Matching")
    UNIQUE_USER_ERROR = _("User with Same Username or Password Already Exists")
    TERMS_NOT_ACCEPTED = _("Please Accept Terms and Conditions")


# Success Messages
# =====================================================
class Success(Enum):
    REGISTERED = _("User Added Successfully")
    USER_404 = _("User Does Not Exists")
    USER_UPDATED = _("User updated successfully")
    LOGGED_IN = _("Logged in Successfully")
    SIGNED_UP = _("User Registered Successfully")
    LOGGED_OUT = _("User Logged Out Successfully")
    FORCE_LOGGED_OUT = _("User Logged Out Successfully from all Sessions")
    PROFILE_UPDATED = _("Profile Updated Successfully")
    NEWSLETTER_SUCCESS = _("Newsletter Subscribed Successfully")


# Templates Name
# =====================================================
class Templates(Enum):
    LOGIN = "accounts/login.html"
    SIGNUP = "accounts/signup.html"
    PROFILE = "accounts/profile.html"
    HOME = "chat/index.html"
    ABOUT = "todos/about.html"
    ONLINE_USERS_LIST = "chat/online-users-list.html"
    PARTICIPANTS = "chat/chat-participant.html"
    CHAT_CONTENT = "chat/content.html"
    NEWSLETTER = "email/newsletter.html"
    CHAT_LIST = "chat/chat-list.html"


# Urls Path & Reverse
# =====================================================
class Urls(Enum):
    HOME = "/chat/"
    ABOUT = "/chat/about/"
    LOGIN = "/accounts/login"
    REGISTER = "accounts/signup"
    LOGOUT = "accounts/logout"
    PROFILE = "accounts/profile"
    HOME_REVERSE = "home"
    ABOUT_REVERSE = "about"
    LOGIN_REVERSE = "login"
    REGISTER_REVERSE = "signup"
    LOGOUT_REVERSE = "logout"
    FORCE_LOGOUT_REVERSE = "force-logout"
    PROFILE_REVERSE = "profile"
    USER_PROFILE_REVERSE = "user-profile"
    INDEX_REVERSE = "index"
    CHAT_DATA = "chat-data"
    PROFILE_UPDATE_SUCCESS_URL = "/accounts/profile/{pk}"
    NEWLETTER_REVERSE = "newsletter"


# Context Variable Names
# =====================================================
class ContextNames(Enum):
    MESSAGES = "chats"


# Forms Constants Dictionary
# =====================================================
FORM_LABELS = {
    "profile": "Please Update Profile Picture",
    "age": "Enter Age",
    "phone": "Enter Phone Number",
    "address": "Enter Address",
    "first_name": "Enter First Name",
    "last_name": "Enter Last Name",
    "username": "Enter Username",
    "email": "Enter Email",
    "password": "Enter Password",
}


# Model Media Urls
# =====================================================
class ModelMediaUrl(Enum):
    USER = "profile/{id}/{file}"


# Email Configurations
# =====================================================
class EmailConfig(Enum):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_465 = 465
    PORT_587 = 587


# Request KEY
# =====================================================
class RequestKey(Enum):
    ONLINE_USERS = "onlineUsers"
    REQUEST_TYPE = "requestType"
    NEW_CHAT = "startNewChat"
    USER_ID = "userId"
    CHAT_MESSAGE = "newChatMessage"
    USER_TEXT = "userText"
    CHAT_ID = "chatId"
    UPDATE_STATUS = "updateStatus"
    UPDATE_FRIENDS_LIST = "updateFriendsList"
    USER = "user"
    LOAD_CHATS = "loadChats"


# Response KEY
# =====================================================
class ResponseKey(Enum):
    PARTICIPANT_HTML = "participant_html"
    CHAT_HTML = "chat_html"
    FIRESTORE_CHAT_COLLECTION = """
chatsCollectionUrl = `chats/{id}/messages;`
"""


# Email Secret
# =====================================================
class EmailConstants(Enum):
    config = dotenv_values(".env")
    NEWSLETTER = _("QuickReads Newsletter Subscribed")
    HOST = config.get("EMAIL_HOST_USER")


# Other Constants
# =====================================================
EMPTY_STR = ""
UTF_8 = "utf-8"
FORM_CLASS = "input input-bordered w-full"
FORM_CLASS_FILE = "file-input file-input-bordered w-full"
TEXT_AREA = "textarea textarea-bordered textarea-lg w-full"
SELECT_CLASS = "select select-bordered w-full select-sm"
THEME_CHOICES = (
    ("light", "light"),
    ("dark", "dark"),
    ("cupcake", "cupcake"),
    ("bumblebee", "bumblebee"),
    ("emerald", "emerald"),
    ("corporate", "corporate"),
    ("synthwave", "synthwave"),
    ("retro", "retro"),
    ("cyberpunk", "cyberpunk"),
    ("valentine", "valentine"),
    ("halloween", "halloween"),
    ("garden", "garden"),
    ("forest", "forest"),
    ("aqua", "aqua"),
    ("lofi", "lofi"),
    ("pastel", "pastel"),
    ("fantasy", "fantasy"),
    ("wireframe", "wireframe"),
    ("black", "black"),
    ("luxury", "luxury"),
    ("dracula", "dracula"),
    ("cmyk", "cmyk"),
    ("autumn", "autumn"),
    ("business", "business"),
    ("acid", "acid"),
    ("lemonade", "lemonade"),
    ("night", "night"),
    ("coffee", "coffee"),
    ("winter", "winter"),
    ("dim", "dim"),
    ("nord", "nord"),
    ("sunset", "sunset"),
)

TYPE_HTML = "text/html"
SECONDS_IN_ONE_DAY = 86400
INACTIVE_STATUS = 0
ACTIVE_STATUS = 1

STATUS_CHOICES = (
    (INACTIVE_STATUS, _("Inactive")),
    (ACTIVE_STATUS, _("Active")),
)
THUMBNAIL_PREVIEW_TAG = '<img src="{img}" width="320"/>'
THUMBNAIL_PREVIEW_HTML = """<div class="warning" style="color:#000;width: 320px;
        padding: 12px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: start;
        background: #FEF7D1;
        border: 1px solid #F7C752;
        border-radius: 5px;
        box-shadow: 0px 0px 5px -3px #111;">
        <div class="warning__icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" viewBox="0 0 24 24" height="24" fill="none">
                <path fill="#393a37" d="m13 14h-2v-5h2zm0 4h-2v-2h2zm-12 3h22l-11-19z" style="
        fill: #F7C752;"></path>
            </svg>
        </div>
        <strong>No Profile Picture Available</strong>
    </div>"""
