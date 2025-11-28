"""Wedding venue recommendation engine - SQL query based"""
import hashlib
from sqlalchemy import text
from src.database import AsyncSessionLocal
from src.services.venue_query_builder import build_venue_query


class VenueRecommender:
    """SQL query based venue recommendation engine"""

    @staticmethod
    def generate_hash(
        guest_count: str,
        budget: str,
        region: str,
        style: str,
        season: str,
        num: int = 3
    ) -> str:
        """Generate unique hash for request parameters"""
        params = f"{guest_count}_{budget}_{region}_{style}_{season}_{num}"
        return hashlib.sha256(params.encode()).hexdigest()

    async def generate(
        self,
        guest_count: str,
        budget: str,
        region: str,
        style_preference: str,
        season: str,
        num_recommendations: int = 3
    ) -> dict:
        """Generate venue recommendation using SQL query"""

        # Build SQL query (parameterized)
        query, params = build_venue_query(
            guest_count, budget, region, style_preference, season, num_recommendations
        )

        # Execute query with parameters
        async with AsyncSessionLocal() as db:
            result = await db.execute(text(query), params)
            rows = result.mappings().fetchall()  # 컬럼명으로 접근 가능

        # Handle empty results - 조건 완화해서 비슷한 결과 찾기
        if not rows:
            fallback_result = await self._find_fallback_venue(
                db, guest_count, budget, region, style_preference, season
            )
            if fallback_result:
                return fallback_result
            return {
                "recommendations": [],
                "overall_advice": "조건에 맞는 웨딩홀을 찾지 못했습니다. 다른 조건으로 검색해보세요."
            }

        # Build response
        recommendations = []
        for row in rows:
            # 컬럼명으로 접근 (인덱스 의존 제거)
            venue_name = row["name"]
            venue_type = row["venueType"]
            parking = row["parking"]
            address = row["address"]
            phone = row["phone"]
            image_url = row["imageUrl"]

            # Generate why_recommended
            why_parts = []
            if guest_count:
                why_parts.append(f"{guest_count} 하객 수용")
            if budget:
                why_parts.append(f"{budget} 예산대")
            if region and region != "상관없음":
                why_parts.append(f"{region} 지역")
            if style_preference:
                why_parts.append(f"{style_preference} 스타일")
            if season:
                why_parts.append(f"{season} 예식")

            why_recommended = f"{', '.join(why_parts)}에 적합합니다."

            # venueType 한글 변환
            venue_type_kr = {
                "HOTEL": "호텔",
                "WEDDING_HALL": "웨딩홀",
                "OUTDOOR": "야외",
                "RESTAURANT": "레스토랑",
                "HOUSE_STUDIO": "하우스스튜디오",
                "GARDEN": "가든",
                "OTHER": "기타"
            }.get(venue_type, venue_type)

            recommendations.append({
                "venue_name": venue_name,
                "description": f"{venue_type_kr} 타입의 웨딩홀입니다.",
                "capacity": f"주차 {parking}대 가능",
                "location": address or "정보 없음",
                "price_range": self._estimate_price_range(venue_type),
                "estimated_cost": self._estimate_cost(venue_type, guest_count),
                "why_recommended": why_recommended,
                "pros": self._get_pros(venue_type),
                "cons": self._get_cons(venue_type),
                "amenities": [f"주차 {parking}대"],
                "food_style": self._get_food_style(venue_type),
                "phone": phone or "",
                "image_url": image_url or "",
                "booking_tips": [
                    f"{season} 시즌은 최소 6개월 전 예약 권장",
                    "주말 예약 시 평일 대비 20-30% 할증",
                    "오프 시즌 할인 이벤트 확인"
                ]
            })

        # Generate overall advice
        overall_advice = self._generate_advice(guest_count, budget, style_preference, season)

        return {
            "recommendations": recommendations,
            "overall_advice": overall_advice
        }

    def _estimate_price_range(self, venue_type: str) -> str:
        """venueType 기반 가격대 추정"""
        price_map = {
            "HOTEL": "고",
            "WEDDING_HALL": "중",
            "OUTDOOR": "중",
            "RESTAURANT": "중",
            "HOUSE_STUDIO": "저",
            "GARDEN": "중",
            "OTHER": "중"
        }
        return price_map.get(venue_type, "중")

    def _estimate_cost(self, venue_type: str, guest_count: str) -> str:
        """예상 비용 추정"""
        base_cost = {
            "HOTEL": {"소규모": "3,000만원~", "중규모": "5,000만원~", "대규모": "8,000만원~"},
            "WEDDING_HALL": {"소규모": "1,500만원~", "중규모": "2,500만원~", "대규모": "4,000만원~"},
            "GARDEN": {"소규모": "1,000만원~", "중규모": "2,000만원~", "대규모": "3,500만원~"},
            "OUTDOOR": {"소규모": "800만원~", "중규모": "1,500만원~", "대규모": "2,500만원~"},
            "RESTAURANT": {"소규모": "500만원~", "중규모": "1,000만원~", "대규모": "2,000만원~"},
            "HOUSE_STUDIO": {"소규모": "300만원~", "중규모": "700만원~", "대규모": "1,200만원~"},
        }
        return base_cost.get(venue_type, {}).get(guest_count, "문의 필요")

    def _get_pros(self, venue_type: str) -> list:
        """venueType 기반 장점"""
        pros_map = {
            "HOTEL": ["최고급 서비스", "부대시설 완비", "접근성 좋음"],
            "WEDDING_HALL": ["전문 웨딩 서비스", "다양한 패키지", "편리한 진행"],
            "GARDEN": ["자연친화적 분위기", "사진 촬영 좋음", "야외 세레모니 가능"],
            "OUTDOOR": ["개방적인 분위기", "자유로운 연출", "자연광 활용"],
            "RESTAURANT": ["맛있는 식사", "아늑한 분위기", "합리적 가격"],
            "HOUSE_STUDIO": ["프라이빗한 공간", "자유로운 구성", "저렴한 비용"],
        }
        return pros_map.get(venue_type, ["정보 없음"])

    def _get_cons(self, venue_type: str) -> list:
        """venueType 기반 단점"""
        cons_map = {
            "HOTEL": ["높은 비용", "형식적 분위기"],
            "WEDDING_HALL": ["획일적인 진행", "시간 제약"],
            "GARDEN": ["날씨 영향", "계절 제한"],
            "OUTDOOR": ["날씨 변수", "편의시설 부족"],
            "RESTAURANT": ["공간 제약", "대규모 어려움"],
            "HOUSE_STUDIO": ["소규모만 가능", "시설 한계"],
        }
        return cons_map.get(venue_type, ["정보 없음"])

    def _get_food_style(self, venue_type: str) -> list:
        """venueType 기반 음식 스타일"""
        food_map = {
            "HOTEL": ["코스", "파인다이닝"],
            "WEDDING_HALL": ["뷔페", "코스"],
            "GARDEN": ["뷔페", "바비큐"],
            "OUTDOOR": ["뷔페", "케이터링"],
            "RESTAURANT": ["코스", "한정식"],
            "HOUSE_STUDIO": ["케이터링", "핑거푸드"],
        }
        return food_map.get(venue_type, ["뷔페"])

    def _generate_advice(self, guest_count: str, budget: str, style: str, season: str) -> str:
        """조건 기반 조언 생성"""
        advices = []

        if budget == "저":
            advices.append("예산을 고려해 평일 예식이나 오프시즌 할인을 활용해보세요")
        elif budget == "고":
            advices.append("프리미엄 서비스와 부대시설을 적극 활용하세요")

        if guest_count == "소규모":
            advices.append("소규모 웨딩은 프라이빗한 분위기를 살릴 수 있어요")
        elif guest_count == "대규모":
            advices.append("대규모 예식은 주차와 접근성을 꼭 확인하세요")

        if season in ["봄", "가을"]:
            advices.append("성수기라 최소 6개월 전 예약을 권장합니다")
        elif season == "여름":
            advices.append("야외 웨딩홀은 날씨 변수를 고려하세요")
        elif season == "겨울":
            advices.append("실내 웨딩홀 위주로 알아보시는 것을 추천드려요")

        return " ".join(advices) if advices else "조건에 맞는 웨딩홀을 신중히 비교해보세요."

    async def _find_fallback_venue(
        self,
        db,
        guest_count: str,
        budget: str,
        region: str,
        style_preference: str,
        season: str
    ) -> dict | None:
        """조건 완화해서 비슷한 웨딩홀 1개 찾기"""

        # 완화 순서: region → parking → venueType → 전체
        fallback_queries = [
            # 1단계: region만 제거
            ("SELECT * FROM tb_wedding_hall LIMIT 1", {}, "지역 조건을 완화"),
        ]

        # venueType 매핑
        style_to_venue_type = {
            "럭셔리": ["HOTEL"],
            "모던": ["HOTEL", "WEDDING_HALL"],
            "클래식": ["HOTEL", "WEDDING_HALL"],
            "자연친화": ["GARDEN", "OUTDOOR"],
            "야외정원": ["GARDEN", "OUTDOOR"],
            "미니멀": ["HOUSE_STUDIO", "RESTAURANT"],
            "유니크": ["HOUSE_STUDIO", "RESTAURANT", "OTHER"],
        }
        venue_types = style_to_venue_type.get(style_preference, [])

        # 1단계: 스타일만 유지
        if venue_types:
            type_placeholders = [f":vt_{i}" for i in range(len(venue_types))]
            params = {f"vt_{i}": vt for i, vt in enumerate(venue_types)}
            fallback_queries.insert(0, (
                f"SELECT * FROM tb_wedding_hall WHERE venueType IN ({', '.join(type_placeholders)}) LIMIT 1",
                params,
                "스타일 조건만 적용"
            ))

        async with AsyncSessionLocal() as new_db:
            for query, params, relaxed_condition in fallback_queries:
                result = await new_db.execute(text(query), params)
                row = result.mappings().fetchone()

                if row:
                    # 결과 포맷팅
                    venue_type = row["venueType"]
                    venue_type_kr = {
                        "HOTEL": "호텔", "WEDDING_HALL": "웨딩홀", "OUTDOOR": "야외",
                        "RESTAURANT": "레스토랑", "HOUSE_STUDIO": "하우스스튜디오",
                        "GARDEN": "가든", "OTHER": "기타"
                    }.get(venue_type, venue_type)

                    recommendation = {
                        "venue_name": row["name"],
                        "description": f"{venue_type_kr} 타입의 웨딩홀입니다.",
                        "capacity": f"주차 {row['parking']}대 가능",
                        "location": row["address"] or "정보 없음",
                        "price_range": self._estimate_price_range(venue_type),
                        "estimated_cost": self._estimate_cost(venue_type, guest_count),
                        "why_recommended": f"정확히 일치하는 결과가 없어 {relaxed_condition}하여 추천드립니다.",
                        "pros": self._get_pros(venue_type),
                        "cons": self._get_cons(venue_type),
                        "amenities": [f"주차 {row['parking']}대"],
                        "food_style": self._get_food_style(venue_type),
                        "phone": row["phone"] or "",
                        "image_url": row["imageUrl"] or "",
                        "booking_tips": ["조건을 조정하시면 더 많은 옵션을 확인할 수 있습니다."]
                    }

                    return {
                        "recommendations": [recommendation],
                        "overall_advice": f"정확히 일치하는 결과가 없어 {relaxed_condition}하여 비슷한 웨딩홀을 추천드립니다."
                    }

        return None


# Global recommender instance
venue_recommender = VenueRecommender()
