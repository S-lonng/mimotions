import requests, time, datetime, re,sys, json, random


agentid = 1000002
corpid = 'wwc628a1b8f3fcd830'

corpsecret = 'zLWnm9BNSNR0DEHCrQtb6HEr6CEo8thuZqSfxuS_c4g'


def get_access_token():
    params={
        'corpid':corpid,
        'corpsecret':corpsecret
    }
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params=params).json()
    #r = json.loads(r)
    #print(r)
    if r['errcode'] == 0:
        access_token_content = r['access_token']
        return {'errcode':0,'access_token':access_token_content}
    else:
        return {'errcode':r['errcode'],'errmsg':r['errmsg']}


def pushWX(msg):

    access_token_code = get_access_token()

    data = {
                    "touser" : "@all",
                    "toparty" : "@all",
                    "totag" : "@all",
                    "msgtype" : "text",
                    "agentid" : agentid,
                    "text" : {
                        "content" :msg
                    },
                    "safe":0,
                    "enable_id_trans": 0,
                    "enable_duplicate_check": 0,
                    "duplicate_check_interval": 1800
                }
    
    if access_token_code['errcode'] == 0:
        access_token = access_token_code['access_token']
    else:
        print(access_token_code)
    
    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}'.format(ACCESS_TOKEN=access_token),data = json.dumps(data)).json()
    if r['errcode'] == 0:
        print('微信推送成功')
    else:
        print(r)

pushWX('python test')
#get_access_token()