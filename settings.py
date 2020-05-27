'''''''''''''''''''''''''''
Current Supported Exchanges:
    binance & bybit
'''''''''''''''''''''''''''
chooseExchange = 'binance'

'''''''''''''''''''''''''''
Available Trading Pairs: 
btc, eth , link, bnb, bch, zec, trx, 
xrp, ada, eos, ltc, ect, xtz, neo
'''''''''''''''''''''''''''
tradingPair = 'link'

'''''''''''''''''''''''''''
Enter your API keys below they must have everything 
enabled except withdrawls for the bot to work properly.
'''''''''''''''''''''''''''
key = 'key goes here'
secret = 'secret goes here'


'''''''''''''''''''''''''''
To enable use Percent Balance for buys & sells 
you must set auto_qty to True, This will allow the bot to 
automatically calculate your qty based of your balance
'''''''''''''''''''''''''''
auto_qty = True

'''''''''''''''''''''''''''
Use Percentage values here to allow the bot to 
auto calculate the position sizing based of you balance.
Super SAFU = 0.05
Conservative = 0.1
Moderate = 0.2
Aggressive = 0.4
Insane = 0.6 +
The Bot will stop buying at you maxPostion value, this can be adjusted and is set low to protect your balance
'''''''''''''''''''''''''''
percentBal = 0.1
maxPosition = 20

'''''''''''''''''''''''''''
if auto_qty = False  set override value here otherwise ignore these settings,
this is for the user that want to set an exact qty of their buys and sells.
'''''''''''''''''''''''''''
longQty = 0.1
shortQty = 0.1

'''''''''''''''''''''''''''
VWAP offsets in percentage values, 
the bot will look to place orders ONLY
when price action is outside of this range
'''''''''''''''''''''''''''
long_vwap_offset = 3.75
short_vwap_offset = 3.75

'''''''''''''''''''''''''''
Set this on exchange to ISOLATED 
then make it match below to help calculate order sizing.
Suggested leverage for this bot is 3-5x, any higher becomes more risky.
'''''''''''''''''''''''''''
leverage = 5

'''''''''''''''''''''''''''
Set this to the size of liquidations you want to hunt for.
This will always be base on the base pair & size of the order.
example = 1000 LINK liquidated
example = 5 BTC liquidated
'''''''''''''''''''''''''''
lick_value = 10

'''''''''''''''''''''''''''
Take Profit & Stop Loss Values,
these values are a percentage %.
Please Ajust to your risk levels.
'''''''''''''''''''''''''''
take_profit = 0.5
stop_loss = 10

'''''''''''''''''''''''''''
User Authentication
For Binance Futures use  = 'ALPHA'
For Bybit use your UID once authed with @CryptoGnome#7769 or @TechHelpDrew#8510 in discord for access
'''''''''''''''''''''''''''
auth = 'ALPHA'

'''''''''''''''''''''''''''
POST NOTIFICATIONS TO DISCORD CHANNEL 
ENTER THE WEBHOOK ADDRESS FROM CHANNEL SETTINGS HERE
'''''''''''''''''''''''''''

discordwebhook = "webhook adress goes here"

'''''''''''''''''''''''''''
Special Settings
'''''''''''''''''''''''''''
# Speed Custimization [ADVANCED USERS ONLY]
delay = 0.7
sleep_on_stop = 1

# make false if you want to ignore licks
check_licks = True