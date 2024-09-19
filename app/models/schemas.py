from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# 1. User
class UserBase(BaseModel):
    name: str
    email: str
    role_id: int

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# 2. Role
class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int

    class Config:
        orm_mode = True


# 3. Property
class PropertyBase(BaseModel):
    landlord_id: int
    location: str

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(PropertyBase):
    pass

class PropertyResponse(PropertyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# 4. Tenant
class TenantBase(BaseModel):
    user_id: int
    property_id: int
    lease_start_date: datetime
    lease_end_date: datetime
    rent_amount: float
    deposit: float

class TenantCreate(TenantBase):
    pass

class TenantUpdate(TenantBase):
    pass

class TenantResponse(TenantBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# 5. Payment
class PaymentBase(BaseModel):
    tenant_id: int
    payment_date: datetime
    amount: float
    status_id: int

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    payment_date: Optional[datetime] = None
    status_id: Optional[int] = None

    class Config:
        orm_mode = True

# 6. Status
class StatusBase(BaseModel):
    name: str

class StatusCreate(StatusBase):
    pass

class StatusResponse(StatusBase):
    id: int

    class Config:
        orm_mode = True


# 7. MaintenanceRequest
class MaintenanceRequestBase(BaseModel):
    tenant_id: int
    property_id: int
    description: str
    status_id: int
    urgency_id: int

class MaintenanceRequestCreate(MaintenanceRequestBase):
    pass

class MaintenanceRequestResponse(MaintenanceRequestBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class MaintenanceRequestUpdate(BaseModel):
    description: Optional[str] = None
    status_id: Optional[int] = None
    urgency_id: Optional[int] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# 8. Urgency
class UrgencyBase(BaseModel):
    name: str

class UrgencyCreate(UrgencyBase):
    pass

class UrgencyResponse(UrgencyBase):
    id: int

    class Config:
        orm_mode = True


# 9. Expense
class ExpenseBase(BaseModel):
    property_id: int
    expense_type: str
    amount: float
    date_incurred: datetime
    description: str

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ExpenseUpdate(BaseModel):
    expense_type: Optional[str] = None
    amount: Optional[float] = None
    date_incurred: Optional[datetime] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
# 10. FinancialReport
class FinancialReportBase(BaseModel):
    property_id: int
    report_type_id: int
    total_income: float
    total_expenses: float

class FinancialReportCreate(FinancialReportBase):
    pass

class FinancialReportResponse(FinancialReportBase):
    id: int
    generated_at: datetime

    class Config:
        orm_mode = True


# 11. ReportType
class ReportTypeBase(BaseModel):
    name: str

class ReportTypeCreate(ReportTypeBase):
    pass

class ReportTypeResponse(ReportTypeBase):
    id: int

    class Config:
        orm_mode = True
