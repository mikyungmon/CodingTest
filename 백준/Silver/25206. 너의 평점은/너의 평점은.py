subject_info = []
score_cal = 0
total_class_n = 0
grade_points = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

for _ in range(20):
    subject_name, class_n, score = input().split()
    class_n = float(class_n)  # 학점은 실수로 변환
    subject_info.append((subject_name, class_n, score))

for s in subject_info:
    if s[2] != 'P':
        score_cal += s[1] * grade_points[s[2]]
        total_class_n += s[1]


avg_score = round(score_cal / total_class_n,7)
print(avg_score)