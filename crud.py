from sqlalchemy.orm import Session
from models import User, Post, Comment

# CRUD
def create_user(db: Session, username: str, email: str):
    user = User(username = username, email = email)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def create_post(db: Session, user_id: int, title: str, body: str):
    post = Post(title = title, body = body, user_id = user_id)

    db.add(post)
    db.commit()
    db.refresh(post)
    return post
def create_comment(db: Session, user_id: int, post_id: int, text: str):
    comment = Comment(text = text, user_id = user_id, post_id = post_id)

    db.add(comment)
    db.commit()

def update_post(db: Session, post_id: int, title: str, body: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.title = title
        post.body = body
        
        db.commit()
        db.refresh(post)
        return post

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()



# Queries
def get_user_posts(db: Session, user_id: int):
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    return posts

def get_post_comment_count(db: Session, post_id: int):
    count = db.query(Comment).filter(Comment.post_id == post_id).count()
    return count

def get_latest_posts(db: Session, limit: int = 5):
    posts = db.query(Post).order_by(Post.id.desc()).limit(limit).all()
    return posts

def search_posts_by_title(db: Session, keyword: str):
    posts = db.query(Post).filter(Post.title.ilike(f"%{keyword}%")).all()
    return posts

def paginate_posts(db: Session, page: int = 1, per_page: int = 5):
    ofsert = (page - 1) * per_page
    posts = db.query(Post).offset(offset=ofsert).limit(per_page).all()
    return posts
