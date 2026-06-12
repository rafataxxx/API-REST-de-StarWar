import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(100), nullable=False, unique=True)


class Follower(Base):
    __tablename__ = 'follower'
    # Usamos composite primary key porque esta tabla intermedia no tiene un "ID" propio en tu diagrama
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

# Creamos un Enum para los tipos de media permitidos en Instagram


class MediaType(enum.Enum):
    IMAGE = "image"
    VIDEO = "video"
    REEL = "reel"


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

# 5. Tabla Comment


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! Revisa el archivo diagram.png en la raíz de tu proyecto")
except Exception as e:
    print("Hubo un problema generando el diagrama")
    raise e
