from sqlalchemy import create_engine,Column,Integer,String,Boolean,DateTime,Numeric,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker,declarative_base
from sqlalchemy.sql import func
DATABASE_URL ="sqlite:///./harmony"

engine = create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine)

Base= declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# User model
class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    role = relationship('Role')
    properties = relationship('Property', back_populates='landlord')
    tenants = relationship('Tenant', back_populates='user')

# Role model
class Role(Base):
    __tablename__ = 'role'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Property model
class Property(Base):
    __tablename__ = 'property'
    
    id = Column(Integer, primary_key=True)
    landlord_id = Column(Integer, ForeignKey('user.id'))
    location = Column(String, nullable=False)
    created_at = Column(DateTime,default=func.now())
    
    landlord = relationship('User', back_populates='properties')
    tenants = relationship('Tenant', back_populates='property')

# Tenant model
class Tenant(Base):
    __tablename__ = 'tenant'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    property_id = Column(Integer, ForeignKey('property.id'))
    lease_start_date = Column(DateTime, nullable=False)
    lease_end_date = Column(DateTime)
    rent_amount = Column(Numeric, nullable=False)
    deposit = Column(Numeric)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    user = relationship('User', back_populates='tenants')
    property = relationship('Property', back_populates='tenants')
    payments = relationship('Payment', back_populates='tenant')
    maintenance_requests = relationship('MaintenanceRequest', back_populates='tenant')

# Payment model
class Payment(Base):
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    payment_date = Column(DateTime, nullable=False)
    amount = Column(Numeric, nullable=False)
    status_id = Column(Integer, ForeignKey('status.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    tenant = relationship('Tenant', back_populates='payments')
    status = relationship('Status')

# Status model
class Status(Base):
    __tablename__ = 'status'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# MaintenanceRequest model
class MaintenanceRequest(Base):
    __tablename__ = 'maintenance_request'
    
    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    property_id = Column(Integer, ForeignKey('property.id'))
    description = Column(String, nullable=False)
    status_id = Column(Integer, ForeignKey('status.id'))
    urgency_id = Column(Integer, ForeignKey('urgency.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    tenant = relationship('Tenant', back_populates='maintenance_requests')
    property = relationship('Property')
    status = relationship('Status')
    urgency = relationship('Urgency')

# Urgency model
class Urgency(Base):
    __tablename__ = 'urgency'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Expense model
class Expense(Base):
    __tablename__ = 'expense'
    
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('property.id'))
    expense_type = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    date_incurred = Column(DateTime, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    property = relationship('Property')

# FinancialReport model
class FinancialReport(Base):
    __tablename__ = 'financial_report'
    
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey('property.id'))
    report_type_id = Column(Integer, ForeignKey('report_type.id'))
    total_income = Column(Numeric)
    total_expenses = Column(Numeric)
    generated_at = Column(DateTime, nullable=False)
    
    property = relationship('Property')
    report_type = relationship('ReportType')

# ReportType model
class ReportType(Base):
    __tablename__ = 'report_type'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
