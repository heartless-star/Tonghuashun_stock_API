import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://stockpage.10jqka.com.cn',
    'platform': 'hxkline',
    'priority': 'u=1, i',
    'referer': 'https://stockpage.10jqka.com.cn/',
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Microsoft Edge";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'source-id': 'hxkline-NEWS_appNewsFlowHome_Page',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0',
    'x-auth-appname': 'AINVEST',
    'x-auth-progid': '7047',
    'x-auth-type': 'ths',
    'x-auth-version': '1.0',
    'x-fuyao-auth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRob3JpemVyX25hbWVzcGFjZSI6ImNvbW1vbi1ocS1hZ2dyIiwibGljZW5zZWVfdHlwZSI6IkZST05UX0FQUCIsImxpY2Vuc2VlX25hbWVzcGFjZSI6Imh4a2xpbmUtTkVXU19hcHBOZXdzRmxvd0hvbWVfUGFnZSJ9.ldrvWTheNnGOa_rH_buA6OoUpLtW2bhcdr3fABrGHbk',
}

json_data = {
    'code_list': [
        {
            'codes': [
                '000001',
            ],
            'market': '33',
        },
    ],
    'trade_class': 'post_market',
    'data_fields': [
        '7',
        '8',
        '9',
        '10',
        '11',
        '13',
        '19',
        '24',
        '30',
        '6',
        '264648',
        '199112',
        '1968584',
        '3153',
        '3541450',
        '3475914',
        '1771976',
        '65551',
    ],
    'lang': 'zh_hans',
    'gpid': 1,
}

response = requests.post(
    'https://quota-h.10jqka.com.cn/fuyao/common_hq_aggr/quote/v1/multi_last_snapshot',
    # cookies=cookies,
    headers=headers,
    json=json_data,
)
data = response.json()
quote = data['data']['quote_data'][0]
fields = quote['data_fields']
values = quote['value'][0]

# 字段代码 -> 含义映射
FIELD_MAP = {
    "11": "昨收",
    "13": "成交量(手)",
    "24": "现价",
    "65551": "均价",
    "3475914": "流通市值",
    "19": "成交额",
    "264648": "涨跌额",
    "3153": "市盈率(动)",
    "1968584": "换手率(%)",
    "3541450": "总市值",
    "1771976": "量比",
    "6": "昨收",
    "7": "卖一价",
    "8": "最高",
    "9": "最低",
    "199112": "涨跌幅(%)",
    "30": "最新价",
    "10": "开盘价",
}

print(f"{'代码':<6} {quote['code']}")
print(f"{'市场':<6} {quote['market']}")
print('=' * 40)
for code, val in zip(fields, values):
    name = FIELD_MAP.get(code, f"未知({code})")
    if val is None:
        display = 'N/A'
    elif isinstance(val, float) and abs(val) >= 1e8:
        display = f'{val:.2f}'
    else:
        display = val
    print(f"{name:<12} {display}")