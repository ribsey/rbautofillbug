# rbautofillbug Extension for Review Board.

from __future__ import unicode_literals

import logging
import re
import itertools

from django.db.models.signals import post_delete, pre_save
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import SignalHook
from reviewboard.reviews.models import ReviewRequestDraft


class AutoFillBugExtension(Extension):
    metadata = {
        'Name': 'Auto Fill Bugs',
        'Summary': 'Extracts bug IDs from the review request summary to fill '
                   'the "Bugs" field automatically.',
    }
    is_configurable = True
    default_settings = {
        'bug_format': "#(\d+)",
    }

    def initialize(self):
        self.already_parsed_drafts = set()
        SignalHook(self, pre_save, self.on_pre_save)
        SignalHook(self, post_delete, self.on_post_delete)

    def on_pre_save(self, sender, instance, **kwargs):
        if sender is ReviewRequestDraft:
            review_request_draft = instance
            logging.debug("pre save for request draft %s",
                          review_request_draft.id)
            if self.need_to_update_bugs_closed(review_request_draft.id):
                summary = review_request_draft.summary
                description = review_request_draft.description
                bug_regex = self.settings['bug_format']
                bugs = find_bugs(bug_regex, summary)
                bugs = bugs + find_bugs(bug_regex, description)
                review_request_draft.bugs_closed = ', '.join(bugs)
                review_request = review_request_draft.review_request
                logging.info(
                    "Found bugs %s in summary of review request %s",
                    bugs, review_request.get_display_id())
                self.already_parsed_drafts.add(review_request_draft.id)
                logging.debug("Marking review request draft %s as parsed",
                              review_request_draft.id)

    def on_post_delete(self, sender, instance, using, **kwargs):
        if sender is ReviewRequestDraft:
            review_request_draft = instance
            logging.debug("Removing review request draft %s from parsed drafts",
                          review_request_draft.id)
            self.already_parsed_drafts.discard(review_request_draft.id)

    def need_to_update_bugs_closed(self, review_request_draft_id):
        try:
            review_request_draft = ReviewRequestDraft.objects.get(
                id=review_request_draft_id)
            return (review_request_draft.review_request and
                    not review_request_draft.review_request.public and
                    review_request_draft_id not in self.already_parsed_drafts and
                    review_request_draft.summary)
        except ReviewRequestDraft.DoesNotExist:
            logging.info(
                "AutoFillBugExtension - ReviewRequestDraft with id %s does not exist", review_request_draft_id)
            return True


def find_bugs(bug_regex, summary):
    bug_regex = re.compile(bug_regex)
    bugs = bug_regex.findall(summary)
    # Flatten list if there are multiple groups to match
    if bug_regex.groups > 1:
        bugs = list(itertools.chain.from_iterable(bugs))
    # Remove empty matches
    return list(filter(None, bugs))
