
from django import forms
from rh.models import Colaborador, Cliente, Projeto
from validate_docbr import CPF, CNPJ


class ColaboradorForm(forms.ModelForm):

    def clean_cpf(self):
        cpf_digitado = self.cleaned_data.get("cpf")
        cpf_validador = CPF()
        if not cpf_validador.validate(cpf_digitado):
            raise forms.ValidationError("O CPF informado não é válido!")
        return cpf_validador.mask(cpf_digitado)

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
        fields = ["nome", "data_nascimento", "cpf", "cpffile", "errege", "rgfile", "endereco", "cidade", "estado", "pais", "telefone", "banco", "conta", "emailpessoal", "emailshoot", "foto", "funcaodobrother", "salario", "desligado"]


class ClienteForm(forms.ModelForm):

    def clean_cnpj(self):
        print("tô passando aqui")
        cnpj_digitado = self.cleaned_data.get("cnpj")
        cnpj_validador = CNPJ()
        if not cnpj_validador.validate(cnpj_digitado):
            raise forms.ValidationError("O CNPJ informado não é válido!")
        return cnpj_validador.mask(cnpj_digitado)

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

        model = Cliente
        fields = ["nome", "cnpj", "razaosocial", "logo", "nomecontato", "emailcontato", "fonecontato"]


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

    class Meta:

        model = Projeto
        fields = ["nome", "cliente", "numero", "valor_total", "desconto", "valor_final", "ativismo", "lucro", "lider_shoot", "colaboradores"]
        widgets = {
            "colaboradores": forms.CheckboxSelectMultiple,
        }
