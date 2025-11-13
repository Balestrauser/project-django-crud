# core/views.py
from django.shortcuts import render, redirect # 1. Adicione 'redirect'
from .models import Funcionario, Alimento # 1. Importa seus "moldes"

# Esta é a "tradução" da sua função 'listar_funcionarios'
def lista_funcionarios(request):
    
    # 2. Pede ao Django para buscar TODOS os objetos Funcionario no banco.
    #    Isto substitui seu 'carregar_dados()' e o 'for func in dados["funcionarios"]'
    todos_os_funcionarios = Funcionario.objects.all()

    # 3. Prepara os dados para enviar ao HTML.
    #    Vamos chamar a variável no HTML de 'funcionarios'.
    contexto = {
        'funcionarios': todos_os_funcionarios
    }

    # 4. Renderiza (exibe) um arquivo HTML, passando os dados (contexto) para ele.
    #    (Nós ainda não criamos este HTML, será o próximo passo).
    return render(request, 'core/lista_funcionarios.html', contexto)

# Vamos fazer o mesmo para a lista de alimentos
def lista_alimentos(request):
    
    # 1. Pede ao Django para buscar TODOS os Alimentos no banco.
    todos_os_alimentos = Alimento.objects.all()

    # 2. Prepara o contexto para o HTML
    contexto = {
        'alimentos': todos_os_alimentos
    }
    
    # 3. Renderiza o HTML (será nosso próximo passo)
    return render(request, 'core/lista_alimentos.html', contexto)
# core/views.py
# ... (mantenha as funções lista_funcionarios e lista_alimentos) ...

# Esta é a "tradução" da sua função 'cadastrar_funcionario'
def cadastrar_funcionario(request):
    
    # Esta é a lógica principal:
    # Se o método for POST, significa que o usuário enviou o formulário
    if request.method == 'POST':
        
        # 1. Pega os dados do formulário (substitui seus 'input()')
        nome_form = request.POST.get('nome')
        idade_form = request.POST.get('idade')
        sexo_form = request.POST.get('sexo')
        
        # 2. Cria o novo funcionário no banco de dados (substitui seu '.append()')
        #    O Django cuida da 'matricula' automaticamente
        Funcionario.objects.create(
            nome=nome_form,
            idade=idade_form,
            sexo=sexo_form
        )
        
        # 3. Redireciona o usuário de volta para a página da lista
        #    'lista_funcionarios' é o 'name' que demos para a URL no core/urls.py
        return redirect('lista_funcionarios')
        
    # Se o método NÃO for POST (ou seja, for GET),
    # o usuário está apenas pedindo para VER a página de cadastro.
    # Então, apenas mostre o HTML do formulário.
    return render(request, 'core/cadastrar_funcionario.html')