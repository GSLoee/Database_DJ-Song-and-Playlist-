"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    songs = db.relationship('PlaylistSong', back_populates='playlist')


class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
    artist = db.Column(db.String(60), nullable=False)
    playlists = db.relationship('PlaylistSong', back_populates='song')



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlistsongs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    playlist = db.relationship('Playlist', back_populates='songs')
    song = db.relationship('Song', back_populates='playlists') 


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
