#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: SullenLook sullenlook@sullenlook.eu
#project: SiriServer plugin


from plugin import *
import urllib
from BeautifulSoup import BeautifulSoup
from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine

class fbgrbild(Plugin):

        res = {
                'fbgrbild': {
                        'de-DE': '.*Unsere.*Facebookgruppe.*|.*Unsere .*Facebook .*Gruppe.*',
                }
        }

        @register("de-DE", res['fbgrbild']['de-DE'])
        def fbgrbild(self, speech, language):
                html = urllib.urlopen("http://siri.sullenlook.eu/fbanner.png/")
                soup = BeautifulSoup(html)
                ImageURL = "http://siri.sullenlook.eu/fbanner.png/"
                view = AddViews(self.refId, dialogPhase="Completion")
                ImageAnswer = AnswerObject(title=str("Unsere Facbook Gruppe"),lines=[AnswerObjectLine(image="http://sullenlook.eu/Pix/cydia/info/testbild.png")])
                view1 = AnswerSnippet(answers=[ImageAnswer])
                view.views = [view1]
                self.sendRequestWithoutAnswer(view)
