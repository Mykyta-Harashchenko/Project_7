from datetime import datetime, timedelta
from faker import Faker
import random
from Project_7.models import Base, Groups, Teachers, Subjects, Students, Marks
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select

data_base = 'sqlite:///database.db'
engine = create_engine(data_base)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


def generate_teachers(session, num_teachers):
    fake = Faker('uk_UA')
    teachers_names = [fake.name() for _ in range(num_teachers)]
    teachers = [Teachers(fullname=name) for name in teachers_names]
    session.add_all(teachers)
    session.commit()
    return session.scalars(select(Teachers.id)).all()


def generate_groups(session, groups_list):
    group_instances = [Groups(group_name=group) for group in groups_list]
    session.add_all(group_instances)
    session.commit()
    return session.scalars(select(Groups.id)).all()


def generate_subjects(session, subjects, teacher_ids):
    subject_instances = [Subjects(subject_name=subject, teacher_id=random.choice(teacher_ids)) for subject in subjects]
    session.add_all(subject_instances)
    session.commit()
    return subject_instances


def generate_students(session, num_students, group_ids):
    fake = Faker('uk_UA')
    student_instances = []
    for _ in range(num_students):
        student_name = fake.name()
        student_group = random.choice(group_ids)
        student_instances.append(Students(fullname=student_name, group_id=student_group))
    session.add_all(student_instances)
    session.commit()
    return session.scalars(select(Students.id)).all()


def generate_marks(session, students_ids, subject_instances):
    start_date = datetime.strptime('2023-03-01', '%Y-%m-%d')
    end_date = datetime.strptime('2024-06-29', '%Y-%m-%d')
    marks_instances = []

    result = []
    while start_date <= end_date:
        if start_date.isoweekday() < 6:
            result.append(start_date)
        start_date += timedelta(1)

    for student_id in students_ids:
        for subject in subject_instances:
            num_marks = random.randint(10, 20)
            for _ in range(num_marks):
                mark_date = random.choice(result)
                mark = random.randint(60, 100)
                marks_instances.append(
                    Marks(student_id=student_id, subject_id=subject.id, mark=mark, date_of=mark_date))
    session.add_all(marks_instances)



if __name__ == '__main__':
    num_teachers = 5
    num_students = 40
    groups_list = ['МА-95', "МА-96", "МА-97"]
    subjects = ["Лінійна алгебра", "Арифметика", "Геометрія", "Теорія імовірності", "Англійська мова"]

    teacher_ids = generate_teachers(session, num_teachers)
    group_ids = generate_groups(session, groups_list)
    subject_instances = generate_subjects(session, subjects, teacher_ids)
    student_ids = generate_students(session, num_students, group_ids)
    generate_marks(session, student_ids, subject_instances)
    session.commit()

    print("База даних успішно заповнена випадковими даними!")

