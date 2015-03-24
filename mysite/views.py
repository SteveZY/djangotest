# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
#from django.template.loader import get_template
#from django.template import Context
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.shortcuts import render_to_response
from mysite.books.models import Book
from django.views.generic.simple import direct_to_template
from django.template import TemplateDoesNotExist
import datetime
import csv

def hi(reqest):
	return HttpResponse("Hi Nihao")

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template("datetime.html")
    #html = "<html><body>你好, It is now %s.</body></html>" % now
    #html0 = t.render(Context({'current_date': now}))
    return  render_to_response('datetime.html', {'current_date': now,'lowercase_name':'YONG ASDFSAF ZHANG'})
#HttpResponse(html0)
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
     	q = request.GET['q']
        #message = 'You searched for: %r' % request.GET['q']
        if not q:
        	errors.append('Enter a search term')
        elif len(q)>20:
        	errors.append('Please enter at most 20 characters')
        else:
	        #q = request.GET['q']
	        books = Book.objects.filter(title__icontains=q)
	        return render_to_response('search_results.html',
	            {'books': books, 'query': q})
        #else:
       # message = 'You submitted an empty form.'
    return render_to_response('search_form.html', {'errors': errors})
    #return HttpResponse(message)
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',
        {'errors': errors})

from mysite.forms import ContactForm
from django.template import RequestContext
#from django.core.context_processors import csrf
def contact_f(request):
    #errors = []
    if request.method == 'POST':
    	form = ContactForm(request.POST)
    	if form.is_valid():
    		cd = form.cleaned_data
    		send_mail(cd['subject'], 
    			cd['message'], 
    			cd.get('email', 'noreply@example.com'), 
    			['siteowner@example.com'],
    		)
    		return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial = {'subject':'I love your site!'})

    return render_to_response('contact_formf.html',
        {'form': form},context_instance = RequestContext(request))

def about_pages(request,page):
    try:
        return direct_to_template(request, template="about/%s.html" % page)
    except TemplateDoesNotExist:
        raise Http404()

UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]

def unruly_passengers_csv(request):#csv generator
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'

    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])

    return response

from cStringIO import StringIO
from reportlab import canvas
def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the response object as its "file."
    temp = StringIO()#Use StringIO to store the temp PDF file
    p = canvas.Canvas(temp)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    response.write(temp.getvalue())
    return response

