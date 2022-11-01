# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Float, String, JSON, Sequence, Table, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


def as_dict(t):
    return {c.name: getattr(t, c.name) for c in t.__table__.columns}


class MetaData(Base):
    __tablename__ = "metadata"
    id = Column(Integer, Sequence("id"), primary_key=True, nullable=False)
    name = Column(String)
    value = Column(String)


class SystemInfo(Base):
    __tablename__ = "systeminfo"
    id = Column(Integer, Sequence("id"), primary_key=True, nullable=False)
    data = Column(JSON)


class FederateGraph(Base):
    __tablename__ = "federategraph"
    id = Column(Integer, Sequence("id"), primary_key=True, nullable=False)
    data = Column(JSON)


class DataGraph(Base):
    __tablename__ = "datagraph"
    id = Column(Integer, Sequence("id"), primary_key=True, nullable=False)
    data = Column(JSON)


class Cores(Base):
    __tablename__ = "cores"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    parent = Column(Integer)
    address = Column(String)


class Federates(Base):
    __tablename__ = "federates"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    parent = Column(Integer)


class FederateEventLogs(Base):
    __tablename__ = "federateeventlogs"
    id = Column(Integer, primary_key=True, nullable=False)
    updated_at = Column(Float)
    name = Column(String)
    requested_time = Column(Float)
    granted_time = Column(Float)
    state = Column(String)


class Brokers(Base):
    __tablename__ = "brokers"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)


class Publications(Base):
    __tablename__ = "publications"
    id = Column(Integer, Sequence("id"), primary_key=True, nullable=False)
    federate_name = Column(String)
    name = Column(String)
    source = Column(Integer)
    target = Column(Integer)
    units = Column(String)
    type = Column(String)
    info = Column(String)
    is_valid = Column(Boolean)


class Subscriptions(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, Sequence("id"), primary_key=True, nullable=False)
    federate_name = Column(String)
    name = Column(String)
    publication_name = Column(String)
    source = Column(Integer)
    target = Column(Integer)
    units = Column(String)
    type = Column(String)
    info = Column(String)
    injection_units = Column(String)
    is_valid = Column(Boolean)


class Inputs(Base):
    __tablename__ = "inputs"
    id = Column(Integer, Sequence("id"), primary_key=True, nullable=False)
    federate_name = Column(String)
    publication_name = Column(String)
    source = Column(Integer)
    target = Column(Integer)
    units = Column(String)
    type = Column(String)
    info = Column(String)
    injection_units = Column(String)
    is_valid = Column(Boolean)
