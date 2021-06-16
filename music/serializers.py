from rest_framework import serializers

from music.models import Song, Album, Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'cover', 'source', 'listened')