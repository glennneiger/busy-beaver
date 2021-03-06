import pytest

from busy_beaver.apps.github_integration.webhook.workflow import (
    generate_new_issue_message,
    generate_new_pull_request_message,
    generate_new_release_message,
)

pytest_plugins = ("tests._utilities.fixtures.github",)


@pytest.mark.unit
def test_generate_new_issue_message_action_is_open(generate_event_subscription_request):
    data = generate_event_subscription_request(action="opened", issue_html_url="url")

    result = generate_new_issue_message(data)

    assert "New Issue" in result
    assert "url" in result


@pytest.mark.unit
def test_generate_new_issue_message_action_is_not_open(
    generate_event_subscription_request,
):
    data = generate_event_subscription_request(action="something_else")
    result = generate_new_issue_message(data)
    assert not result


@pytest.mark.unit
def test_generate_new_pr_message_action_is_open(generate_event_subscription_request):
    data = generate_event_subscription_request(action="opened", pr_html_url="url")

    result = generate_new_pull_request_message(data)

    assert "New Pull Request" in result
    assert "url" in result


@pytest.mark.unit
def test_generate_new_pr_message_action_is_not_open(
    generate_event_subscription_request,
):
    data = generate_event_subscription_request(action="something_else")
    result = generate_new_pull_request_message(data)
    assert not result


@pytest.mark.unit
def test_post_message_when_release_action_is_published(
    generate_event_subscription_request,
):
    data = generate_event_subscription_request(
        action="published", release_html_url="url"
    )

    result = generate_new_release_message(data)

    assert "New Release" in result
    assert "url" in result


@pytest.mark.unit
def test_do_not_post_message_when_release_action_is_not_published(
    generate_event_subscription_request,
):
    data = generate_event_subscription_request(action="something_else")
    result = generate_new_release_message(data)
    assert not result
