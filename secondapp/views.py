from django.shortcuts import render
def show(request):
    curriculum = Curriculum.objects.all()
    html = ''
    for c in curriculum:
         html += c.id + '<br>'
         html += c.sido + '<br>'
         html += c.name + '<br>'
         html += c.medical + '<br>'
         html += c.room + '<br>'
         html += c.tel + '<br>'
         html += c.address + '<br>'
    return HttpResponse(html)
