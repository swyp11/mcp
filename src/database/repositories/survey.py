"""Repository for survey operations"""
from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from typing import Optional, List, Dict

from src.database.models import Survey, WeddingDress
from src.services.schemas import SurveyCreate, SurveyUpdate


class SurveyRepository:
    """Handle database operations for surveys"""

    @staticmethod
    async def get_by_id(db: AsyncSession, survey_id: int) -> Optional[Survey]:
        """Get survey by ID with dress relationship"""
        result = await db.execute(
            select(Survey)
            .options(selectinload(Survey.dress))
            .where(Survey.id == survey_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(
        db: AsyncSession,
        skip: int = 0,
        limit: int = 100,
        load_dress: bool = False
    ) -> List[Survey]:
        """Get all surveys with pagination"""
        query = select(Survey)

        if load_dress:
            query = query.options(selectinload(Survey.dress))

        query = query.offset(skip).limit(limit).order_by(Survey.created_at.desc())
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def get_by_body_type(
        db: AsyncSession,
        arm_length: str,
        leg_length: str,
        neck_length: str,
        face_shape: str,
        body_type: str
    ) -> List[Survey]:
        """Get surveys by body measurements"""
        result = await db.execute(
            select(Survey)
            .options(selectinload(Survey.dress))
            .where(
                Survey.arm_length == arm_length,
                Survey.leg_length == leg_length,
                Survey.neck_length == neck_length,
                Survey.face_shape == face_shape,
                Survey.body_type == body_type
            )
            .order_by(Survey.created_at.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def create(db: AsyncSession, survey: SurveyCreate) -> Survey:
        """Create new survey"""
        db_survey = Survey(**survey.model_dump())
        db.add(db_survey)
        await db.commit()
        await db.refresh(db_survey)

        # Load dress relationship
        result = await db.execute(
            select(Survey)
            .options(selectinload(Survey.dress))
            .where(Survey.id == db_survey.id)
        )
        return result.scalar_one()

    @staticmethod
    async def update(
        db: AsyncSession,
        survey_id: int,
        survey_update: SurveyUpdate
    ) -> Optional[Survey]:
        """Update survey"""
        result = await db.execute(
            select(Survey).where(Survey.id == survey_id)
        )
        db_survey = result.scalar_one_or_none()

        if not db_survey:
            return None

        # Update only provided fields
        update_data = survey_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_survey, field, value)

        await db.commit()
        await db.refresh(db_survey)

        # Load dress relationship
        result = await db.execute(
            select(Survey)
            .options(selectinload(Survey.dress))
            .where(Survey.id == db_survey.id)
        )
        return result.scalar_one()

    @staticmethod
    async def delete(db: AsyncSession, survey_id: int) -> bool:
        """Delete survey"""
        result = await db.execute(
            select(Survey).where(Survey.id == survey_id)
        )
        db_survey = result.scalar_one_or_none()

        if not db_survey:
            return False

        await db.delete(db_survey)
        await db.commit()
        return True

    @staticmethod
    async def get_stats(db: AsyncSession) -> Dict:
        """Get survey statistics"""
        # Total surveys
        total_result = await db.execute(
            select(func.count(Survey.id))
        )
        total_surveys = total_result.scalar()

        # Most popular body type
        body_type_result = await db.execute(
            select(
                Survey.arm_length,
                Survey.leg_length,
                Survey.neck_length,
                Survey.face_shape,
                Survey.body_type,
                func.count(Survey.id).label('count')
            )
            .group_by(
                Survey.arm_length,
                Survey.leg_length,
                Survey.neck_length,
                Survey.face_shape,
                Survey.body_type
            )
            .order_by(func.count(Survey.id).desc())
            .limit(5)
        )
        popular_body_types = [
            {
                "arm_length": row[0],
                "leg_length": row[1],
                "neck_length": row[2],
                "face_shape": row[3],
                "body_type": row[4],
                "count": row[5]
            }
            for row in body_type_result
        ]

        # Most recommended dresses
        dress_result = await db.execute(
            select(
                Survey.dress_id,
                WeddingDress.name,
                WeddingDress.style,
                func.count(Survey.id).label('recommendation_count')
            )
            .join(WeddingDress, Survey.dress_id == WeddingDress.id)
            .where(Survey.dress_id.isnot(None))
            .group_by(Survey.dress_id, WeddingDress.name, WeddingDress.style)
            .order_by(func.count(Survey.id).desc())
            .limit(5)
        )
        popular_dresses = [
            {
                "dress_id": row[0],
                "dress_name": row[1],
                "style": row[2],
                "recommendation_count": row[3]
            }
            for row in dress_result
        ]

        # Body measurement distribution
        arm_dist = await db.execute(
            select(Survey.arm_length, func.count(Survey.id))
            .group_by(Survey.arm_length)
        )
        leg_dist = await db.execute(
            select(Survey.leg_length, func.count(Survey.id))
            .group_by(Survey.leg_length)
        )
        neck_dist = await db.execute(
            select(Survey.neck_length, func.count(Survey.id))
            .group_by(Survey.neck_length)
        )
        face_dist = await db.execute(
            select(Survey.face_shape, func.count(Survey.id))
            .group_by(Survey.face_shape)
        )
        body_dist = await db.execute(
            select(Survey.body_type, func.count(Survey.id))
            .group_by(Survey.body_type)
        )

        return {
            "total_surveys": total_surveys,
            "popular_body_types": popular_body_types,
            "popular_dresses": popular_dresses,
            "distribution": {
                "arm_length": {row[0]: row[1] for row in arm_dist},
                "leg_length": {row[0]: row[1] for row in leg_dist},
                "neck_length": {row[0]: row[1] for row in neck_dist},
                "face_shape": {row[0]: row[1] for row in face_dist},
                "body_type": {row[0]: row[1] for row in body_dist}
            }
        }


# Global repository instance
survey_repo = SurveyRepository()
