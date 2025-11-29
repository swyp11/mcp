"""Recommendation routes"""
from fastapi import APIRouter, HTTPException

from src.services.schemas import RecommendationRequest, RecommendationResponse, DressRecommendation
from src.services.dress_recommender import recommender, DressRecommender
from src.database import AsyncSessionLocal
from src.database.repositories.dress import recommendation_repo
# Redis disabled
# from src.config import redis_client

router = APIRouter(prefix="", tags=["recommendations"])


@router.post("/recommend", response_model=RecommendationResponse)
async def recommend_dress(request: RecommendationRequest):
    """
    Get wedding dress recommendations

    Parameters:
    - **arm_length**: Arm length (short, normal, long)
    - **leg_length**: Leg length (short, normal, long)
    - **neck_length**: Neck length (short, normal, long)
    - **face_shape**: Face shape (oval, wide, angular, long)
    - **body_type**: Body type (thin, medium, heavy)
    - **num_recommendations**: Number of recommendations (1-5, default: 3)

    Returns wedding dress recommendations with styling tips
    """
    try:
        arm_length = request.arm_length.value
        leg_length = request.leg_length.value
        neck_length = request.neck_length.value
        face_shape = request.face_shape.value
        body_type = request.body_type.value
        num_recommendations = request.num_recommendations

        # Generate query hash
        query_hash = DressRecommender.generate_hash(
            arm_length, leg_length, neck_length, face_shape, body_type, num_recommendations
        )

        # 1. Check Redis cache (temporarily disabled for testing)
        # cached_result = await redis_client.get(f"recommendation:{query_hash}")
        # if cached_result:
        #     return RecommendationResponse(
        #         request_params=request,
        #         recommendations=[
        #             DressRecommendation(**rec)
        #             for rec in cached_result["recommendations"]
        #         ],
        #         overall_advice=cached_result["overall_advice"],
        #         cached=True,
        #         source="redis_cache"
        #     )

        # 2. Check MySQL database
        async with AsyncSessionLocal() as db:
            db_record = await recommendation_repo.get_by_hash(db, query_hash)
            if db_record:
                result = db_record.recommendation
                # Redis disabled
                # await redis_client.set(f"recommendation:{query_hash}", result)

                return RecommendationResponse(
                    request_params=request,
                    recommendations=[
                        DressRecommendation(**rec)
                        for rec in result["recommendations"]
                    ],
                    overall_advice=result["overall_advice"],
                    cached=True,
                    source="mysql_db"
                )

            # 3. Generate new recommendation
            recommendation = await recommender.generate(
                arm_length, leg_length, neck_length, face_shape, body_type, num_recommendations
            )

            # Save to database
            await recommendation_repo.create(
                db, query_hash, arm_length, leg_length, neck_length, face_shape, recommendation, body_type
            )

        # Redis disabled
        # await redis_client.set(f"recommendation:{query_hash}", recommendation)

        return RecommendationResponse(
            request_params=request,
            recommendations=[
                DressRecommendation(**rec)
                for rec in recommendation["recommendations"]
            ],
            overall_advice=recommendation["overall_advice"],
            cached=False,
            source="ai_generated"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
