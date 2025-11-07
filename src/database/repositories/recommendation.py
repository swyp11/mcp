"""Repository for recommendation queries"""
from sqlalchemy import select, update, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from typing import Optional

from src.database.models import RecommendationQuery


class RecommendationRepository:
    """Handle database operations for recommendations"""

    @staticmethod
    async def get_by_hash(db: AsyncSession, query_hash: str) -> Optional[RecommendationQuery]:
        """Get recommendation by hash"""
        result = await db.execute(
            select(RecommendationQuery).where(
                RecommendationQuery.query_hash == query_hash
            )
        )
        query_record = result.scalar_one_or_none()

        if query_record:
            # Update access count
            await db.execute(
                update(RecommendationQuery)
                .where(RecommendationQuery.id == query_record.id)
                .values(
                    access_count=RecommendationQuery.access_count + 1,
                    last_accessed=datetime.utcnow()
                )
            )
            await db.commit()

        return query_record

    @staticmethod
    async def create(
        db: AsyncSession,
        query_hash: str,
        arm_length: str,
        leg_length: str,
        neck_length: str,
        face_shape: str,
        recommendation: dict,
        body_type: str
    ) -> RecommendationQuery:
        """Create new recommendation record"""
        query_record = RecommendationQuery(
            query_hash=query_hash,
            arm_length=arm_length,
            leg_length=leg_length,
            neck_length=neck_length,
            face_shape=face_shape,
            body_type=body_type,
            recommendation=recommendation,
            access_count=1
        )
        db.add(query_record)
        await db.commit()
        await db.refresh(query_record)
        return query_record

    @staticmethod
    async def get_stats(db: AsyncSession) -> dict:
        """Get recommendation statistics"""
        # Total queries
        total_result = await db.execute(
            select(func.count(RecommendationQuery.id))
        )
        total_queries = total_result.scalar()

        # Total accesses
        access_result = await db.execute(
            select(func.sum(RecommendationQuery.access_count))
        )
        total_accesses = access_result.scalar() or 0

        # Most popular combinations
        popular_result = await db.execute(
            select(
                RecommendationQuery.arm_length,
                RecommendationQuery.leg_length,
                RecommendationQuery.neck_length,
                RecommendationQuery.face_shape,
                RecommendationQuery.body_type,
                func.sum(RecommendationQuery.access_count).label('total_access')
            )
            .group_by(
                RecommendationQuery.arm_length,
                RecommendationQuery.leg_length,
                RecommendationQuery.neck_length,
                RecommendationQuery.face_shape,
                RecommendationQuery.body_type
            )
            .order_by(func.sum(RecommendationQuery.access_count).desc())
            .limit(5)
        )
        popular_combinations = [
            {
                "arm_length": row[0],
                "leg_length": row[1],
                "neck_length": row[2],
                "face_shape": row[3],
                "body_type": row[4],
                "access_count": row[5]
            }
            for row in popular_result
        ]

        return {
            "total_unique_queries": total_queries,
            "total_accesses": total_accesses,
            "cache_hit_rate": (total_accesses - total_queries) / total_accesses if total_accesses > 0 else 0,
            "popular_combinations": popular_combinations
        }


# Global repository instance
recommendation_repo = RecommendationRepository()
