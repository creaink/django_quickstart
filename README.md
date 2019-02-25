# django quickstart

这是一个按照我的对 Django 使用使用，建立的一个 Django 的快速开发的初始化工程。同时也用于测试自己写的一些 Django 插件如：[django-tinymce-widget](https://github.com/creaink/django-tinymce-widget) 的示例工程。

## overview

依赖文件 `requirements.txt` 里面加入了写常用的依赖，同时通过对整个项目以 `FIXME` 为关键字全局搜索可以得到一些在定制化时候需要修改和考虑的地方。

默认在中间件 `middleware/exception_handle.py` 里面加入了一个用于捕获项目里未 catch 住的 exception 的中间件，然后记录在日志里面，建议是在每个可能 raise exception 的地方显示的处理，最好不要依赖这个中间件。

对于 log ，在 setting.py 里给出一个简单的配置，在 `apps/article/views.py` 有其示例用法。

对于扩展用户类，可以在 setting.py 里面去掉 `AUTH_USER_MODEL = 'account.User'` 的注释并修改为你自己的继承于 AbstractUser 的类即可。

### 项目结构

默认使用 `python ./manage.py startapp projName` 生成的 App 文件夹是位于 manage.py 文件的同级目录的，而一般的我会习惯在这个层次下存放很多其他的功能文件夹如 log, docs, scripts 等等。所以我将命令新生成新生成的 app 统一放于 `apps` 目录下，第三方的 App 存放于 `extra_apps` 目录下。

其他结构如 config 存放如: uwsgi, nginx, supervisor 和守护的配置文件。docs 存放文档，log 用于存储日志，media 用于存储用户上传的文件，middleware 用于存储中间件，scripts 用于存储一些脚本，static 用于存储前端收集的静态文件，templates 文件夹用于存放重载 Django 的默认模板文件，volumes 用于存储 Docker 化时候作为数据卷挂载的文件（如日志和配置文件等）。

### 配置

#### django 配置

为了方便用于生成环境、测试环境、开发环境的配置的隔离，这里将所有敏感的配置全部集中到由 `django_quickstart/env.py` 从环境变量中获取到 Python 变量当中，之后在 `django_quickstart/settings.py` 当中再赋予到 Django 的配置项。

当然为了快速开发 env.py 文件里提供了些默认的配置，而我建议的区分环境变量的配置方式的最佳实践是在 virtual env 的激活脚本里加上环境变量的设置，如 Windows 下的 `venv/Scripts/activate.(ps1/bat)` 文件，unix下的 `venv/bin/activate` 的虚拟环境激活脚本，在里面添加环境变量。

或者使用 supervisor 配置文件来导入环境变量。

#### supervisor 配置

supervisor 的配置文件存放于 `config/supervisord.conf` 该文件是基于默认配置的一些修改，主要将其日志输出更改为 `logfile=../log/supervisord.log`。并且最后将其配置 include 文件修改为 `files=conf/*.ini`，这样 supervisor 守护的配置文件就存放于 `config/conf/` 下，配置文件命名建议如： `app-uwsgi.ini`。

### nginx 配置

这里提供了两个 nginx 的配置文件示例，一个用于直接部署，一个用于 Docker 部署使用。**注意** 在直接部署的配置 nginx.conf 里面，由于部署路径未知，所以没有加入如 media static 的转发，但是可以参考 nginx-docker.conf 进行定制。

还有如 favicon.ico 的转发也没有放入，同时这两个配置里加入了限流，可以根据个人使用来修改。

建议在部署时候修改下 `/etc/nginx/nginx.conf` 里的 `server_tokens off;` 的注释打开，以去掉 HTTP 请求中的 server 头的服务器信息，同时将 gzip 的注释都去掉以开启 gzip 加快静态文件的传输。

在修改 nginx 配置的时候需要注意保持 uwsgi_pass 的端口要与 `config/conf/app-uwsgi.ini` 一致。
可以参考 [Let’s Encrypt 证书教程](https://www.hi-linux.com/posts/6968.html) 申请免费的证书，但是需要注意的是：**Let’s encrypt 的免费证书默认有效期为 90 天，到期后如果要续期需要执行：**

### 数据库配置

在 setting.py 里给出了 SQLite3, MySQL, PostgreSQL 等对于 Django 来说常用的数据库的配置，最后由 `DATABASES = DATABASES_SQLLTE` 语句来切换，关于数据库的配置大多都可以在环境变量中找到对应的值。

同时还提供了在单元测试时候使用内存中的 sqlite3 用于加速测试的配置，用 TESTING 变量进行判断。

## 其他集成

### django reset framework

在使用 django 过程当中难免要使用到 [Django REST framework](https://www.django-rest-framework.org)，同时我也常常使用 [django-rest-framework-jwt](https://github.com/GetBlimp/django-rest-framework-jwt) 用于用户认证鉴权。在 settings.py 里面我给出了这两个模块我用到的配置。

- 将 JWT 的 JWT_AUTH_HEADER_PREFIX 修改为 `Bearer`，这样便于 Postman 的测试。

- 修改了 DEFAULT_AUTHENTICATION_CLASSES 去掉了 SessionAuthentication 和 BasicAuthentication，只允许 JSONWebTokenAuthentication 方式的用户验证，进一步的前后端分离，同时采用 JWT 的话避免了 CSRF。

- 三是修改 DEFAULT_RENDERER_CLASSES，只允许返回 JSON 数据，默认情况下以浏览器访问接口会得到接口的操作页面。

### uwsgi

uwsgi 的配置文件位于在 `config/uwsgi.ini`，其内的参数如 processes threads 需要根据部署环境来具体配置，注意修改配置时候其服务端口要与 nginx 配置里的一致。如果不使用 supervisor 管理的话可以使用系统级别的 systemd 或者 sysinit 来守护。使用 supervisor 守护的启动配置位于 `config/conf/app-uwsgi.ini`。

### supervisor

[supervisord](http://supervisord.org) 我一般用于守护如 uwsgi 和 celery。用法：切换到 `config` 目录下，使用 `supervisord -nc supervisord.conf` 命令启动。其他用法如：

- `supervisorctl status` 查看状态
- `supervisorctl start/stop/restart uwsgi` 开始、停止、重启 uwsgi 程序
- `unlink /tmp/supervisor.sock` 根据套接字关闭守护服务
- `supervisorctl reread` 重载已有配置
- `supervisorctl update` 重新加载配置

### celery

对于需要定时的任务和大工作量的处理需要使用 [celery](http://www.celeryproject.org) 分布式任务队列了。这里配置的 celery 的 backed 使用的是 redis，使用的 json 方向序列化。

celery 的定时任务和 work 由 supervisord 使用 `config/conf/app-celery.ini` 配置文件来启动。

### docker

这里基于 python:3.6-stretch 和 python:3.6-alpine 两个基础镜像提供了两份 Dockerfile。在构建镜像时候首先在 Dockerfile 和 Dockerfile.alpine 里选择需要的依赖包，以减小镜像的体积，如果有第三方包需要安装还需要修改下，默认暴露的为 8050 端口为 uwsgi。

可以使用 Docker 方式部署，这里提供了一个参考的 docker-compose.yml 文件，提供了 redis, redis, nginx 等。基于 docker-compose 的方式可以方便使用 `*.env` 文件将环境变量传入，对于不同的环境的切换十分方便，默认会加载 `volumes/env/` 下相应的文件，详情见 docker-compose.yml 文件。

需要 **注意** 的是，必须提供一个 `volumes/env/django-quickstart.env` 文件，且其内需要有：

```env
REDIS_HOST=redis
```

`volumes` 目录下一般为容器挂载的目录，详情见 docker-compose.yml 和 Dockerfile。

## TODO

- [ ] docker-entrypoint 重写
