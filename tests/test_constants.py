"""Tests for the updated constants in utils/constants.py."""

from utils.constants import info, projects, youtube_playlists


def test_info_about_updated():
    """Verify info['About'] contains '13+ years' (not '11+ years')."""
    assert "13+ years" in info["About"]
    assert "11+ years" not in info["About"]


def test_info_intro_updated():
    """Verify info['Intro'] contains 'AI Engineer'."""
    assert "AI Engineer" in info["Intro"]


def test_info_intro_does_not_contain_old():
    """Verify info['Intro'] no longer contains the old title."""
    assert "Data Analytics Professional" not in info["Intro"]


def test_projects_list_structure():
    """Verify projects list has the expected structure."""
    assert len(projects) > 0
    for project in projects:
        assert "title" in project
        assert "description" in project
        assert "image_url" in project
        assert "link" in project


def test_projects_count():
    """Verify the expected number of projects."""
    assert len(projects) == 6


def test_youtube_playlists_structure():
    """Verify youtube_playlists list has the expected structure."""
    assert len(youtube_playlists) > 0
    for playlist in youtube_playlists:
        assert "title" in playlist
        assert "url" in playlist
        assert "image_url" in playlist
        assert "description" in playlist


def test_youtube_playlists_count():
    """Verify the expected number of playlists."""
    assert len(youtube_playlists) == 3
