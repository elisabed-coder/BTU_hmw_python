from mock_data import blogs
from django.http import HttpResponse


def blogs_view(request):
    html = ""
    for blog in blogs.values():
        html += f"""
        <h3>{blog['title']}</h3>
        <p>{blog['author']} on {blog['date_published']}<p>
        <p>{blog['content']}<p>
        <p>Tags: {', '.join(blog['tags'])}</p>
        """
    return HttpResponse(html, status=200)
