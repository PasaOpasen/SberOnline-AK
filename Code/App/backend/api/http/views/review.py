from rest_framework import generics, status
from rest_framework.response import Response
from api.services.content_detector.detector import get_content_from_text

from api.http.serializers import ReviewSerializer
from api.services.tonality.get_ton import tonality


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = ''

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        review = serializer.data['review']

        teams = get_content_from_text(review.split('\n'))
        review_tonality = tonality(review)

        return Response({"teams": teams, "tonality": review_tonality}, status=status.HTTP_201_CREATED, headers=headers)
