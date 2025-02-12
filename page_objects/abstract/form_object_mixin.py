from abc import ABC, abstractmethod


class FormObjectMixin(ABC):

    @property
    @abstractmethod
    def submit_button(self):
        raise NotImplementedError("Implement submit button")

    def populate_form(self, data):
        for k, v in data.items():
            element = getattr(self, k)
            element.value = v

    def submit_form(self, data=None):
        data = data or dict()
        self.populate_form(data)
        self.submit_button.click()
