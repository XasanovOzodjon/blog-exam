import json
from database import Base, engine, SessionLocal
from models import User, Post, Comment

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def load_demo_data():
    db = SessionLocal()
    with open("demo_data.json", "r") as f:
        data = json.load(f)

    # Users larni kriting
    users = []
    for user_data in data.get("users", []):
        user = User(username=user_data["username"], email=user_data["email"])
        users.append(user)
    db.add_all(users)
    db.commit()

    # Posts larni kriting
    posts = []
    for post in data.get("posts", []):
        post = Post(title=post["title"], body=post["body"], user_id=post["user_id"])
        posts.append(post)
    db.add_all(posts)
    db.commit()

    # Comments larni kriting
    comments = []
    for comment in data.get("comments", []):
        comment = Comment(text=comment["text"], user_id=comment["user_id"], post_id=comment["post_id"])
        comments.append(comment)
    db.add_all(comments)
    db.commit()

    db.close()

if __name__ == "__main__":
    init_db()
    load_demo_data()
    print("✅ Database initialized and demo data loaded!")
