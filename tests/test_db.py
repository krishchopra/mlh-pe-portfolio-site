import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]

# use in-memory SQLite database for tests
test_db = SqliteDatabase(":memory:")

class TestTimelinePost(unittest.TestCase):
  def setUp(self):
    # bind model to test db
    # no need to recursively bind refs/backrefs, all models are included
    test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
    test_db.connect()
    test_db.create_tables(MODELS)
  
  def tearDown(self):
    # not necessary since it's in memory, but good practice
    test_db.drop_tables(MODELS)

    # close db connection
    test_db.close()

  def test_timeline_post(self):
    # create posts
    first_post = TimelinePost.create(name="John Doe", email="john@example.com", content="Hello world, I'm John!")
    assert first_post.id == 1
    second_post = TimelinePost.create(name="Jane Doe", email="jane@example.com", content="Hello world, I'm Jane!")
    assert second_post.id == 2

    # get posts
    posts = TimelinePost.select()
    assert len(posts) == 2

    johns_post = TimelinePost.get(TimelinePost.name == "John Doe")
    assert johns_post.email == "john@example.com"
    assert johns_post.content == "Hello world, I'm John!"

    janes_post = TimelinePost.get(TimelinePost.name == "Jane Doe")
    assert janes_post.email == "jane@example.com"
    assert janes_post.content == "Hello world, I'm Jane!"
