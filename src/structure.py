class List:
    def __init__(self, date, name):
        self.name = name
        self.date = date
        self.items_in_list = []

    def print_list(self):
        return self.name + " - " + self.date

    def print_content(self):
        if len(self.items_in_list) > 0:
            print(f"Showing {self.name}\' content:")
            for item in self.items_in_list:
                print("* " + item + "")
        else: 
            print(f"The specified list \"{self.name}\" does not contain any items.")

    def add_item(self, item):
        self.items_in_list.append(item)

