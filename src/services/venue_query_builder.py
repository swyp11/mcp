"""Wedding venue SQL query builder - 추정 매핑 기반 (Parameterized)"""
from typing import Tuple, List, Any


def build_venue_query(
    guest_count: str,
    budget: str,
    region: str,
    style_preference: str,
    season: str,
    num_recommendations: int = 3
) -> Tuple[str, dict]:
    """
    설문 조건을 기존 tb_wedding_hall 컬럼에 매핑하여 SQL 쿼리 생성

    Returns:
        Tuple[str, dict]: (쿼리 문자열, 파라미터 딕셔너리)

    기존 컬럼:
    - name, venueType, parking, address, phone, email, imageUrl

    매핑 로직:
    - region → address LIKE
    - style_preference → venueType
    - guest_count → parking 기준 추정
    - budget → venueType 기준 추정
    - season → venueType (야외 가능 여부)
    """
    conditions = []
    params = {}

    # 1. region → address (Parameterized)
    if region and region != "상관없음":
        conditions.append("address LIKE :region_pattern")
        params["region_pattern"] = f"%{region}%"

    # 2. style_preference → venueType
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

    # 3. season → venueType 필터 (여름/겨울은 실내 위주)
    if season in ["여름", "겨울"]:
        # 야외 제외
        indoor_types = ["HOTEL", "WEDDING_HALL", "RESTAURANT", "HOUSE_STUDIO"]
        if venue_types:
            venue_types = [vt for vt in venue_types if vt in indoor_types]
        else:
            venue_types = indoor_types

    if venue_types:
        # Parameterized IN clause
        type_placeholders = [f":venue_type_{i}" for i in range(len(venue_types))]
        conditions.append(f"venueType IN ({', '.join(type_placeholders)})")
        for i, vt in enumerate(venue_types):
            params[f"venue_type_{i}"] = vt

    # 4. guest_count → parking 추정
    parking_map = {
        "소규모": (0, 50),
        "중규모": (30, 150),
        "대규모": (100, None),
    }
    if guest_count in parking_map:
        min_val, max_val = parking_map[guest_count]
        conditions.append("parking >= :parking_min")
        params["parking_min"] = min_val
        if max_val:
            conditions.append("parking <= :parking_max")
            params["parking_max"] = max_val

    # 5. budget → venueType 추가 필터
    # 고예산: HOTEL 우선, 저예산: HOTEL 제외
    if budget == "저":
        conditions.append("venueType != :excluded_type")
        params["excluded_type"] = "HOTEL"

    # 쿼리 빌드
    query = "SELECT * FROM tb_wedding_hall"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    # ORDER BY: 고예산이면 HOTEL 우선
    if budget == "고":
        query += " ORDER BY CASE WHEN venueType = 'HOTEL' THEN 0 ELSE 1 END"

    query += " LIMIT :limit"
    params["limit"] = num_recommendations

    return query, params


def get_query_explanation(
    guest_count: str,
    budget: str,
    region: str,
    style_preference: str,
    season: str
) -> dict:
    """쿼리 매핑 설명 반환 (디버깅/로깅용)"""
    return {
        "region_mapping": f"address LIKE '%{region}%'" if region != "상관없음" else "전체 지역",
        "style_mapping": f"{style_preference} → venueType 매핑",
        "guest_count_mapping": f"{guest_count} → parking 수 기준 추정",
        "budget_mapping": f"{budget} 예산 → venueType 우선순위",
        "season_mapping": f"{season} → 야외/실내 필터",
    }
