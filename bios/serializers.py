from rest_framework import fields, serializers
from .models import Bio


class BioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields='__all__'
        read_only_fields=['owner','published_date','updated_date']