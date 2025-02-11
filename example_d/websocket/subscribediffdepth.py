import logging
from binance_d import SubscriptionClient
from binance_d.constant.test import *
from binance_d.model import *
from binance_d.exception.binanceapiexception import BinanceApiException

from binance_d.base.printobject import *

logger = logging.getLogger("binance-futures")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    #if data_type == SubscribeMessageType.RESPONSE:
        #print("Event ID: ", event)
    if  data_type == SubscribeMessageType.PAYLOAD:
        #print("Event Type: ", event.eventType)
        #print("Event Time: ", event.eventTime)
        #print("transaction time: ", event.transactionTime)
        #print("Symbol: ", event.symbol)
        #print("first update Id from last stream: ", event.firstUpdateId)
        #print("last update Id from last stream: ", event.finalUpdateId)
        #print("last update Id in last stream: ", event.lastUpdateIdInlastStream)
        #print("=== Bids to be updated ===")
        #PrintMix.print_data(event.bids)
        #print("==========================")
        #print("=== Asks to be updated ===")
        #PrintMix.print_data(event.asks)
        #print("==========================")
        sub_client.unsubscribe_all()
    #else:
        #print("Unknown Data:")
    #print()


def error(e: 'BinanceApiException'):
    #print(e.error_code + e.error_message)

sub_client.subscribe_diff_depth_event("btcusd_200925", callback, error, update_time=UpdateTime.REALTIME)
#sub_client.subscribe_diff_depth_event("btcusd_200925", callback, error, update_time=UpdateTime.FAST)
#sub_client.subscribe_diff_depth_event("btcusd_200925", callback, error, update_time=UpdateTime.NORMAL)
#sub_client.subscribe_diff_depth_event("btcusd_200925", callback, error)
