
class CleanUpString:
    def __init__(self) -> None:
        self.new_string: str = ""

    def cleanup_folder_name(self, value: str | None = None) -> None:

        folder_name_format = ['/', '\\', '|', '*', '"', '?',  '<', '>']

        for oc in folder_name_format:
            value = value.replace(oc, '')

        index = value.find('(')
        if index:
            value = value[:index]

        value = value.replace(' ', '-')
        value.strip()

        self.new_string = str(value)

    def cleanup_link(self, new_path):
        for x in new_path:
            if x != '.' and x != '/':
                nbr_key = new_path.find(x)
                index = new_path.find(new_path[nbr_key])
                new_path = new_path[index:]
                break
        return new_path
