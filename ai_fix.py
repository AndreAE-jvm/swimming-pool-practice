def parse_csv(filename):
    result = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        headers = f.readline().strip().split(",")
        for line in f:
            line = line.strip()
            if not line:
                continue
            values = line.split(",")
            result.append(dict(zip(headers, values)))
    return result

print(parse_csv("students.csv"))