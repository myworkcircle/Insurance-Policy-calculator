from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.conf import settings


class Render:

    @staticmethod
    def render(path: str, params: dict):
        
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        links    = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
        # pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),dest=response, link_callback=links)
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response,link_callback=links)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)
