from enum import Enum


class DecodeConstants(object):
    UTF8 = 'utf-8'


class WebSocketMessageType(object):
    USER_NEW = 'new-user'
    USER_CONNECTED = 'user-connected'
    USER_DISCONNECTED = 'user-disconnected'
    USER_AVATAR_UPDATED = 'user-avatar-updated'
    USER_AVATAR_DELETED = 'user-avatar-deleted'
    USER_INFO_UPDATED = 'user-info-updated'
    USER_USERNAME_CHANGED = 'username-changed'
    USER_EMAIL_CHANGED = 'email-changed'
    USER_STATUS_LIST = 'user-status-list'
    USER_SYNCHRONIZE = 'synchronize-users'
    USER_LOCK = 'lockUser'

    NOTIFICATION_UPDATE_SETTINGS = 'update-notification-settings'
    STATE_OF_FIELD_CHANGE = 'state-of-field-change'

    ROOM_NEW = 'new-room'
    ROOM_NEW_DIRECT = 'new-direct-room'
    ROOM_DISABLE = 'disable-room'
    ROOM_DELETE = 'remove-room'
    ROOM_SUBSCRIBE = 'subscribe'
    ROOM_UNSUBSCRIBE = 'unsubscribe'
    ROOM_CHANGE_INFO = 'change-room-info'
    ROOM_INVITE = 'invite'
    ROOM_DISMISS = 'dismiss'
    ROOM_STARRED = 'starred-room'
    ROOM_UNSTARRED = 'unstarred-room'
    ROOM_DIRECT_VISIBILITY = 'direct-room-visibility'
    ROOM_UPDATE_ACL = 'update-room-acls'
    ROOM_UPDATE_ADMINS = 'update-room-admins'

    MESSAGE_NEW = 'new-message'
    MESSAGE_MARK_AS_READ = 'mark-as-read'
    MESSAGE_MARK_AS_UNREAD = 'mark-as-unread'
    MESSAGE_NEW_LINK = 'new-message-links'
    MESSAGE_EDIT = 'edit-message'
    MESSAGE_EDIT_TEXT_FILE = 'edit-text-file'
    MESSAGE_STARRED = 'starred-message'
    MESSAGE_UNSTARRED = 'unstarred-message'
    MESSAGE_DELETE = 'delete-message'
    MESSAGE_PIN_ITEM = 'pin-item'
    MESSAGE_UNPIN_ITEM = 'unpin-item'
    MESSAGE_ADD_REACTION = 'add-reaction'
    MESSAGE_REMOVE_REACTION = 'remove-reaction'
    MESSAGE_TYPING = 'someone-typing-message'


class ContentType(object):
    ALL = '*/*'
    APPLICATION_ATOM_XML = 'application/atom+xml'
    APPLICATION_FORM_URLENCODED = 'application/x-www-form-urlencoded'
    APPLICATION_JSON = 'application/json'
    APPLICATION_JSON_UTF8 = 'application/json;charset=UTF-8'
    APPLICATION_OCTET_STREAM = 'application/octet-stream'
    APPLICATION_PDF = 'application/pdf'
    APPLICATION_PROBLEM_JSON = 'application/problem+json'
    APPLICATION_PROBLEM_JSON_UTF8 = 'application/problem+json;charset=UTF-8'
    APPLICATION_PROBLEM_XML = 'application/problem+xml'
    APPLICATION_RSS_XML = 'application/rss+xml'
    APPLICATION_STREAM_JSON = 'application/stream+json'
    APPLICATION_XHTML_XML = 'application/xhtml+xml'
    APPLICATION_XML = 'application/xml'
    IMAGE_GIF = 'image/gif'
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_PNG = 'image/png'
    MULTIPART_FORM_DATA = 'multipart/form-data'
    TEXT_EVENT_STREAM = 'text/event-stream'
    TEXT_HTML = 'text/html'
    TEXT_MARKDOWN = 'text/markdown'
    TEXT_PLAIN = 'text/plain'
    TEXT_XML = 'text/xml'
    TEXT_SCV = 'text/csv'


class HttpHeaders(object):
    ACCEPT = "Accept"
    ACCEPT_CHARSET = "Accept-Charset"
    ACCEPT_ENCODING = "Accept-Encoding"
    ACCEPT_LANGUAGE = "Accept-Language"
    ACCEPT_RANGES = "Accept-Ranges"
    ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
    ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
    ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
    ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
    ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
    ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"
    ACCESS_CONTROL_REQUEST_HEADERS = "Access-Control-Request-Headers"
    ACCESS_CONTROL_REQUEST_METHOD = "Access-Control-Request-Method"
    AGE = "Age"
    ALLOW = "Allow"
    AUTHORIZATION = "Authorization"
    CACHE_CONTROL = "Cache-Control"
    CONNECTION = "Connection"
    CONTENT_ENCODING = "Content-Encoding"
    CONTENT_DISPOSITION = "Content-Disposition"
    CONTENT_LANGUAGE = "Content-Language"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_LOCATION = "Content-Location"
    CONTENT_RANGE = "Content-Range"
    CONTENT_TYPE = "Content-Type"
    COOKIE = "Cookie"
    DATE = "Date"
    ETAG = "ETag"
    EXPECT = "Expect"
    EXPIRES = "Expires"
    FROM = "From"
    HOST = "Host"
    IF_MATCH = "If-Match"
    IF_MODIFIED_SINCE = "If-Modified-Since"
    IF_NONE_MATCH = "If-None-Match"
    IF_RANGE = "If-Range"
    IF_UNMODIFIED_SINCE = "If-Unmodified-Since"
    LAST_MODIFIED = "Last-Modified"
    LINK = "Link"
    LOCATION = "Location"
    MAX_FORWARDS = "Max-Forwards"
    ORIGIN = "Origin"
    PRAGMA = "Pragma"
    PROXY_AUTHENTICATE = "Proxy-Authenticate"
    PROXY_AUTHORIZATION = "Proxy-Authorization"
    RANGE = "Range"
    REFERER = "Referer"
    RETRY_AFTER = "Retry-After"
    SERVER = "Server"
    SET_COOKIE = "Set-Cookie"
    SET_COOKIE2 = "Set-Cookie2"
    TE = "TE"
    TRAILER = "Trailer"
    TRANSFER_ENCODING = "Transfer-Encoding"
    UPGRADE = "Upgrade"
    USER_AGENT = "User-Agent"
    VARY = "Vary"
    VIA = "Via"
    WARNING = "Warning"
    WWW_AUTHENTICATE = "WWW-Authenticate"
