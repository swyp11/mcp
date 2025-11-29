"""Venue recommendation routes"""
from fastapi import APIRouter, HTTPException

from src.services.schemas import VenueRecommendationRequest, VenueRecommendationResponse, VenueRecommendation
from src.services.venue_recommender import venue_recommender, VenueRecommender
from src.database import AsyncSessionLocal
from src.database.repositories.venue import venue_repo
# Redis disabled
# from src.config import redis_client

router = APIRouter(prefix="", tags=["venue-recommendations"])


@router.post("/recommend/venue", response_model=VenueRecommendationResponse)
async def recommend_venue(request: VenueRecommendationRequest):
    """
    Get wedding venue recommendations

    Parameters:
    - **guest_count**: Expected number of guests (소규모/중규모/대규모)
    - **budget**: Budget range (저/중/고)
    - **region**: Preferred region (서울/경기/인천/상관없음)
    - **style_preference**: Preferred venue style (럭셔리/모던/클래식/자연친화/야외정원/미니멀/유니크)
    - **season**: Wedding season (봄/여름/가을/겨울)
    - **num_recommendations**: Number of recommendations (1-5, default: 3)

    Returns wedding venue recommendations with details
    """
    try:
        guest_count = request.guest_count.value
        budget = request.budget.value
        region = request.region.value
        style_preference = request.style_preference.value
        season = request.season.value
        num_recommendations = request.num_recommendations

        # Generate query hash
        query_hash = VenueRecommender.generate_hash(
            guest_count, budget, region, style_preference, season, num_recommendations
        )

        # 1. Check Redis cache (temporarily disabled for testing)
        # cached_result = await redis_client.get(f"venue:{query_hash}")
        # if cached_result:
        #     return VenueRecommendationResponse(
        #         request_params=request,
        #         recommendations=[
        #             VenueRecommendation(**rec)
        #             for rec in cached_result["recommendations"]
        #         ],
        #         overall_advice=cached_result["overall_advice"],
        #         cached=True,
        #         source="redis_cache"
        #     )

        # 2. Check MySQL database
        async with AsyncSessionLocal() as db:
            db_record = await venue_repo.get_by_hash(db, query_hash)
            if db_record:
                result = db_record.recommendation
                # Save to Redis cache (temporarily disabled for testing)
                # await redis_client.set(f"venue:{query_hash}", result)

                return VenueRecommendationResponse(
                    request_params=request,
                    recommendations=[
                        VenueRecommendation(**rec)
                        for rec in result["recommendations"]
                    ],
                    overall_advice=result["overall_advice"],
                    cached=True,
                    source="mysql_db"
                )

            # 3. Generate new recommendation
            recommendation = await venue_recommender.generate(
                guest_count, budget, region, style_preference, season, num_recommendations
            )

            # Save to database
            await venue_repo.create(
                db, query_hash, guest_count, budget, region, style_preference, season, recommendation
            )

        # Save to cache (temporarily disabled for testing)
        # await redis_client.set(f"venue:{query_hash}", recommendation)

        return VenueRecommendationResponse(
            request_params=request,
            recommendations=[
                VenueRecommendation(**rec)
                for rec in recommendation["recommendations"]
            ],
            overall_advice=recommendation["overall_advice"],
            cached=False,
            source="ai_generated"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
