from django.shortcuts import render
from .forms import UniversidadForm


def formulario_view(request):

    if request.method == 'POST':

        form = UniversidadForm(request.POST)

        if form.is_valid():
            print("FORMULARIO VÁLIDO")

            # Guardar en la base de datos
            universidad = form.save()

            # Mostrar datos guardados en consola
            for campo, valor in form.cleaned_data.items():
                print(f"{campo}: {valor}")

            return render(
                request,
                'ejercicio/formulario.html',
                {
                    'form': UniversidadForm(),  # limpiar formulario
                    'success': True,
                    'usuario': universidad
                }
            )

        else:
            print("FORMULARIO INVÁLIDO")
            print(form.errors)

    else:
        form = UniversidadForm()

    return render(
        request,
        'ejercicio/formulario.html',
        {'form': form}
    )


def scroll_view(request):
    return render(request, 'ejercicio/scroll.html')