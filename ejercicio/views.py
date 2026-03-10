from django.shortcuts import render, redirect
from .forms import UniversidadForm

def registro(request):

    if request.method == "POST":
        form = UniversidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("exito")

    else:
        form = UniversidadForm()

    return render(request, "registro.html", {"form": form})