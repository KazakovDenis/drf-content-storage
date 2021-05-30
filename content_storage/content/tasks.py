from content.models import Page
from core import app


@app.task
def increment_content_counters(page_id: int):
    """Background task to increment counters of some page contents"""
    page = Page.objects.get(id=page_id)
    page.increment_counters()
