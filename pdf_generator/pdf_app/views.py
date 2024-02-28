from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django_wkhtmltopdf.views import PDFTemplateResponse

def generate_pdf(request):
    template = get_template('pdf_template.html')
    context = {'data': 'Your PDF Data Here'}
    html = template.render(context)
    response = PDFTemplateResponse(request=request,
                                   template='pdf_template.html',
                                   filename='my_pdf.pdf',
                                   context=context,
                                   show_content_in_browser=False,
                                   cmd_options={'margin-top': 10, 'zoom': 1})
    return response
