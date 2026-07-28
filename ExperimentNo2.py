def bold_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"** {result} **"
    return wrapper

class Report:
    _templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template_func):
        cls._templates[name] = template_func

    @classmethod
    def get_template(cls, name):
        return cls._templates.get(name)

    def __call__(self, template_name):
        template_func = self.get_template(template_name)
        if template_func:
            return template_func(self)
        return f"[Error] Template '{template_name}' not found."

    def __str__(self):
        return f"Report Object -> Title: '{self.title}', Content Length: {len(self.content)} characters"

def simple_template(report):
    return f"Title: {report.title}\nBody: {report.content}"

@bold_text
def fancy_template(report):
    return f"FANCY REPORT | TITLE: {report.title.upper()} | CONTENT: {report.content}"

def main():
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    monthly_report = Report("Annual Tech Summary", "AI adoption has increased significantly across all departments.")

    print("--- Default String Representation (__str__) ---")
    print(monthly_report)
    print()

    print("--- Simple Template Output ---")
    print(monthly_report("simple"))
    print()

    print("--- Fancy Template Output (Decorated) ---")
    print(monthly_report("fancy"))
    print()
    
    print("--- Missing Template Output ---")
    print(monthly_report("executive_summary"))

if __name__ == "__main__":
    main()
