import csv
from rest_framework.renderers import BaseRenderer
from django.http import HttpResponse

class CSVRenderer(BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'
    charset = 'utf-8'
    render_style = 'text'

    def render(self, data, media_type=None, renderer_context=None):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'

        if not data:
            return response

        if isinstance(data, dict):
            data = [data]  # Преобразуем в список, если один объект

        writer = csv.writer(response)
        headers = data[0].keys()
        writer.writerow(headers)

        for item in data:
            writer.writerow(item.values())

        return response
