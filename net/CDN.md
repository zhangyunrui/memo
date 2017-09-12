CDN -> nginx -> HTTPGenerator -> API Service
在CDN层面对页面和静态资源分别做缓存，但因为两者的回源路径不一样(static回源s3)，cloudfront支持，七牛未看到说明，所以需要把static拆分成独立域名，进而需要在 HTTPGenerator 层面拼接静态资源的绝对路径
ajax获取的数据无法被CDN缓存