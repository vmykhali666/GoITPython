def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        salaries = [int(line.split(',')[1]) for line in lines]
        total = sum(salaries)
        average = total / len(salaries) if salaries else 0
        return total, average
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0

total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")