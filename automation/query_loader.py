from pathlib import Path
import re


class QueryLoader:
    def __init__(self):
        self.exercise_folder = Path(__file__).parent.parent / "Exercises"

    def load_queries(self):
        exercises = []

        sql_files = sorted(
            self.exercise_folder.glob("Exercise-*.sql"),
            key=self._exercise_number
        )

        for sql_file in sql_files:
            exercise_number = self._exercise_number(sql_file)

            exercises.append({
                "number": exercise_number,
                "sheet": f"Q{exercise_number}",
                "file": sql_file,
                "sql": sql_file.read_text(encoding="utf-8")
            })

        return exercises

    @staticmethod
    def _exercise_number(path):
        match = re.search(r"Exercise-(\d+)", path.name)
        return int(match.group(1))