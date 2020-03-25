# URL endpoints and paths taken from uHoo Android app

# URL Endpoints
API_URL_SCAFFOLD: str = "https://api.uhooinc.com/v1"
AUTH_URL_SCAFFOLD: str = "https://auth.uhooinc.com"

# API Paths
DEVICE_PAIR: str = "pairdevice"
USER_REFRESH_TOKEN: str = "renewusertoken"
USER_CONFIG: str = "user"
USER_VERIFY_EMAIL: str = "verifyemail"
USER_LOGIN: str = "login"
APP_MUST_UPDATE: str = "getandroidversionconsumer"
APP_MUST_UPDATE_BIZ: str = "getandroidversion"
USER_LOGOUT: str = "clearusersession"
USER_REGISTER: str = "registeruser"
USER_EDIT_DATA: str = "edituserdata"
USER_DATA: str = "getuserdata"
USER_AVATAR: str = "useravatar"
USER_SET_AVATAR: str = "useravatar"
USER_FORGOT_PASSWORD: str = "forgetpw"
USER_RESET_PASSWORD: str = "resetpw"
USER_CHANGE_PASSWORD: str = "changepw"
USER_LANGUAGES: str = "languagelist"
USER_VERIFY: str = "getuserinformation"
USER_SETTINGS: str = "wtvsRh/usersettings"
USER_SET_SETTINGS: str = "usersettings"
DEVICE_ALL: str = "getdevice"
DEVICE_DATA: str = "wtvsRh/getdevicedata"
DEVICE_GET_DETAILS: str = "getdevicedetails"
DEVICE_SAVE_DETAILS: str = "savedeviceconsumer"
DEVICE_SAVE_CORPORATE: str = "test/savecorporatedevice"
DEVICE_EDIT_DETAILS: str = "test/editdevicedetails"
DEVICE_CHECK_MAC: str = "checkproddevice"
DEVICE_IS_REGISTERED: str = "device/whoami"
DEVICE_REGIONS: str = "deviceregion"
DEVICE_TIMEZONES: str = "gettimezones"
DEVICE_ROOMS: str = "getlocationtypes"
DEVICE_TRANSFER_OWNER: str = "transferowner"
DATA_LATEST: str = "getalllatestdata"
DATA_HOUR: str = "wtvsRh/gethourcolor"
DATA_DAY: str = "wtvsRh/getdaycolor"
DATA_WEEK: str = "wtvsRh/getweekcolor"
DATA_MONTH: str = "wtvsRh/getmonthcolor"
DATA_DOWNLOAD_HOUR: str = "wtvsRh/datahouravg"
DATA_DOWNLOAD_MINUTE: str = "wtvsRh/dataminute"
SHARE_TO_LIST: str = "sharetolist"
SHARE_TO_LIST_BIZ: str = "sharetolistbiz"
SHARE_DEVICE: str = "autosharedevice"
SHARE_DEVICE_SUPERADMIN: str = "sharedevicesa"
SHARE_DEVICE_ADMIN: str = "sharedeviceadmin"
SHARE_UNSHARE_DEVICE: str = "unsharedevice"
SHARE_UNSHARE_DEVICE_SUPERADMIN: str = "unsharedevicesa"
SHARE_UNSHARE_DEVICE_ADMIN: str = "unsharedeviceadmin"
SHARE_ACCEPT_DEVICE: str = "acceptsharedevice"
NOTIFS_ALL: str = "wtvsRh/allnotif"
NOTIFS_NEXT: str = "wtvsRh/allnotif"
NOTIFS_DEVICE: str = "wtvsRh/devicenotif"
NOTIFS_DEVICE_NEXT: str = "wtvsRh/devicenotif"
NOTIFS_DELETE: str = "deletedevicenotif"
NOTIFS_DEVICE_DELETE: str = "deletedevicenotif"
NOTIFS_SYSTEM: str = "systemnotifs"
NOTIFS_SETTINGS: str = "getnotifsettings"
NOTIFS_SETTINGS_SET: str = "notifsettings"
NOTIFS_SETTINGS_SET_QUEUE: str = "notifsettings"
THRESHOLDS_DEFAULT: str = "wtvsRh/thresholddefault"
THRESHOLDS_DEVICE: str = "wtvsRh/getdevicethreshold"
THRESHOLDS_DEVICE_EDIT: str = "thresholdupdateall"
SHOP_GET_ITEMS: str = "uhoolist"
PUSH_SET_DEVICE: str = "pushdevicecontrol"
PUSH_TEST: str = "pushtest"
INTEGRATE_IFTTT_USERTOKEN: str = "ifttttoken"
