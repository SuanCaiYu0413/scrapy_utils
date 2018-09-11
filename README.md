# scrapy_utils
scrapy分享一些可以公共使用的中间价，扩展等

---

# 安装

```bash
git clone https://github.com/SuanCaiYu0413/scrapy_utils.git

cd scrapy_utils

python setup.py install

```

---

# 使用

* scrapy项目下的setting.py设置

```python

DOWNLOADER_MIDDLEWARES = {
     # 添加该项为每个请求随机使用UserAgent
    'scrapy_utils.downloadermiddlewares.RoundUserAgent.RoundUserAgent':545
}

# 随机用的UserAgent列表(可选，内置了一些网上收集的UserAgent)
UTILS_USER_AGENTS = ['user-agent1','user-agent2',...]

```