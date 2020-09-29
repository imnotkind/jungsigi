from student import student


def main():
    # fill out the main function
    # 1. Read the Input File
    # 2. Make the student instance for each student
    # 3. Print name, score, grade with using __repr__
    # 4. Write the outpuf File

    input_file = open("student_scores.txt", "r")
    output_file = open("grading_result.txt", "w")

    for line in input_file.readlines():
        s = student(*line.rstrip().split(","))
        print(s)
        output_file.write(
            "{},{:.2f},{}\n".format(
                s.name, s.calculate_total_score(), s.get_total_grade()
            )
        )

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()
