from reportlab.pdfgen import canvas
from django.http import HttpResponse
def pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="templates/education.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "yashwanth")
    p.showPage()
    p.save()
    return response

