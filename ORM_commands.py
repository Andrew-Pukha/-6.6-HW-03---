# '''список всех команд, запускаемых в Django shell'''
#
# '''
# 1)  python manage.py shell
#
# 2)  from django.contrib.auth.models import User
#     from your_app.models import Author, Category, Post, Comment
#
# 3)  user1 = User.objects.create_user('user1', password='password123')
#     user2 = User.objects.create_user('user2', password='password456')
#
# 4)  author1 = Author.objects.create(user=user1)
#     author2 = Author.objects.create(user=user2)
#
# 5)  category1 = Category.objects.create(name='Sport')
#     category2 = Category.objects.create(name='Politics')
#     category3 = Category.objects.create(name='Education')
#     category4 = Category.objects.create(name='Technology')
#
# 6)  post1 = Post.objects.create(author=author1, type='AR', title='Article 1', content='Content of article 1...')
#     post2 = Post.objects.create(author=author2, type='AR', title='Article 2', content='Content of article 2...')
#     news1 = Post.objects.create(author=author1, type='NW', title='News 1', content='Content of news 1...')
#
# 7)  post1.categories.add(category1, category2)  # 2 категории
#     post2.categories.add(category3)  # 1 категория
#     news1.categories.add(category4)  # 1 категория
#
# 8)  comment1 = Comment.objects.create(post=post1, user=user2, content='Comment on article 1')
#     comment2 = Comment.objects.create(post=post2, user=user1, content='Comment on article 2')
#     comment3 = Comment.objects.create(post=news1, user=user2, content='Comment on news 1')
#     comment4 = Comment.objects.create(post=post1, user=user1, content='Another comment on article 1')
#
# 9)  post1.like()
#     post1.like()
#     post2.like()
#     post2.dislike()
#     news1.like()
#
#     comment1.like()
#     comment2.like()
#     comment2.dislike()
#     comment3.like()
#     comment4.dislike()
#
# 10) author1.update_rating()
#     author2.update_rating()
#
# 11) best_author = Author.objects.order_by('-rating').first()
#     print(f"Лучший пользователь: {best_author.user.username}, Рейтинг: {best_author.rating}")
#
# 12) best_post = Post.objects.order_by('-rating').first()
#     print(f"Дата добавления: {best_post.created_at}")
#     print(f"Автор: {best_post.author.user.username}")
#     print(f"Рейтинг: {best_post.rating}")
#     print(f"Заголовок: {best_post.title}")
#     print(f"Предварительный просмотр: {best_post.preview()}")
#
# 13) comments = Comment.objects.filter(post=best_post)
#     for comment in comments:
#         print(f"Дата: {comment.created_at}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.content}")