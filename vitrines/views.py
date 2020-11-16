from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from vitrines.models import Vitrines
from vitrines.serializer import VitrinesSerializer
from vitrines.filter import VitrinesFilter
from rest_framework.permissions import AllowAny


class VitrinesViewSet(GenericAPIView):
    """
    View Set para os metodos da API e listagem de vitrines
    """
    serializer_class = VitrinesSerializer
    queryset = Vitrines.objects.all()
    filterset_class = VitrinesFilter
    permission_classes = [AllowAny]

    def post(self, request):
        pass

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Vitrines.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
