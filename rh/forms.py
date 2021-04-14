
from django import forms
from rh.models import Colaborador
from validate_docbr import CPF


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
        fields = ["nome", "emaildapessoa", "funcaodobrother", "cpf", "data_nascimento", "foto", "desligado"]
