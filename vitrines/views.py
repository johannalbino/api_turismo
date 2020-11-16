from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from vitrines.models import Vitrines, About
from vitrines.serializer import VitrinesSerializer
from vitrines.filter import VitrinesFilter
from rest_framework.permissions import AllowAny


class VitrinesViewSet(GenericAPIView):
    """
    View Set para os metodos da API e listagem de vitrines
    """
    serializer_class = VitrinesSerializer
    filterset_class = VitrinesFilter
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        filter_routes = request.data.get('routes')
        if 'sobre' in filter_routes[0]:
            serializer = self.get_serializer(About.objects.all(), many=True)
            return Response(serializer.data)
        else:
            queryset = self.filter_queryset(Vitrines.objects.all())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                response = {
                    "title": "Melhores Hotéis",
                    "subtitle": "Veja os hotéis mais procurados",
                    "routes": ["/", "/destinos"],
                    "itens": serializer.data
                }
                return Response(response)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Vitrines.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = {
                "title": "Melhores Hotéis",
                "subtitle": "Veja os hotéis mais procurados",
                "routes": ["/", "/destinos"],
                "itens": serializer.data
            }
            return Response(response)
