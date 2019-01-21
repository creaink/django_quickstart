FROM python:3.6-stretch

ENV TZ=Asia/Shanghai

ENV DJANGO_MAINAPP=django_quickstart

# change time zone, apt and pip source, chaneg default bash -> sh rather than dash
# aliyun mirrors.aliyun.com, mirrors.aliyun.com/pypi/simple
# tuna   mirrors.tuna.tsinghua.edu.cn, pypi.tuna.tsinghua.edu.cn/simple
# ustc   mirrors.ustc.edu.cn, mirrors.ustc.edu.cn/pypi/web/simple
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
	&& sed -i 's/\(archive\|security\).debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
    && printf "[global]\nindex-url=https://pypi.tuna.tsinghua.edu.cn/simple/" > /etc/pip.conf \
    && printf "[easy_install]\nindex-url=https://pypi.tuna.tsinghua.edu.cn/simple/" > ~/.pydistutils.cfg \
    && ln -sf bash /bin/sh

# install base and clean cache
# FIXME select package you need
RUN apt-get update \
    && apt-get install -y \
        netcat \
        mysql-client \
        redis-tools \
        supervisor \
    && rm -rf /var/cache/apt/* \
    && rm -rf /var/lib/apt/lists/*

# install python requirements
WORKDIR /root
COPY requirements.txt .
RUN pip install -r requirements.txt \
    && rm -rf ~/.cache/pip


# copy code to WORKDIR
COPY . .

EXPOSE 8080

VOLUME [ "/root/log", \
         "/root/media" \
         ]

WORKDIR /root/config

# check if supervisorctl is healthy
HEALTHCHECK --interval=5m --timeout=15s --retries=2 \
    CMD supervisorctl status | grep -Eo 'STOPPED|STARTING' | wc -l | \
        test 0 -ne $(cat) && exit 1 || exit 0

ENTRYPOINT [ "../scripts/docker-entrypoint.sh" ]
