import logging
from binance_d import RequestClient
from binance_d import SubscriptionClient
from binance_d.constant.test import *
from binance_d.model import *
from binance_d.exception.binanceapiexception import BinanceApiException

from binance_d.base.printobject import *

# Start user data stream
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
listen_key = request_client.start_user_data_stream()
#print("listenKey: ", listen_key)

# Keep user data stream
result = request_client.keep_user_data_stream()
#print("Result: ", result)

# Close user data stream
# result = request_client.close_user_data_stream()
# #print("Result: ", result)

logger = logging.getLogger("binance-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    


def error(e: 'BinanceApiException'):
    #print(e.error_code + e.error_message)

sub_client.subscribe_user_data_event(listen_key, callback, error)
