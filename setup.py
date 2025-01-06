
from setuptools import setup, find_packages

setup(
    name="sms_sender_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "aliyun-python-sdk-core",
        "aliyun-python-sdk-dysmsapi",
    ],
    description="发送短信包",
    author="CJH",
    author_email="942130598@qq.com",
    url="https://github.com/chongjiahao223/sms_sender.git"
)