
from django import forms
from validate_docbr import CNPJ, CPF

from rh.models import Cliente, Clima, Colaborador, Contato, Curso, Projeto, Palestra


class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ["nome", "email", "mensagem"]

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'mensagem': forms.Textarea(attrs={'class':'form-control'}),
        }

class ColaboradorForm(forms.ModelForm):

    def clean_cpf(self):
        cpf_digitado = self.cleaned_data.get("cpf")
        cpf_validador = CPF()
        if not cpf_validador.validate(cpf_digitado):
            raise forms.ValidationError("O CPF informado não é válido!")
        # Estamos passando somente o only_digits porque zica se utilizarmos o cpf_validator com
        # os caracters não dígitos. Exemplo: . e -
        return cpf_validador.mask(cpf_validador._only_digits(cpf_digitado))

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        caracteres_nao_permitidos = '!"#$%&\'()*+/:;<=>?@[\\]^_`{|}~'
        for c in caracteres_nao_permitidos:
            if c in nome:
                raise forms.ValidationError("O campo nome não pode ter o caracter '%s'!" % c)
        nomes = nome.split()
        if len(nomes) == 1:
            raise forms.ValidationError("O campo nome tem que ter nome e sobrenome!")
        return nome

    class Meta:

        model = Colaborador
        fields = ["nome", "user", "bio", "data_nascimento", "cpf", "cpffile", "errege", "rgfile", "endereco", "bairro", "cep", "cidade", "estado", "pais", "telefone", "agencia", "banco", "conta", "emailpessoal", "emailshoot", "foto", "funcaodobrother", "salario", "instagram","linkedin","facebook", "entrounashoot", "desligado"]


class ClienteForm(forms.ModelForm):

    def clean_cnpj(self):
        print("tô passando aqui")
        cnpj_digitado = self.cleaned_data.get("cnpj")
        cnpj_validador = CNPJ()
        if not cnpj_validador.validate(cnpj_digitado):
            raise forms.ValidationError("O CNPJ informado não é válido!")
        return cnpj_validador.mask(cnpj_digitado)

    class Meta:

        model = Cliente
        fields = ["nome", "cnpj", "razaosocial", "logo", "nomecontato", "emailcontato", "fonecontato", "lider_shoot", "inicio", "fim"]


class ProjetoForm(forms.ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        caracteres_nao_permitidos = '!"#$%&\'()*+/:;<=>?@[\\]^_`{|}~'
        for c in caracteres_nao_permitidos:
            if c in nome:
                raise forms.ValidationError("O campo nome não pode ter o caracter '%s'!" % c)
        nomes = nome.split()
        if len(nomes) == 1:
            raise forms.ValidationError("O campo nome tem que ter nome e sobrenome!")
        return nome

    # Este método será executado sempre que ele terminar todas as validações extras do formulário (neste caso, clean_nome),
    # e depois vai chamar essa função. Utiliza-se para validar dois ou mais campos ao mesmo tempo.
    def clean(self):
        # Primeiro, buscamos todos os campos já validados pela super classe
        cleaned_data = super().clean()
        # Agora, buscamos o campo onde está definido quem é o líder
        lider_shoot = cleaned_data.get("lider_shoot")
        # Buscamos também, todos os colaboradores selecionados no formulário
        colaboradores = cleaned_data.get("colaboradores")
        # Caso tenha sido informado o líder
        if lider_shoot:
            # E agora caso o líder esteja na lista dos colaboradores.
            if lider_shoot in colaboradores:
                # O primeiro parâmetro, é o campo o erro será informado
                self.add_error("lider_shoot", "Se a pessoa é líder, ela não pode estar na lista de colaboradores.")
                self.add_error("colaboradores", "O Tuli mandou dizer que o %s (%s) não pode estar aqui." % (lider_shoot.cpf, lider_shoot.nome))
        return cleaned_data

    class Meta:

        model = Projeto
        fields = ["nome", "numero","lider_shoot", "colaboradores", "cliente", "resumo", "ativo", "data_inicio"]
        widgets = {
            "colaboradores": forms.CheckboxSelectMultiple,
        }


class ClimaForm(forms.ModelForm):

    class Meta:

        model = Clima
        fields = ["nome", "desc", "quando", "paraquem"]
        widgets = {
            "paraquem": forms.CheckboxSelectMultiple,
        }


class PalestraForm(forms.ModelForm):
    
    class Meta:

        model = Palestra
        fields = ["nome", "desc", "quem"]
        widgets = {
            "quem": forms.CheckboxSelectMultiple,
        }


class CursoForm(forms.ModelForm):

    class Meta:

        model = Curso
        fields = ["qual", "quando", "paraquem", "verba"]
        widgets = {
            "paraquem": forms.RadioSelect,
        }
