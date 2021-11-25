from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy import desc


engine = create_engine('sqlite:///referee.sqlite')
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


class RefereeModel(Base):
    __tablename__ = 'referee'
    userID = Column(String, primary_key=True)
    serverID = Column(String, primary_key=True)
    warning = Column(Boolean, default=0)
    yellowCard = Column(Boolean, default=0)
    redCard = Column(Boolean, default=0)
    totalWarnings = Column(Integer, default=0)
    totalYellows = Column(Integer, default=0)
    totalReds = Column(Integer, default=0)
    totalExpulsions = Column(Integer, default=0)


Base.metadata.create_all(engine)


def check_exists(user_id, server_id):
    check_user = session.query(RefereeModel).filter_by(userID=user_id, serverID=server_id).one_or_none()
    if check_user:
        return check_user
    else:
        return False


def add(user_id, server_id):
    aux_user = RefereeModel()
    aux_user.userID = user_id
    aux_user.serverID = server_id
    session.add(aux_user)
    session.commit()
    return aux_user


def get_user(user_id, server_id):
    aux_user = check_exists(user_id, server_id)
    if aux_user:
        return aux_user
    else:
        aux_user = add(user_id, server_id)
        return aux_user


def get_leaderboard(server_id):
    top_warnings = session.query(RefereeModel).filter_by(serverID=server_id).order_by(RefereeModel.totalWarnings)\
        .limit(3).all()
    top_yellows = session.query(RefereeModel).filter_by(serverID=server_id).order_by(RefereeModel.totalYellows)\
        .limit(3).all()
    top_reds = session.query(RefereeModel).filter_by(serverID=server_id).order_by(RefereeModel.totalReds)\
        .limit(3).all()
    top_expulsions = session.query(RefereeModel).filter_by(serverID=server_id).order_by(RefereeModel.serverID)\
        .limit(3).all()

    return [top_warnings, top_yellows, top_reds, top_expulsions]


def warning(user_id, server_id):
    aux_user = get_user(user_id, server_id)
    yellow_check = False
    red_check = False
    if aux_user.warning and aux_user.yellowCard:
        aux_user.warning = False
        aux_user.yellowCard = False
        aux_user.redCard = True
        aux_user.totalWarnings += 1
        aux_user.totalYellows += 1
        aux_user.totalReds +=1
        red_check = True
        session.commit()
        return yellow_check, red_check

    elif aux_user.warning:
        aux_user.warning = False
        aux_user.yellowCard = True
        aux_user.totalWarnings += 1
        aux_user.totalYellows += 1
        yellow_check = True
        session.commit()
        return yellow_check, red_check

    else:
        aux_user.warning = True
        aux_user.totalWarnings += 1
        session.commit()
        return yellow_check, red_check


def yellow(user_id, server_id):
    aux_user = get_user(user_id, server_id)
    red_check = False
    if aux_user.yellowCard:
        aux_user.yellowCard = False
        aux_user.totalYellows += 1
        aux_user.totalReds += 1
        session.commit()
        red_check = True

    else:
        aux_user.yellowCard = True
        aux_user.totalYellows += 1
        session.commit()

    return red_check


def red(user_id, server_id):
    aux_user = get_user(user_id, server_id)
    aux_user.totalReds += 1
    session.commit()


def expulsion(user_id, server_id):
    aux_user = get_user(user_id, server_id)
    aux_user.totalExpulsions += 1
    session.commit()

# def drop():
#     RefereeModel.__table__.drop(engine)





