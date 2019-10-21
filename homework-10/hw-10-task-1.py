class Gadget:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def gadget_info(self):
        return f'Gadget: {self.brand} {self.model} ({self.year})'


class Phone(Gadget):
    def __init__(self, brand, model, year, apps: list,
                 contacts, settings: dict):
        super(Phone, self).__init__(brand, model, year)
        self.apps = apps
        self.contacts = []
        self.settings = settings

    def add_app(self, app):
        self.apps.add(app)
        # if app not in self.apps:
        #     self.apps.append(app)
        # else:
        #     return f"{app} already installed"

    def del_app(self, app):
        self.apps.remove(app)

    def add_contacts(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            return self.contacts
        else:
            return f"{contact} already in memory"

    def del_contacts(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            return self.contacts
        else:
            return f"{contact} wasn't found"

    def edit_setting(self, **settings):
        self.settings.update(settings)


class Computer(Gadget):
    def __init__(self, brand, model, year, apps, os):
        super(Computer, self).__init__(brand, model, year)
        self.os = os
        self.apps = apps
        self.trash = []

    def add_app(self, app):
        self.apps.add(app)
#         if app not in self.apps:
#             self.apps.append(app)
#         else:
#             return f"{app} already installed"

    def del_app(self, app):
        self.apps.remove(app)
        self.trash.append(app)
        # if app in self.apps:
        #     self.apps.remove(app)
        #     self.trash.append(app)
        # else:
        #     return f"{app} wasn't found"

    def explorer_trash(self, app):
        return ", ".join(self.trash)
        # if len(self.trash) > 0:
        #     return self.trash
        # else:
        #     return f"Explorer trash is empty"

    def remove_trash(self):
        self.trash.clear()
        print("Trash-box was cleared!")


class TV(Gadget):
    def __init__(self, brand, model, year, channels, settings):
        super(TV, self).__init__(brand, model, year)
        self.channels = channels
        self.settings = settings
        
    def add_channel(self, channel):
        self.channels.append(channel)
        # if channel not in self.channels:
        #     self.channel.append(channel)
        #     return self.channels
        # else:
        #     f"{channel} alredy installed"
    	
    def del_channel(self, channel):
        self.channels.remove(channel)

    def edit_settings(self, **settings):
        self.settings.update(settings)
