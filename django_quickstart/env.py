# -*- coding: utf-8 -*-
"""
Get setting from environment variable, key setting provide fake value

Usge:
	boolean: ENV_XXX_BOOL = (os.environ.get('ENV_XXX_BOOL', 'False') == 'True')
	str: 	 ENV_XXX_STR  = os.environ.get('ENV_XXX_STR', 'default_str')
	int:	 ENV_XXX_INT  = int(os.environ.get('ENV_XXX_INT', 0))
"""
import os


## django setting
ENV_DJ_SECRET_KEY = os.environ.get('DJ_ALLOWED_DOMAIN', '@c$c1ba%_xepk#7#@=@ia()1*+e3_w0af27a-vnim1z05364v!')
ENV_DJ_ALLOWED_HOSTS = os.environ.get('DJ_ALLOWED_DOMAIN', '*')
ENV_DJ_DEBUG_MODE = (os.environ.get('DJ_DEBUG_MODE', 'True') == 'True')


## MySQL
ENV_MYSQL_HOST = os.environ.get('MYSQL_HOST', "127.0.0.1")
ENV_MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
ENV_MYSQL_CHARSET = os.environ.get('MYSQL_CHARSET', 'utf8mb4')
ENV_MYSQL_ISOLATION_LEVEL = os.environ.get('ENV_MYSQL_ISOLATION_LEVEL', 'read committed')

ENV_MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME', 'django_quickstart')
ENV_MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
ENV_MYSQL_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD', '123456')


## PostgreSQL
ENV_POSTGRES_HOST = os.environ.get('POSTGRES_HOST', "127.0.0.1")
ENV_POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", 5432))

ENV_POSTGRES_DB = os.environ.get('POSTGRES_DB', 'django_quickstart')
ENV_POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
ENV_POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '123456')


## redis
ENV_REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
ENV_REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
ENV_REDIS_DB_NUM = int(os.environ.get("REDIS_DB_NUM", 0))


# RabbitMQ
ENV_RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST', '127.0.0.1')
ENV_RABBITMQ_PORT = int(os.environ.get('RABBITMQ_PORT', 5672))

ENV_RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER', 'admin')
ENV_RABBITMQ_DEFAULT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS', 'admin')
