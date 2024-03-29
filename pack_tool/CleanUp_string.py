
class CleanUpString:
    def __init__(self) -> None:
        self.new_string: str = ""

    def cleaner_folder_name(self, value):

        folder_name_format = ['/', '\\', '|', '*', '"', '?', '<', '>']

        for oc in folder_name_format:
            if oc == '/':
                value = value.replace(oc, '-')
            else:
                value = value.replace(oc, '')

        bracket_before = value.find('(')
        bracket_after = value.find(')')
        if bracket_before != -1:
            text_before = value[:bracket_before]
            if bracket_after != -1:
                text_after = value[bracket_after + 1:]
                value = text_before + text_after

        count_text = len(value)

        db_point = value.find(': ')
        if db_point != -1:
            db_before = value[:db_point]
            db_after = value[db_point + 2:]

            if len(db_before) > 30:
                value = db_before.strip().replace(' ', '_')
            else:
                if len(db_after) > 20:
                    for x in reversed(range(2, 5)):
                        ct_word = db_after.split()[:x]
                        ct_word = " ".join(ct_word)
                        if len(ct_word) < 21 or x == 2:
                            db_after = ct_word + '.etc'
                            break

                db_before = db_before.strip().replace(' ', '_')
                db_after = db_after.strip().replace(' ', '-')
                value = db_before + '_=_' + db_after

        elif count_text > 53:
            for x in reversed(range(2, 5)):
                count_word = value.split()[:x]
                count_word = " ".join(count_word)
                if len(count_word) < 53 or x == 2:
                    value = count_word.strip().replace(' ', '_') + '.etc'
                    break
        else:
            value = value.strip().replace(' ', '_')

        return value

    def cleanup_link(self, new_path):
        for x in new_path:
            if x != '.' and x != '/':
                nbr_key = new_path.find(x)
                index = new_path.find(new_path[nbr_key])
                new_path = new_path[index:]
                break
        return new_path
