#!/usr/bin/env python2
# coding=utf-8

import plotly.plotly as py

buckets = [
    {
        "key": "All",
        "doc_count": 117,
        "max_routerReply_routerRecv": {
            "value": 2792
        },
        "max_serverRecv_routerReply": {
            "value": 164
        },
        "avg_totalTime": {
            "value": 1290.4017094017095
        },
        "count": {
            "value": 117
        },
        "avg_serverInitial_appSend": {
            "value": 588.1794871794872
        },
        "avg_routerReply_routerRecv": {
            "value": 1018.2393162393163
        },
        "avg_serverSend_routerRecv": {
            "value": -5.538461538461538
        },
        "max_serverSend_routerRecv": {
            "value": 9
        },
        "max_totalTime": {
            "value": 3055
        },
        "max_serverInitial_appSend": {
            "value": 1763
        },
        "avg_serverRecv_routerReply": {
            "value": 132.94871794871796
        },
        "avg_end_serverReply": {
            "value": -465.8974358974359
        },
        "max_end_serverReply": {
            "value": -179
        }
    },
    {
        "key": "mesh.info.wan.stats.get",
        "doc_count": 50,
        "max_routerReply_routerRecv": {
            "value": 1397
        },
        "max_serverRecv_routerReply": {
            "value": 164
        },
        "avg_totalTime": {
            "value": 1523.78
        },
        "count": {
            "value": 50
        },
        "avg_serverInitial_appSend": {
            "value": 614.96
        },
        "avg_routerReply_routerRecv": {
            "value": 1223.46
        },
        "avg_serverSend_routerRecv": {
            "value": -0.16
        },
        "max_serverSend_routerRecv": {
            "value": 9
        },
        "max_totalTime": {
            "value": 2603
        },
        "max_serverInitial_appSend": {
            "value": 1763
        },
        "avg_serverRecv_routerReply": {
            "value": 133.34
        },
        "avg_end_serverReply": {
            "value": -459.42
        },
        "max_end_serverReply": {
            "value": -184
        }
    },
    {
        "key": "mesh.device.count.get",
        "doc_count": 26,
        "max_routerReply_routerRecv": {
            "value": 290
        },
        "max_serverRecv_routerReply": {
            "value": 148
        },
        "avg_totalTime": {
            "value": 436.46153846153845
        },
        "count": {
            "value": 26
        },
        "avg_serverInitial_appSend": {
            "value": 555.1923076923077
        },
        "avg_routerReply_routerRecv": {
            "value": 191.23076923076923
        },
        "avg_serverSend_routerRecv": {
            "value": -1.9230769230769231
        },
        "max_serverSend_routerRecv": {
            "value": 7
        },
        "max_totalTime": {
            "value": 571
        },
        "max_serverInitial_appSend": {
            "value": 717
        },
        "avg_serverRecv_routerReply": {
            "value": 131.73076923076923
        },
        "avg_end_serverReply": {
            "value": -454.7692307692308
        },
        "max_end_serverReply": {
            "value": -189
        }
    },
    {
        "key": "mesh.info.get",
        "doc_count": 21,
        "max_routerReply_routerRecv": {
            "value": 1478
        },
        "max_serverRecv_routerReply": {
            "value": 148
        },
        "avg_totalTime": {
            "value": 1566.952380952381
        },
        "count": {
            "value": 21
        },
        "avg_serverInitial_appSend": {
            "value": 565.4285714285714
        },
        "avg_routerReply_routerRecv": {
            "value": 1313.5238095238096
        },
        "avg_serverSend_routerRecv": {
            "value": -17
        },
        "max_serverSend_routerRecv": {
            "value": 8
        },
        "max_totalTime": {
            "value": 1873
        },
        "max_serverInitial_appSend": {
            "value": 722
        },
        "avg_serverRecv_routerReply": {
            "value": 132.38095238095238
        },
        "avg_end_serverReply": {
            "value": -472.5238095238095
        },
        "max_end_serverReply": {
            "value": -229
        }
    },
    {
        "key": "mesh.node.get",
        "doc_count": 17,
        "max_routerReply_routerRecv": {
            "value": 1505
        },
        "max_serverRecv_routerReply": {
            "value": 150
        },
        "avg_totalTime": {
            "value": 1550.9411764705883
        },
        "count": {
            "value": 17
        },
        "avg_serverInitial_appSend": {
            "value": 566.2941176470588
        },
        "avg_routerReply_routerRecv": {
            "value": 1310.0588235294117
        },
        "avg_serverSend_routerRecv": {
            "value": -2.1176470588235294
        },
        "max_serverSend_routerRecv": {
            "value": 8
        },
        "max_totalTime": {
            "value": 1808
        },
        "max_serverInitial_appSend": {
            "value": 719
        },
        "avg_serverRecv_routerReply": {
            "value": 133.88235294117646
        },
        "avg_end_serverReply": {
            "value": -473.3529411764706
        },
        "max_end_serverReply": {
            "value": -179
        }
    },
    {
        "key": "mesh.gateway.bind",
        "doc_count": 2,
        "max_routerReply_routerRecv": {
            "value": 179
        },
        "max_serverRecv_routerReply": {
            "value": 140
        },
        "avg_totalTime": {
            "value": 556.5
        },
        "count": {
            "value": 2
        },
        "avg_serverInitial_appSend": {
            "value": 729
        },
        "avg_routerReply_routerRecv": {
            "value": 171
        },
        "avg_serverSend_routerRecv": {
            "value": -102.5
        },
        "max_serverSend_routerRecv": {
            "value": 6
        },
        "max_totalTime": {
            "value": 703
        },
        "max_serverInitial_appSend": {
            "value": 780
        },
        "avg_serverRecv_routerReply": {
            "value": 137
        },
        "avg_end_serverReply": {
            "value": -598.5
        },
        "max_end_serverReply": {
            "value": -575
        }
    },
    {
        "key": "mesh.node.reset",
        "doc_count": 1,
        "max_routerReply_routerRecv": {
            "value": 2792
        },
        "max_totalTime": {
            "value": 3055
        },
        "max_serverInitial_appSend": {
            "value": 675
        },
        "avg_serverRecv_routerReply": {
            "value": 133
        },
        "max_serverRecv_routerReply": {
            "value": 133
        },
        "avg_totalTime": {
            "value": 3055
        },
        "count": {
            "value": 1
        },
        "avg_serverInitial_appSend": {
            "value": 675
        },
        "avg_end_serverReply": {
            "value": -548
        },
        "avg_routerReply_routerRecv": {
            "value": 2792
        },
        "avg_serverSend_routerRecv": {
            "value": 8
        },
        "max_serverSend_routerRecv": {
            "value": 8
        },
        "max_end_serverReply": {
            "value": -548
        }
    }
]

x = ['{}\n{}appears'.format(i['key'], i['count']['value']) for i in buckets]

trace2 = {
    'x': x,
    'y': [int(i['avg_end_serverReply']['value'] + i['avg_serverInitial_appSend']['value']) for i in buckets],
    'name': 'netTime',
    'type': 'bar'
}
trace3 = {
    'x': x,
    'y': [
        int(i['avg_totalTime']['value'] - i['avg_routerReply_routerRecv']['value'] - i['avg_end_serverReply']['value'] -
            i['avg_serverInitial_appSend']['value'])
        for i in buckets],
    'name': 'server_mqttTime',
    'type': 'bar'
}
trace1 = {
    'x': x,
    'y': [int(i['avg_routerReply_routerRecv']['value']) for i in buckets],
    'name': 'routerTime',
    'type': 'bar'
}

data = [trace2, trace3, trace1]
layout = {
    'xaxis': {'title': 'Method'},
    'yaxis': {'title': 'Time ms'},
    'barmode': 'relative',
    'title': 'API Speeds'
}
py.iplot({'data': data, 'layout': layout}, filename='api_speeds', auto_open=True)
