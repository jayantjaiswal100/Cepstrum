from rest_framework import fields, serializers
from .models import PaperMan


class PaperManSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaperMan
        fields='__all__'
