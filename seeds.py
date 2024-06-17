from faker import Faker
import random
from Project_7.models import Base, Groups, Teachers, Subjects, Students, Marks
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

data_base = 'sqlite:///database.db'
engine = create_engine(data_base)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

if __name__ == '__main__':
    fake = Faker('uk_UA')
    num_teachers = 5
    num_students = 40
    groups_list = ['МА-95', "МА-96", "МА-97"]
    subjects = ["Лінійна алгебра", "Арифметика", "Геометрія", "Теорія імовірності", "Англійська мова"]

    teachers_names = [fake.name() for _ in range(num_teachers)]
    teachers = [Teachers(fullname=name) for name in teachers_names]
    session.add_all(teachers)

    group_instances = [Groups(group_name=group) for group in groups_list]
    session.add_all(group_instances)

    subject_instances = [Subjects(subject_name=subject) for subject in subjects]
    session.add_all(subject_instances)

    student_instances = []
    for _ in range (num_students):
        student_name = fake.name()
        student_group = random.choice(group_instances)
        student_instances.append(Students(fullname=student_name, group_id = student_group.id))

    marks_instances = []
    for student in student_instances:
        for subject in subject_instances:
            num_marks = random.randint(10, 20)
            for _ in range(num_marks):
                mark = random.randint(60, 100)
                marks_instances.append(Marks(student_id=student.id, subject_id=subject.id, mark=mark))

    session.add_all(marks_instances)

    session.add_all(student_instances)

    session.commit()
