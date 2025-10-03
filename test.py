from database import SessionLocal
import crud

db = SessionLocal()

# Test: user qo‘shish
user = crud.create_user(db, "test_user", "test@example.com")
print("\nCreated User:", user.username)


# Test: user postlari
posts = crud.get_user_posts(db, user.id)
print("\nUser posts:", posts)

# Qolgan function larni ham shu yerda test qiling:

# Test: post yaratish
post = crud.create_post(db, user.id, "Yangi Post", "Lorem ipsum dolor sit amet.")
print("\nCreated Post:", post.title)

# Test: Comment qo'shish
crud.create_comment(db, user.id, post.id, "Bu birinchi komment!")
print("\nComment added to post.")

# Test: post yangilash
post = crud.update_post(db, post.id, "Yangilangan Post", "Ali vali dgsdkkds dsdsdsds.")
print(f"\nUpdated Post:{post.title}\n{post.body}")

#test: post o'chirish
crud.delete_post(db, 5)
print("\nPost deleted.")

#test: get_user_posts
posts = crud.get_user_posts(db, 3)
restult = []
for post in posts:
    restult.append({
        "id": post.id,
        "title": post.title,
        "body": post.body
    })
print("\nUser posts:", restult)

#test get_post_comment_count
count = crud.get_post_comment_count(db, 2)
print("\nPost comment count:", count)

#test get_latest_posts
latest_posts = crud.get_latest_posts(db, limit=5)
restult = []
for post in latest_posts:
    restult.append(post.title)
print("\nLatest posts:", restult)

#test search_posts_by_title
search_results = crud.search_posts_by_title(db, "Kitob")
restult = []
for post in search_results:
    restult.append({
        "id": post.id,
        "title": post.title,
        "body": post.body
    })
print("\nSearch results:", restult)

#test paginate_posts
paginated_posts = crud.paginate_posts(db, page=1, per_page=2)
restult = []
for post in paginated_posts:
    restult.append({
        "id": post.id,
        "title": post.title,
        "body": post.body
    })
print("\nPaginated posts:", restult)

