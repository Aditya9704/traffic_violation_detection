def check_violation(cars, stop_line_y=300):
    violations = []
    for (x, y, w, h) in cars:
        if y + h > stop_line_y:
            violations.append((x, y, w, h))
    return violations
