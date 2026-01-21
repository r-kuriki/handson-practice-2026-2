# ...existing code...
import csv
import re
import sys

_email_re = re.compile(r'^[^@]+@[^@]+\.[^@]+$')

def validate_email(email: str) -> bool:
    return bool(_email_re.match(email or ""))

def main(path: str = "employees.csv") -> None:
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.reader(f)
            email_idx = None
            for lineno, row in enumerate(reader, start=1):
                if lineno == 1:
                    try:
                        email_idx = row.index("email")
                    except ValueError:
                        print("header does not contain 'email'", file=sys.stderr)
                        return
                    continue
                if not row:
                    continue
                email = row[email_idx] if email_idx is not None and len(row) > email_idx else ""
                if not validate_email(email):
                    print(f"Line {lineno}: {','.join(row)}", file=sys.stderr)
    except FileNotFoundError:
        print(f"File not found: {path}", file=sys.stderr)

if __name__ == "__main__":
    main()
# ...existing code...