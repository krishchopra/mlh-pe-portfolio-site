import unittest
import os
import re

# set testing environment
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()
  
  """
  Tests the home page:
  1. Checks the title in the HTML response
  2. Checks the active navbar item is "Home"
  3. Checks the about section is present
  """
  def test_home(self):
    response = self.client.get('/')
    assert response.status_code == 200
    
    # test the right title is rendered
    html = response.get_data(as_text=True)
    assert re.search(r'<title>(?!<\/title>)*[\w\s|]*Krish Chopra<\/title>', html)

    # test the home navbar item is active
    assert re.search(r'<a[^>]*\sclass="nav-link active"[^>]*>(?!<\/a>)[\w\s<!->]*Home[\s]*<\/a>', html)

    # test the about content is present
    assert re.search(r'about me', html, re.IGNORECASE)

  """
  Tests the timeline API endpoint:
  1. Checks the GET request, assert 200 response and 0 posts initially.
  2. Test POST request to create a new timeline post.
  3. Check that the timeline post is created and returned in the next GET response.
  """
  def test_timeline(self):
    # check initial GET request
    response = self.client.get('/api/timeline_post')
    assert response.status_code == 200
    assert response.is_json

    json = response.get_json()
    assert "timeline_posts" in json
    assert len(json["timeline_posts"]) == 0

    # create a new timeline post
    response = self.client.post('/api/timeline_post', data={
      "name": "John Doe",
      "email": "john@example.com",
      "content": "Hello world, I'm John!"
    })
    assert response.is_json

    # check the response from POST request
    json = response.get_json()
    assert json["name"] == "John Doe"
    assert json["email"] == "john@example.com"
    assert json["content"] == "Hello world, I'm John!"
    
    # check GET request again to see the new post
    response = self.client.get('/api/timeline_post')
    assert response.status_code == 200
    assert response.is_json

    json = response.get_json()
    assert "timeline_posts" in json
    assert len(json["timeline_posts"]) == 1

    # note: cannot test HTML results without executing Node.js code
    # as timeline posts are rendered on the client

  def test_malformed_timeline_post(self):
    # POST missing name
    response = self.client.post('/api/timeline_post', data={
      "email": "john@example.com",
      "content": "Hello world, I'm John!"
    })
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid name" in html

    # POST missing content
    response = self.client.post('/api/timeline_post', data={
      "name": "John Doe",
      "email": "john@example.com"
    })
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid content" in html

    # POST missing email
    response = self.client.post('/api/timeline_post', data={
      "name": "John Doe",
      "content": "Hello world, I'm John!"
    })
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid email" in html
