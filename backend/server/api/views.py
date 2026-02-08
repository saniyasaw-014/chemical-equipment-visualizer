from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Dataset
from .utils import analyze_csv

class UploadCSV(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        try:
            summary = analyze_csv(file)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        Dataset.objects.create(
            filename=file.name,
            summary=summary
        )

        # Keep only last 5 datasets
        if Dataset.objects.count() > 5:
            Dataset.objects.order_by("uploaded_at").first().delete()

        return Response(summary)

class LatestSummary(APIView):
    def get(self, request):
        dataset = Dataset.objects.last()
        if not dataset:
            return Response({"error": "No data available"}, status=404)
        return Response(dataset.summary)

class UploadHistory(APIView):
    def get(self, request):
        datasets = Dataset.objects.order_by('-uploaded_at')[:5]

        data = []
        for d in datasets:
            data.append({
                "filename": d.filename,
                "uploaded_at": d.uploaded_at,
                "summary": d.summary
            })

        return Response(data)
