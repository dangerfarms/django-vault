from django.forms import forms
from django.conf import settings

from django_vault.client import VaultSecretsClient


class RedisForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RedisForm, self).__init__(*args, **kwargs)

        client = VaultSecretsClient(settings.VAULT_NAMESPACE, settings.VAULT_HOSTNAME, settings.VAULT_TOKEN)
        keys = client.all
        for key in keys:
            self.fields[key] = forms.CharField()
