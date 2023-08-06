import pytest


def test_create_post(client, user):
    response = client.post(
        "/api/posts",
        json={"title": "Test Post", "content": "This is a test blog post."},
        headers={"Authorization": f"Bearer {user.generate_auth_token()}"},
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Blog post created successfully"
    assert "data" in data


def test_get_all_posts(client, user):
    response = client.get(
        "/api/posts", headers={"Authorization": f"Bearer {user.generate_auth_token()}"}
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "data" in data
    assert isinstance(data["data"], list)


def test_get_post_details(client, user, test_post):
    response = client.get(
        f"/api/posts/{test_post.id}",
        headers={"Authorization": f"Bearer {user.generate_auth_token()}"},
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "data" in data
    assert data["data"]["title"] == test_post.title
    assert data["data"]["content"] == test_post.content


def test_create_comment(client, user, test_post):
    response = client.post(
        f"/api/posts/{test_post.id}/comments",
        json={"content": "This is a test comment."},
        headers={"Authorization": f"Bearer {user.generate_auth_token()}"},
    )
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Added comment to blog post with ID 1"
    assert "data" in data


def test_get_all_comments_for_post(client, user, test_post):
    response = client.get(
        f"/api/posts/{test_post.id}/comments",
        headers={"Authorization": f"Bearer {user.generate_auth_token()}"},
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "data" in data
    assert isinstance(data["data"], list)


def test_comments_associated_with_correct_post(client, user):
    response = client.get(
        "/api/posts/99999/comments",
        headers={"Authorization": f"Bearer {user.generate_auth_token()}"},
    )  # Non-existent post ID
    data = response.get_json()
    assert response.status_code == 404
    assert "message" in data


def test_comments_count_for_post(client, user, test_post, create_comment):
    # Creating comments for the test_post using the create_comment fixture
    create_comment("Comment 1", test_post.author_id, test_post.id)
    create_comment("Comment 2", test_post.author_id, test_post.id)
    create_comment("Comment 3", test_post.author_id, test_post.id)

    # Fetch the comments associated with the test_post
    response = client.get(
        f"/api/posts/{test_post.id}/comments",
        headers={"Authorization": f"Bearer {user.generate_auth_token()}"},
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "data" in data
    assert len(data["data"]) == 3  # Check the count of comments for the blog post
