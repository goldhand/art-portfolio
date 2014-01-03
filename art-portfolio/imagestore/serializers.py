from rest_framework import serializers
from imagestore.models import Album, Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    #content_type = serializers.Field(source='content_type')
    api_url = serializers.Field(source='get_api_url')
    sm_img_url = serializers.Field(source='get_sm_img_url')
    md_img_url = serializers.Field(source='get_md_img_url')
    lg_img_url = serializers.Field(source='get_lg_img_url')
    album = serializers.PrimaryKeyRelatedField(source='album')
    user = serializers.PrimaryKeyRelatedField(source='user')

    class Meta:
        model = Image
        fields = [
            'id',
            'url',
            'api_url',
            'sm_img_url',
            'md_img_url',
            'lg_img_url',
            'title',
            'description',
            'tags',
            'order',
            'image',
            'user',
            'url',
            'created',
            'updated',
            'album',

        ]
        read_only_fields = [
            'created',
            'updated',
        ]

