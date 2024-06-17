import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey, select, Text, and_, desc, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, mapped_column, Mapped

engine = create_engine("sqlite:///database", echo = False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Groups(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str] = mapped_column(String)

class Students(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    fullname: Mapped[str] = mapped_column(String(150), nullable=False, index = True)
    group_id: Mapped[str] = mapped_column('group_id', Integer, ForeignKey('groups.id'))
    group: Mapped['Groups'] = relationship(Groups)

class Teachers(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)

class Subjects(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    subject_name: Mapped[str] = mapped_column(String(150), nullable=False, index = True)
    teacher_id: Mapped[str] = mapped_column('teacher_id', Integer, ForeignKey('teachers.id'))
    teacher: Mapped['Teachers'] = relationship(Teachers)

class Marks(Base):
    __tablename__ =  'marks'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer, nullable=False)
    date_of: Mapped[datetime.datetime] = mapped_column('date_of', DateTime)
    student_id: Mapped[str] = mapped_column('student_id', Integer, ForeignKey('students.id'))
    subject_id: Mapped[str] = mapped_column('subject_id', Integer, ForeignKey('subjects.id'))

    student: Mapped['Students'] = relationship(Students)
    subject: Mapped['Subjects'] = relationship(Subjects)

