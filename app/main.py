from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.database import User,Role,Payment,Property,Urgency,Tenant,MaintenanceRequest,Status,Expense,FinancialReport
from models.schemas import UserCreate, UserResponse, UserUpdate,RoleResponse, RoleCreate,RoleResponse,  PropertyCreate, PropertyUpdate,PropertyResponse,TenantCreate,TenantUpdate,TenantResponse,PaymentCreate,PaymentResponse,StatusCreate,StatusResponse,MaintenanceRequestCreate,MaintenanceRequestResponse,UrgencyCreate,UrgencyResponse,ExpenseCreate,ExpenseResponse,FinancialReportCreate,FinancialReportResponse,ReportTypeCreate,ReportTypeResponse,MaintenanceRequestUpdate,PaymentUpdate,ExpenseUpdate
from models.database import Base,get_db,engine

app = FastAPI()
Base.metadata.create_all(engine)

# Create a User
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all Users
@app.get("/users", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

# Get a specific User by ID
@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update a User
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for key, value in user.dict().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

# Delete a User
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

@app.post("/roles", response_model=RoleResponse)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    db_role = Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@app.get("/roles", response_model=list[RoleResponse])
def read_roles(db: Session = Depends(get_db)):
    roles = db.query(Role).all()
    return roles

@app.get("/roles/{role_id}", response_model=RoleResponse)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@app.put("/roles/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, role: RoleCreate, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    for key, value in role.dict().items():
        setattr(db_role, key, value)

    db.commit()
    db.refresh(db_role)
    return db_role

@app.delete("/roles/{role_id}", response_model=dict)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    db.delete(role)
    db.commit()
    return {"message": "Role deleted successfully"}

@app.post("/properties", response_model=PropertyResponse)
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    db_property = Property(**property.dict())
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property

@app.get("/properties", response_model=list[PropertyResponse])
def read_properties(db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    return properties

@app.get("/properties/{property_id}", response_model=PropertyResponse)
def read_property(property_id: int, db: Session = Depends(get_db)):
    property = db.query(Property).filter(Property.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@app.put("/properties/{property_id}", response_model=PropertyResponse)
def update_property(property_id: int, property: PropertyUpdate, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    
    for key, value in property.dict().items():
        setattr(db_property, key, value)

    db.commit()
    db.refresh(db_property)
    return db_property

@app.delete("/properties/{property_id}", response_model=dict)
def delete_property(property_id: int, db: Session = Depends(get_db)):
    db_property = db.query(Property).filter(Property.id == property_id).first()
    if not db_property:
        raise HTTPException(status_code=404, detail="Property not found")
    
    db.delete(db_property)
    db.commit()
    return {"message": "Property deleted successfully"}

@app.post("/tenants", response_model=TenantResponse)
def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    db_tenant = Tenant(**tenant.dict())
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

@app.get("/tenants", response_model=list[TenantResponse])
def read_tenants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tenants = db.query(Tenant).offset(skip).limit(limit).all()
    return tenants

@app.get("/tenants/{tenant_id}", response_model=TenantResponse)
def read_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

@app.put("/tenants/{tenant_id}", response_model=TenantResponse)
def update_tenant(tenant_id: int, tenant: TenantUpdate, db: Session = Depends(get_db)):
    db_tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    
    for key, value in tenant.dict().items():
        setattr(db_tenant, key, value)

    db.commit()
    db.refresh(db_tenant)
    return db_tenant

@app.delete("/tenants/{tenant_id}", response_model=dict)
def delete_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    
    db.delete(tenant)
    db.commit()
    return {"message": "Tenant deleted successfully"}

@app.post("/payments", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

@app.get("/payments", response_model=list[PaymentResponse])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    payments = db.query(Payment).offset(skip).limit(limit).all()
    return payments

@app.get("/payments/{payment_id}", response_model=PaymentResponse)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.put("/payments/{payment_id}", response_model=PaymentResponse)
def update_payment(payment_id: int, payment: PaymentUpdate, db: Session = Depends(get_db)):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    for key, value in payment.dict().items():
        setattr(db_payment, key, value)

    db.commit()
    db.refresh(db_payment)
    return db_payment

@app.delete("/payments/{payment_id}", response_model=dict)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    db.delete(payment)
    db.commit()
    return {"message": "Payment deleted successfully"}

@app.post("/maintenance-requests", response_model=MaintenanceRequestResponse)
def create_maintenance_request(request: MaintenanceRequestCreate, db: Session = Depends(get_db)):
    db_request = MaintenanceRequest(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

@app.get("/maintenance-requests", response_model=list[MaintenanceRequestResponse])
def read_maintenance_requests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    requests = db.query(MaintenanceRequest).offset(skip).limit(limit).all()
    return requests

@app.get("/maintenance-requests/{request_id}", response_model=MaintenanceRequestResponse)
def read_maintenance_request(request_id: int, db: Session = Depends(get_db)):
    request = db.query(MaintenanceRequest).filter(MaintenanceRequest.id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Maintenance Request not found")
    return request

@app.put("/maintenance-requests/{request_id}", response_model=MaintenanceRequestResponse)
def update_maintenance_request(request_id: int, request: MaintenanceRequestUpdate, db: Session = Depends(get_db)):
    db_request = db.query(MaintenanceRequest).filter(MaintenanceRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(status_code=404, detail="Maintenance Request not found")
    
    for key, value in request.dict().items():
        setattr(db_request, key, value)

    db.commit()
    db.refresh(db_request)
    return db_request

@app.delete("/maintenance-requests/{request_id}", response_model=dict)
def delete_maintenance_request(request_id: int, db: Session = Depends(get_db)):
    request = db.query(MaintenanceRequest).filter(MaintenanceRequest.id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Maintenance Request not found")
    
    db.delete(request)
    db.commit()
    return {"message": "Maintenance Request deleted successfully"}

@app.post("/expenses", response_model=ExpenseResponse)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.get("/expenses", response_model=list[ExpenseResponse])
def read_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    expenses = db.query(Expense).offset(skip).limit(limit).all()
    return expenses

@app.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@app.put("/expenses/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, expense: ExpenseUpdate, db: Session = Depends(get_db)):
    db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    for key, value in expense.dict().items():
        setattr(db_expense, key, value)

    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.delete("/financial-reports/{report_id}", response_model=dict)
def delete_financial_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(FinancialReport).filter(FinancialReport.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Financial Report not found")
    
    db.delete(report)
    db.commit()
    return {"message": "Financial Report deleted successfully"}

