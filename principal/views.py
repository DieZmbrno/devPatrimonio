from django.shortcuts import render, get_object_or_404, redirect
from .models import PuntoInteres, Usuario, Calificacion, HistorialVisitas, DestinoCultural, Comentario, PreguntaInteractiva, RecursoAdicional, Evaluacion
from .forms import ContactForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView

def lista_puntos_de_interes(request):
    puntos_de_interes = PuntoInteres.objects.all()
    return render(request, 'lista_puntos_de_interes.html', {'puntos_de_interes': puntos_de_interes})

def detalle_punto_de_interes(request, punto_interes_id):
    punto_interes = get_object_or_404(PuntoInteres, pk=punto_interes_id)
    return render(request, 'detalle_punto_de_interes.html', {'punto_interes': punto_interes})

def prueba(request):
    return render(request, 'prueba.html')

def index(request):
    return render(request, 'index.html')


class CustomLoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Utiliza authenticate para verificar las credenciales
        user = Usuario.objects.filter(username=username, password=password).first()

        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Inicio de sesión exitoso.')
            return redirect('index')
        else:
            messages.error(self.request, 'Usuario o contraseña incorrectos.')

        return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error en el formulario, revise los campos nuevamente.')
        return super().form_invalid(form)