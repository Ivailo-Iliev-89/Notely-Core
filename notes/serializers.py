from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    # READ_ONLY
    # from here we not gave to setting client to change anything, only the set are from viewset 'perform_create'
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ['id', 'owner', 'title', 'content', 'created_at']
