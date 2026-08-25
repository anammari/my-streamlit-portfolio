"""Tests for the updated bio.txt content."""


def _read_bio():
    with open("data/bio.txt", "r", encoding="utf-8") as f:
        return f.read()


def test_bio_contains_future_secure_ai():
    """Verify bio.txt mentions Future Secure AI."""
    content = _read_bio()
    assert "Future Secure AI" in content


def test_bio_contains_university_of_new_england():
    """Verify bio.txt mentions University of New England."""
    content = _read_bio()
    assert "University of New England" in content


def test_bio_contains_temporalio():
    """Verify bio.txt mentions Temporal.io."""
    content = _read_bio()
    assert "Temporal.io" in content


def test_bio_contains_claude_code():
    """Verify bio.txt mentions Claude Code."""
    content = _read_bio()
    assert "Claude Code" in content


def test_bio_contains_mcp():
    """Verify bio.txt mentions MCP."""
    content = _read_bio()
    assert "MCP" in content


def test_bio_contains_agentic_ai():
    """Verify bio.txt mentions agentic AI."""
    content = _read_bio()
    assert "agentic" in content.lower()


def test_bio_contains_13_years():
    """Verify bio.txt mentions 13+ years of experience."""
    content = _read_bio()
    assert "13+" in content


def test_bio_does_not_contain_old_years():
    """Verify bio.txt no longer mentions 11 or 12 years."""
    content = _read_bio()
    assert "11+" not in content


def test_bio_contains_one_week_availability():
    """Verify bio.txt states availability within one week of an offer."""
    content = _read_bio()
    assert "within one week" in content


def test_bio_does_not_contain_four_weeks_availability():
    """Verify bio.txt no longer states the old four-week availability."""
    content = _read_bio()
    assert "within four weeks" not in content
