from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Command(Base):
    __tablename__ = 'commands'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

def initialize_db():
    """Initialize the SQLite database and seed it with commands."""
    engine = create_engine('sqlite:///commands.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Seed commands if not already seeded
    if session.query(Command).count() == 0:
        commands = ["ls", "exit", "mkdir", "rm", "cd", "pwd", "touch"]
        for cmd in commands:
            session.add(Command(name=cmd))
        session.commit()
    return session
