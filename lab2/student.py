class student(object):
    def __init__(
        self,
        name,
        participation_score,
        labassignment_score,
        homework_score,
        midterm_score,
        finalterm_score,
    ):
        # fill out the constructor
        self.name = name
        self.participation_score = float(participation_score)
        self.labassignment_score = float(labassignment_score)
        self.homework_score = float(homework_score)
        self.midterm_score = float(midterm_score)
        self.finalterm_score = float(finalterm_score)

    def __repr__(self):
        # fill out here
        return "Total score of {} is {:.2f} and grade is {}".format(
            self.name, self.calculate_total_score(), self.get_total_grade()
        )

    def calculate_total_score(self):
        # fill out here
        # Percentage for total score is Participation 10%, Lab Assignment 30%, Homework 30%, Mid Term Exam 15 %, Final Exam 15%
        return (
            0.1 * self.participation_score
            + 0.3 * self.labassignment_score
            + 0.3 * self.homework_score
            + 0.15 * self.midterm_score
            + 0.15 * self.finalterm_score
        )

    def get_total_grade(self):
        # fill out here
        # if total_grade x is in
        # 90<= x <=100, grade is A
        # 70 <= x <90, grade is B
        # 50 <= x <70, grade is C
        # x < 50, grade is F
        total_score = self.calculate_total_score()
        if 90 <= total_score and total_score <= 100:
            return "A"
        elif 70 <= total_score and total_score < 90:
            return "B"
        elif 50 <= total_score and total_score < 70:
            return "C"
        elif total_score < 50:
            return "F"
