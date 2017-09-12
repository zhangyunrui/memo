### Video

#### Draft Video
```js
{
    "id": "id_of_video",
    "submitted_time": 123123, // UTC
    "author": "...",
    "thumbnail": <URI>
    "name": "name of video",
    "introduction": "...",
    "source_url": <URI>, // Video Address
    "tags": [{{ Tag }}],
    "is_released": true/false,
    "info_count": 5, // 取值大于等于0，OPTIONAL，当is_released为true时，不要此字段 
}
```

#### Released Video
```js
{
    "id": "id_of_video",
    "released_time": 123123, // UTC
    "author": "...",
    "thumbnail": <URI>
    "name": "name of video",
    "introduction": "...",
    "source_url": <URI>, // Video Address
    "tags": [{{ Tag }}],
    "info_count": 5, // 取值大于等于0，不为0时，显示"查看" 
    "reviewed_by": "...", // 审核人
}
```