from selenium_datatable import DataTable


class CategoryPageFilter(DataTable):

    def get_option_by_name(self, name):
        """
        The reason this is done this way is due to unlucky text coupling on the page, like so:
		<a href='...'>Tops<span> (2)</span></a>
		Due to the <span> node with text being inside the <a> node,
		reading the text attribute of WebElement corresponding to <a> node results in 'Tops (2)'.
		Thus, it needs to be decoupled 'manually'.
        """
        for item in self:
            option = item.name.text.split(" (")[0]
            if name == option:
                return item

    @staticmethod
    def get_amount(amount: str):
        """(5) -> 5"""
        return int(amount.strip("()"))
