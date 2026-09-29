from django.shortcuts import render


def dashboard(request):
    return render(request, "core/dashboard.html")


def novo_servico(request):
    return render(request, "core/novo_servico.html")


def detalhe_servico(request):
    return render(request, "core/detalhe_servico.html")
