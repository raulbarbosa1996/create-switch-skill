from mycroft import MycroftSkill, intent_file_handler


class CreateSwitch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('switch.create.intent')
    def handle_switch_create(self, message):
        self.speak_dialog('switch.create')


def create_skill():
    return CreateSwitch()

