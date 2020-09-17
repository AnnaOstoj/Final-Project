import os
import redis

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
        SECRET_KEY = "12390812903183242"
        SQLALCHEMY_DATABASE_URI = (
                os.environ.get('DATABASE_URL') or
                'sqlite:///' + os.path.join(BASE_DIR, 'blogs.db')
        )
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
        ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin")

        redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
        redis = redis.from_url(redis_url)