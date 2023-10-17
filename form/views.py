from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = f"Nombre: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMensaje:\n{form.cleaned_data['message']}"
            send_mail(subject, message, 'luisernestoperezbello@gmail.com', ['luisernestoperezbello@gmail.com'])
            return redirect('/')  # Redirige a la URL de éxito después de enviar el correo
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
