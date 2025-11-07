"""Pydantic schemas for request/response"""
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
from datetime import date, datetime
from decimal import Decimal


class ArmLength(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


class LegLength(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


class NeckLength(str, Enum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


class FaceShape(str, Enum):
    OVAL = "oval"
    WIDE = "wide"
    ANGULAR = "angular"
    LONG = "long"


class BodyType(str, Enum):
    THIN = "thin"
    MEDIUM = "medium"
    HEAVY = "heavy"


class RecommendationRequest(BaseModel):
    """Wedding dress recommendation request"""
    arm_length: ArmLength = Field(..., description="Arm length")
    leg_length: LegLength = Field(..., description="Leg length")
    neck_length: NeckLength = Field(..., description="Neck length")
    face_shape: FaceShape = Field(..., description="Face shape")
    body_type: BodyType = Field(..., description="Body type")
    num_recommendations: int = Field(
        default=3,
        ge=1,
        le=5,
        description="Number of recommendations (1-5)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "arm_length": "medium",
                "leg_length": "long",
                "neck_length": "medium",
                "face_shape": "oval",
                "body_type": "medium",
                "num_recommendations": 3
            }
        }


class DressRecommendation(BaseModel):
    """Single dress recommendation"""
    style_name: str = Field(..., description="Dress style name")
    description: str = Field(..., description="Dress description")
    why_recommended: str = Field(..., description="Why recommended")
    styling_tips: List[str] = Field(default_factory=list, description="Styling tips")


class RecommendationResponse(BaseModel):
    """Wedding dress recommendation response"""
    request_params: RecommendationRequest
    recommendations: List[DressRecommendation] = Field(..., description="Dress recommendations")
    overall_advice: str = Field(..., description="Overall advice")
    cached: bool = Field(default=False, description="Whether cached result")
    source: str = Field(default="ai_generated", description="Result source")


# ============================================================================
# Wedding Dress Schemas
# ============================================================================

class WeddingDressBase(BaseModel):
    """Base wedding dress schema"""
    name: str = Field(..., description="Dress name")
    description: Optional[str] = Field(None, description="Dress description")
    price: Optional[Decimal] = Field(None, description="Price")
    style: Optional[str] = Field(None, description="Dress style (A-Line, Mermaid, Ball Gown, etc.)")
    size: Optional[str] = Field(None, description="Size")
    color: Optional[str] = Field(None, description="Color")
    fabric: Optional[str] = Field(None, description="Fabric material")
    availability: bool = Field(default=True, description="Availability status")
    image_url: Optional[str] = Field(None, description="Image URL")


class WeddingDressCreate(WeddingDressBase):
    """Schema for creating wedding dress"""
    pass


class WeddingDressUpdate(BaseModel):
    """Schema for updating wedding dress"""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    style: Optional[str] = None
    size: Optional[str] = None
    color: Optional[str] = None
    fabric: Optional[str] = None
    availability: Optional[bool] = None
    image_url: Optional[str] = None


class WeddingDressResponse(WeddingDressBase):
    """Schema for wedding dress response"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ============================================================================
# Survey Schemas
# ============================================================================

class SurveyBase(BaseModel):
    """Base survey schema"""
    arm_length: ArmLength = Field(..., description="Arm length")
    leg_length: LegLength = Field(..., description="Leg length")
    neck_length: NeckLength = Field(..., description="Neck length")
    face_shape: FaceShape = Field(..., description="Face shape")
    body_type: BodyType = Field(..., description="Body type")
    event_date: Optional[date] = Field(None, description="Wedding event date")
    notes: Optional[str] = Field(None, description="Additional notes")


class SurveyCreate(SurveyBase):
    """Schema for creating survey"""
    dress_id: Optional[int] = Field(None, description="Recommended dress ID")


class SurveyUpdate(BaseModel):
    """Schema for updating survey"""
    dress_id: Optional[int] = None
    event_date: Optional[date] = None
    notes: Optional[str] = None


class SurveyResponse(SurveyBase):
    """Schema for survey response"""
    id: int
    dress_id: Optional[int]
    created_at: datetime
    updated_at: datetime
    dress: Optional[WeddingDressResponse] = None

    class Config:
        from_attributes = True
