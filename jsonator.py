import json
import os
import requests
import codecs
import string
import re
import fileinput

# 192.168.1.15:1234
class getData:
    def __init__(self, get_url):
        print(self,'is there any url',get_url)
        self.get_url = get_url
        os.system('pip3 install requests')

    def fetchData(self):
        # API GET URL goes inside the quotes below DON'T CHANGE ANYTHING ELSE!
        print('self in  fetch data',self)
        resp_data = requests.get(self.get_url).json()
        formatted_data = resp_data['data']
        proc_data = json.dumps(formatted_data)

        precoded_data = """{
            "contractEtherDelta": "smart_contract/etherdelta.sol",
            "contractToken": "smart_contract/token.sol",
            "contractReserveToken": "smart_contract/reservetoken.sol",
            "contractEtherDeltaAddrs": [
                { "addr": "0x6323A8711180820b834c0295808c188E7F8cD9e7", "info": "Deployed 02/07/2019 -- THE CURRENT SMART CONTRACT" }
            ],
            "ethTestnet": false,
            "ethChainId": 1,
            "ethProvider": "http://localhost:8545",
            "ethGasPrice": 4000000000,
            "ethAddr": "0x0000000000000000000000000000000000000000",
            "ethAddrPrivateKey": "",
            "gasApprove": 250000,
            "gasDeposit": 250000,
            "gasWithdraw": 250000,
            "gasTrade": 250000,
            "gasOrder": 250000,
            "minOrderSize": 0.001,  
            "socketServer": "http://54.179.168.57:8080",
            "userCookie": "EtherDelta",
            "eventsCacheCookie": "EtherDelta_eventsCache",
            "ordersCacheCookie": "EtherDelta_ordersCache",
            "etherscanAPIKey": "GCGR1C9I17TYIRNYUDDEIJH1K5BRPH4UDE",
            "ledgerPath": "m/44'/60'/0'/0",
            "bases": [
                { "addr": "0x0000000000000000000000000000000000000000", "name": "ETH", "fullName": "Ethereum", "decimals": 18 }
            ],
            """
        
        test_file = open("config/main.json", "w")
        test_file.write(str(precoded_data)+str('"tokens":\n')+proc_data+ '\n'+str(""", "defaultPair": { "token": "TON", "base": "ETH" } \n}"""))
        
        # f = open("test.json",'r')
        # filedata = f.read()
        # f.close()

        # newdata = filedata.replace("{'addr':", '{"addr":')

        # f = open("test.json",'w')
        # f.write(newdata)
        # f.close()

# getIt = getData("https://backendtuneapi.herokuapp.com/gettokendata")
getIt=getData("http://ec2-13-229-250-134.ap-southeast-1.compute.amazonaws.com:3000/admin/deployed-tokens")

getIt.fetchData()


