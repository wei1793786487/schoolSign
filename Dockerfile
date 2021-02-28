FROM python

COPY *.py /

RUN pip install requests -i https://mirrors.aliyun.com/pypi/simple/  \
&&pip install apscheduler -i https://mirrors.aliyun.com/pypi/simple \
&& pip install pymongo -i https://mirrors.aliyun.com/pypi/simple

ENV TIME_ZONE=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime && echo $TIME_ZONE > /etc/timezone

CMD python schoolTask.py