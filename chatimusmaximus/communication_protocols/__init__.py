from communication_protocols.xmpp_client import ReadOnlyXMPPBot
from communication_protocols.javascript_webscraper import JavascriptWebscraper
from communication_protocols.socket_io_client import ReadOnlyWebSocket
from communication_protocols.irc_client import create_irc_bot, EchoToMessage

__all__ = ['ReadOnlyXMPPBot',
           'JavascriptWebscraper',
           'ReadOnlyWebSocket',
           'create_irc_bot',
           'EchoToMessage']
