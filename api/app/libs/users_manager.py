from flask import current_app, g
from datetime import datetime, timedelta
from app.models.Users import Users
from app.models.Posts import Posts,Comments
from app.models.Todos import Todos
from app.libs.singleton import Singleton
from app.libs.jsonplaceholder_connector import Jsonplaceholder_connector
import requests


class UsersManager(object,metaclass=Singleton):
    """docstring for UsersManager"""
    def __init__(self):
        super().__init__()

    # TODO: possibly dependence injection on source without actual implementation here
    @staticmethod
    def sync_users_from_source():
        jsp = Jsonplaceholder_connector()
        users_source = jsp.get_users()
        todos_source = jsp.get_todos()
        posts_source = jsp.get_posts()
        comments_source = jsp.get_comments()
        # all or nothing for data integrity 
        if users_source is None or todos_source is None or posts_source is None or comments_source is None: 
            raise Exception("Source api is not accessible")
        posts_dict = { ps["id"]:Posts(post_id=ps["id"],body=ps["body"]) for ps in posts_source}
        users_dict = { us["id"]:Users(user_id=us["id"],name=us["name"],username=us["username"],email=us["email"],address=us["address"],phone=us["phone"],company=us["company"],website=us["website"]) for us in users_source}
        for comment in comments_source:
            # skip unrecognized posts
            if comment["postId"] not in posts_dict:
                continue
            postDoc = posts_dict[comment["postId"]]
            postDoc.comments.append(Comments(comment_id=comment["id"],name=comment["name"],email=comment["email"],body=comment["body"]))
        for post in posts_source:
            # skip unrecognized users
            if post["userId"] not in users_dict:
                continue
            postDoc = posts_dict[post["id"]]
            userDoc = users_dict[post["userId"]]
            userDoc.posts.append(postDoc)
        for todo in todos_source:
            # skip unrecognized users
            if todo["userId"] not in users_dict:
                continue
            userDoc = users_dict[post["userId"]]
            userDoc.todos.append(Todos(todo_id=todo["id"],title=todo["title"],completed=todo["completed"]))
        for _,userDoc in users_dict.items():
            userDoc.save()
        return


    def get_users_list(self,user_id=[]):
        users = []
        for u in Users.objects:
            users.append({
                "id": u.user_id,
                "name": u.name,
                "username": u.username,
                "email": u.email,
                "address": u.address,
                "phone": u.phone,
                "website": u.website,
                "company": u.company,
            })
        return users

    def get_user(self,user_id):
        try:
            u = Users.objects.get(pk=user_id)
        except Users.DoesNotExist as e:
            return None
        return {
                "id": u.user_id,
                "name": u.name,
                "username": u.username,
                "email": u.email,
                "address": u.address,
                "phone": u.phone,
                "website": u.website,
                "company": u.company,
                "posts":u.posts,
                "todos":u.todos
        }