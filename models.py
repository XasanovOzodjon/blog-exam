from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from database import Base


class User(Base):
    __tablename__ = "users"

    # column larni yarating
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    

    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    # column larni yarating
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class Comment(Base):
    __tablename__ = "comments"

    # column larni yarating
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
