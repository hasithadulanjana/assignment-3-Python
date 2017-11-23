from sys import stdout as console


# Interface
class Command:
    def execute(self):
        raise NotImplementedError()

    def help(self):
        raise NotImplementedError()

    def name(self):
        raise NotImplementedError()


# bar command
class Bar(Command):
    def execute(self, arg):
        arg = arg.upper()
        if arg == "GENDER":
            if self.db.get_data(arg):
                self.view.plot_pie_gender(self.db.get_data(arg))
            else:
                print("Couldn't find valid data")
        else:
            print('The valid option for a pie graph is currently only gender')

    def help(self):
        print(self.file_handler.open_help("bar"))

    def name(self):
        return "Excuitng a Bar Chart"


# pie command
class Pie(Command):
    def execute(self, arg):
        arg = arg.upper()
        if arg == "SALARY":
            salary = self.db.get_data("SALARY")
            age = self.db.get_data("AGE")
            self.view.age_salary(age, salary)
        elif arg == "SALES":
            sales = self.db.get_data("SALES")
            age = self.db.get_data("AGE")
            self.view.pygal_line_salebased(sales, age)
        else:
            print('The valid options for a scatter graph are salary or sales')

    def help(self):
        print(self.file_handler.open_help('pie'))

    def name(self):
        return "Excuitng a Pie Chart"


# line command
class Line(Command):
    def execute(self):
        sales = self.db.get_data("SALES")
        ages = self.db.get_data("AGE")
        self.view.pygal_line_salebased(sales, ages)

    def help(self):
        print(self.file_handler.open_help('line'))

    def name(self):
        return "Excuitng a Line"


        # linegrapgh  command


class LineGrapgh(Command):
    def execute(self):
        ages = self.db.get_data("AGE")
        # print(sales)
        salarys = self.db.get_data("SALARY")
        self.view.age_salary(ages, salarys)

    def help(self):
        print(self.file_handler.open_help('linegraph'))

    def name(self):
        return "Excuitng a Line graph"


# redo command
class DoScatter(Command):
    def execute(self, arg):
        arg = arg.upper()
        if arg == "SALARY":
            salary = self.db.get_data("SALARY")
            age = self.db.get_data("AGE")
            self.view.age_salary(age, salary)
        elif arg == "SALES":
            sales = self.db.get_data("SALES")
            age = self.db.get_data("AGE")
            self.view.pygal_line_salebased(sales, age)
        else:
            print('The valid options for a scatter graph are salary or sales')

    def help(self):
        print(self.file_handler.open_help('scatter'))

    def name(self):
        return "Excuitng a scatter graph"


def main():
    def __init__(self, new_file_handler, new_db, new_view):
        self.__init__(self)
        self.prompt = "> "
        self.file_handler = new_file_handler
        self.db = new_db
        self.view = new_view
        self.db.attach(self.view)


if __name__ == "__main__":
    main()