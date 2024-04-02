import datetime
import locale


class FrenchDate:
    def __init__(self) -> None:

        array_month_fr = (
            'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
            'Décembre')

        locale.setlocale(locale.LC_TIME, 'fr_FR')
        current_date = datetime.datetime.now()

        today_fr = str(current_date.date().day)
        month_fr = current_date.date().month
        month_fr = array_month_fr[month_fr - 1]
        year_fr = str(current_date.date().year)

        self.format_fr = today_fr + '-' + month_fr + '-' + year_fr
