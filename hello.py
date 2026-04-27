import re
import uuid


MONTHS = {
	"january": "01",
	"february": "02",
	"march": "03",
	"april": "04",
	"may": "05",
	"june": "06",
	"july": "07",
	"august": "08",
	"september": "09",
	"october": "10",
	"november": "11",
	"december": "12",
}


def generate_student_id(name: str, birth_month: str) -> str:
	"""Generate a unique student ID from a name and birth month."""
	clean_name = re.sub(r"[^A-Za-z]", "", name).upper()
	initials = (clean_name[:3] or "STU").ljust(3, "X")

	month = birth_month.strip().lower()
	month_code = MONTHS.get(month)
	if month_code is None:
		if birth_month.isdigit() and 1 <= int(birth_month) <= 12:
			month_code = f"{int(birth_month):02d}"
		else:
			raise ValueError("Birth month must be a month name or a number from 1 to 12.")

	unique_part = uuid.uuid4().hex[:6].upper()
	return f"{initials}-{month_code}-{unique_part}"


if __name__ == "__main__":
	student_name = input("Enter student name: ").strip()
	student_month = input("Enter birth month: ").strip()
	print(generate_student_id(student_name, student_month))
