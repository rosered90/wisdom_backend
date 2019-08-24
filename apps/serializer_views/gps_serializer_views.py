# _*_ coding:utf-8 _*_

from rest_framework import mixins, status, generics

from apps.models.gps_md import GpsModel
from apps.serializer.gps_serializer import GpsModelSerializer


class GpsModelView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    gps的查看和创建
    """
    queryset = GpsModel.objects.all()
    serializer_class = GpsModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GpsModelDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    """
    更新、删除
    """
    queryset = GpsModel.objects.all()
    serializer_class = GpsModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
