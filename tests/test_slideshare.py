"""Tests for the SlideShare curated data in constants.py."""

from utils.constants import slides


def test_slides_list_structure():
    """Verify each slide entry has the required fields."""
    assert len(slides) > 0
    for slide in slides:
        assert "title" in slide
        assert "url" in slide
        assert "thumbnail" in slide
        assert "slides" in slide
        assert "views" in slide


def test_slides_urls_valid():
    """Verify all slide URLs point to slideshare.net."""
    for slide in slides:
        assert "slideshare.net" in slide["url"]


def test_slides_thumbnail_urls_valid():
    """Verify all thumbnail URLs point to image.slidesharecdn.com."""
    for slide in slides:
        assert "image.slidesharecdn.com" in slide["thumbnail"]


def test_slides_count():
    """Verify the expected number of curated slides."""
    assert len(slides) == 7
