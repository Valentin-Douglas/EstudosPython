from django.shortcuts import redirect, render
from .models import Transacao
from .forms import TransacaoForms


# Create your views here.
from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['Transação 1','Transação 2','Transação 3','Transação 4','Transação 5',]
    data['now'] = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'contas/form.html', {'form': form})