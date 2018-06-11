# 京东618电商爬虫测试 #

----------
注：以笔记本为例


### 爬取主要思路 ###
1. 先确定url['https://list.jd.com/list.html?cat=670,671,672&page=1']('https://list.jd.com/list.html?cat=670,671,672&page=1')
2. 确定爬取字段信息
            
			--goods_info（商品详情）
			--goods_link（商品链接）
			--goods_price（商品价格）
			**goods_price_url（商品价格链接）**

3.分析页面
			
    页面中除了商品价格，都可以用xpath找到，商品价格是用json生产的

	数据，所以我们需要，使用浏览器的控制台来找到js文件，经过我的查

	找，一个文件名为‘mgets?callback’的文件就是当前页面30个（一半）

	的含有价格信息的文件，有两个这样命名的文件，然后，我们随便点击

	一个商品，进入商品详情页后，找到商品对应的id，然后将找到的

	文件链接修改为单个商品的，例：'https://p.3.cn/prices/mgets?&skuIds=J_{}%2&pduid=15286332332502030043335'
	
	{}中填写对应的id就可以得到一个标准的类json格式，提取我们想要

	的P（键名）就可以得到对应的商品价格
4.后续工作
	
	这个爬虫主要是对价格的寻找，后面都没有什么难度了，只要对
	
	scrapy框架稍微掌握就可以实现，在这个简单的爬取过程中，京东大

	佬对价格进行的反爬还是有点东西，如果找不到json文件~那我们只能

	动用selinum chrome的插件对页面进行抓取了