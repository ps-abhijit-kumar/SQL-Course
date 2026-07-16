from database import Database
from excel_writer import ExcelWriter
from query_loader import QueryLoader
class AutomationEngine:
    def __init__(self):
        self.loader = QueryLoader()
        self.database = Database()
        self.writer = ExcelWriter()
        self.success = 0
        self.failed = 0
    def run(self):
        print("=" * 60)
        print("SQL EXERCISE AUTOMATION")
        print("=" * 60)
        self.database.connect()
        exercises = self.loader.load_queries()
        try:
            for exercise in exercises:
                self.execute_exercise(exercise)
            output = self.writer.save()
            print("\n" + "=" * 60)
            print("Workbook Created")
            print(output)
        finally:
            self.database.close()
            print("=" * 60)
            print(f"Completed : {self.success}")
            print(f"Failed    : {self.failed}")
            print("=" * 60)
    def execute_exercise(self, exercise):
        print(f"\n[{exercise['sheet']}] {exercise['file'].name}")
        try:
            columns, rows = self.database.execute_script(
                exercise["sql"]
            )
            self.writer.add_sheet(
                exercise["sheet"],
                columns,
                rows
            )
            self.success += 1
            print(f"✓ Exported {len(rows)} rows")
        except Exception as ex:
            self.failed += 1
            print(f"✗ Failed")
            print(ex)