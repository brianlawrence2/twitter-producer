import os

TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY")

for env in os.environ:
    print(env)