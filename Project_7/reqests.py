from models import Subjects, Students, Teachers, Marks, Groups
from sqlalchemy import select, func, desc
from seeds import session

def select_1():
    request_1 = session.query(Students.fullname, func.round(func.avg(Marks.mark), 2).label('avg_grade')).select_from(
        Marks).join(Students).group_by(Students.id).order_by(desc('avg_grade')).limit(5).all()
    return request_1

def select_2(subject_name):
    request_2 = session.query(
        Students.fullname,
        func.round(func.avg(Marks.mark), 2).label('avg_grade')
    ).join(Marks).join(Subjects).filter(
        Subjects.subject_name == subject_name
    ).group_by(Students.id).order_by(
        desc('avg_grade')
    ).first()
    return request_2

def select_3(subject_name):
    request3 = session.query(
        func.round(func.avg(Marks.mark), 2).label('avg_grade'),
        Groups.group_name
    ).join(Students, Students.group_id == Groups.id).join(Marks, Marks.student_id == Students.id).join(Subjects, Marks.subject_id == Subjects.id).filter(
        Subjects.subject_name == subject_name
    ).group_by(Groups.id).order_by(
        Groups.group_name
    ).all()
    return request3

def select_4():
    request_4 = session.query(
        func.round(func.avg(Marks.mark), 2).label('avg_grade'),
        Groups.group_name
    ).join(Students, Students.group_id == Groups.id).join(Marks, Marks.student_id == Students.id
        ).group_by(Groups.id).order_by(
        Groups.group_name
    ).all()
    return request_4

def select_5(teacher_name):
    request_5 = session.query(
        Subjects.subject_name,
        Teachers.fullname
    ).join(Subjects, Subjects.teacher_id == Teachers.id).filter(
        Teachers.fullname == teacher_name
    ).group_by(Subjects.id).order_by(
        Subjects.subject_name
    ).all()
    return request_5

def select_6(group_name):
    request_6 = session.query(
        Students.fullname,
        Groups.group_name
    ).join(Students, Students.group_id == Groups.id).filter(
        Groups.group_name == group_name
    ).group_by(Groups.id).order_by(
        Groups.group_name
    ).all()
    return request_6

def select_7(group_name, subject):
    request_7 = session.query(
        Marks.mark,
        Students.fullname,
    ).join(Students, Marks.student_id == Students.id).join(Groups, Students.group_id == Groups.id).join(Subjects, Marks.subject_id == Subjects.id).filter(
        Groups.group_name == group_name,
        Subjects.subject_name == subject
    ).all()
    return request_7

def select_8(teacher):
    request_8 = session.query(
        func.round(func.avg(Marks.mark), 2).label('avg_grade'),
        Teachers.fullname
    ).join(Teachers, Subjects.teacher_id == Teachers.id).join(Subjects, Marks.subject_id == Subjects.id).filter(
        Teachers.fullname == teacher
    ).all()
    return request_8

def select_9(student):
    request = session.query(
        Subjects.subject_name,
        Students.fullname
    ).join(Students, Marks.student_id == Students.id).join(Marks, Marks.subject_id == Subjects.id).filter(
        Students.fullname == student
    ).all()
    return request

def select_10(students, teacher):
    request = session.query(
        Subjects.subject_name
    ).join(Students, Marks.student_id == Students.id).join(Marks, Marks.subject_id == Subjects.id).join(Teachers, Subjects.teacher_id == Teachers.id).filter(
        Students.fullname == students,
        Teachers.fullname == teacher
    ).all()
    return request


if __name__ == '__main__':
    print(select_10('Маруся Вишняк', 'Мартин Цісик'))