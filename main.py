#!/usr/bin/env python
import webapp2
from google.appengine.api import app_identity
from google.appengine.api import mail
from conference import ConferenceApi

class SetAnnouncementHandler(webapp2.RequestHandler):
    def get(self):
        """Set Announcement in Memcache."""
        ConferenceApi._cacheAnnouncement()
        self.response.set_status(204)


class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

class SendConfirmationEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Conference!',            # subj
            'Hi, you have created a following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

class SendConfirmationOfSessionEmailHandler(webapp2.RequestHandler):
    def post(self):
        """Send email confirming Conference creation."""
        mail.send_mail(
            'noreply@%s.appspotmail.com' % (
                app_identity.get_application_id()),     # from
            self.request.get('email'),                  # to
            'You created a new Session!',            # subj
            'Hi, you have created a new Session in the following '         # body
            'conference:\r\n\r\n%s' % self.request.get(
                'conferenceInfo')
        )

class CheckFeaturedSpeakerHandler(webapp2.RequestHandler):
    def post(self):
        """Check FeaturedSpeaker and Set FeaturedSpeaker in Memcache."""
        # update speaker and add session to speaker
        ConferenceApi._updateSpeaker(self.request)
        # cache featured speaker
        speaker = ndb.Key(urlsafe = self.request.get("speakerKey")).get()
        if  len(speaker.sessionKeys) > 1:
            featuredSpeaker = {"name" : speaker.name, "speakerKey":  speaker.key()}
            memcache.set(MEMCACHE_FEATUREDSPEAKER_KEY, featuredSpeaker)
        self.response.set_status(204)

app = webapp2.WSGIApplication([
    ('/crons/set_announcement', SetAnnouncementHandler),
    ('/tasks/send_confirmation_email', SendConfirmationEmailHandler),
    ('/tasks/send_confirmation_session_email', SendConfirmationOfSessionEmailHandler),
    ('/tasks/check_featured_speaker', CheckFeaturedSpeakerHandler),
], debug=True)
