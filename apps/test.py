import os

from apps.gps.consumers import push

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wisdom_backend.settings")

push('push_gps_info','I am zou')