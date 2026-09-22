#he ajj pasun me parat start karat ahe
# tyamule me hyala suddha mummy chi madat ghetli ahe
def convert_date():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_input = input("Enter a date (MM/DD/YYYY or Month Day, YYYY): ").strip()

        if "/" in date_input:
            try:
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    return f"{year:04d}-{month:02d}-{day:02d}"
                else:
                    continue
            except ValueError:
                continue

        elif "," in date_input:
            try:
                date_input = date_input.replace(",", "")
                parts = date_input.split()
                if len(parts) == 3:
                    month_str, day_str, year_str = parts
                    month = months.index(month_str.capitalize()) + 1
                    day = int(day_str)
                    year = int(year_str)

                    if 1 <= month <= 12 and 1 <= day <= 31:
                        return f"{year:04d}-{month:02d}-{day:02d}"
                    else:
                        continue
                else:
                    continue
            except (ValueError, IndexError):
                continue
        else:
            continue

if __name__ == "__main__":
    print(convert_date())