from django import forms
from django.core.mail.message import EmailMessage

class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=60)
    email = forms.EmailField(label='E-Mail')
    assunto = forms.CharField(label='Assunto', max_length=60)
    telefone = forms.CharField(label='Telefone com DDD', max_length=15)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n E-Mail: {email}\n Telefone: {telefone}\n Assunto: {assunto}\n Mensagem:\n{mensagem}'

        mail = EmailMessage(
            subject=f'Contato de {nome}',
            body=conteudo,
            from_email=email,
            to=['pedrohazevedo@gmail.com']
        )
        mail.send()