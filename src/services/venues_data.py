"""Wedding venue database"""

WEDDING_VENUES = {
    "더 클래식 500": {
        "description": "강남 중심지에 위치한 500명 수용 가능한 대형 럭셔리 연회장",
        "capacity": {"min": 200, "max": 500},
        "price_range": "고",
        "location": "서울 강남구",
        "region": "서울",
        "styles": ["럭셔리", "모던"],
        "seasons": ["봄", "여름", "가을", "겨울"],
        "amenities": [
            "지하철역 도보 5분",
            "주차 200대 가능",
            "프리미엄 신부대기실",
            "최신 음향/조명 시스템"
        ],
        "features": [
            "높은 천장 (5m)",
            "대형 샹들리에",
            "무대 조명 시스템",
            "VIP 라운지"
        ],
        "food_style": ["뷔페", "코스"],
        "pros": [
            "접근성 우수",
            "대형 주차장",
            "최신 시설"
        ],
        "cons": [
            "주말 예약 경쟁률 높음",
            "비용이 높은 편"
        ],
        "suitable_for": {
            "guest_count": ["대규모"],
            "budget": ["고"],
            "style": ["럭셔리", "모던"]
        }
    },

    "가든파티 웨딩홀": {
        "description": "야외 정원과 실내홀이 조화된 자연친화적 웨딩홀",
        "capacity": {"min": 50, "max": 150},
        "price_range": "중",
        "location": "경기 성남시",
        "region": "경기",
        "styles": ["자연친화", "로맨틱", "야외정원"],
        "seasons": ["봄", "가을"],
        "amenities": [
            "야외 정원",
            "주차 80대",
            "포토존 다수",
            "자연채광"
        ],
        "features": [
            "1000평 정원",
            "야외 세레모니 공간",
            "사계절 꽃길",
            "분수대"
        ],
        "food_style": ["뷔페", "바비큐"],
        "pros": [
            "사진 촬영 명소",
            "자연스러운 분위기",
            "합리적 가격"
        ],
        "cons": [
            "날씨 영향 받음",
            "겨울/여름 비추천"
        ],
        "suitable_for": {
            "guest_count": ["소규모", "중규모"],
            "budget": ["중"],
            "style": ["자연친화", "로맨틱"]
        }
    },

    "모던 스카이라운지": {
        "description": "63층 전망과 현대적 인테리어가 돋보이는 프리미엄 웨딩홀",
        "capacity": {"min": 100, "max": 200},
        "price_range": "고",
        "location": "서울 영등포구",
        "region": "서울",
        "styles": ["모던", "럭셔리", "도심뷰"],
        "seasons": ["봄", "여름", "가을", "겨울"],
        "amenities": [
            "63층 전망",
            "발렛파킹",
            "프라이빗 라운지",
            "프리미엄 음향"
        ],
        "features": [
            "한강뷰",
            "통유리 전망",
            "모던 인테리어",
            "LED 조명"
        ],
        "food_style": ["코스", "파인다이닝"],
        "pros": [
            "환상적인 전망",
            "세련된 분위기",
            "야경 아름다움"
        ],
        "cons": [
            "높은 비용",
            "엘리베이터 대기시간"
        ],
        "suitable_for": {
            "guest_count": ["중규모"],
            "budget": ["고"],
            "style": ["모던", "럭셔리"]
        }
    },

    "클래식 팰리스": {
        "description": "전통미와 격식을 중시하는 클래식 스타일 웨딩홀",
        "capacity": {"min": 150, "max": 300},
        "price_range": "중",
        "location": "서울 강북구",
        "region": "서울",
        "styles": ["클래식", "전통"],
        "seasons": ["봄", "여름", "가을", "겨울"],
        "amenities": [
            "주차 150대",
            "한복 대여실",
            "전통 혼례상",
            "넓은 대기실"
        ],
        "features": [
            "전통 한옥 디자인",
            "고급 목재 인테리어",
            "대형 샹들리에",
            "격식있는 분위기"
        ],
        "food_style": ["뷔페", "한정식"],
        "pros": [
            "전통적 분위기",
            "넓은 공간",
            "합리적 가격"
        ],
        "cons": [
            "다소 보수적 분위기",
            "인테리어 오래됨"
        ],
        "suitable_for": {
            "guest_count": ["중규모", "대규모"],
            "budget": ["중"],
            "style": ["클래식", "전통"]
        }
    },

    "컨템포러리 웨딩홀": {
        "description": "현대적 감각과 세련미가 돋보이는 중형 웨딩홀",
        "capacity": {"min": 80, "max": 150},
        "price_range": "중",
        "location": "서울 마포구",
        "region": "서울",
        "styles": ["모던", "미니멀"],
        "seasons": ["봄", "여름", "가을", "겨울"],
        "amenities": [
            "지하철 직결",
            "주차 100대",
            "프라이빗 공간",
            "최신 음향"
        ],
        "features": [
            "심플한 인테리어",
            "화이트톤 디자인",
            "자연채광",
            "유연한 공간 구성"
        ],
        "food_style": ["뷔페", "코스"],
        "pros": [
            "접근성 좋음",
            "깔끔한 분위기",
            "합리적 가격"
        ],
        "cons": [
            "규모가 작은 편",
            "대규모 예식 불가"
        ],
        "suitable_for": {
            "guest_count": ["소규모", "중규모"],
            "budget": ["중"],
            "style": ["모던", "미니멀"]
        }
    },

    "스몰 웨딩 라운지": {
        "description": "소규모 프라이빗 웨딩에 특화된 아늑한 공간",
        "capacity": {"min": 20, "max": 80},
        "price_range": "저",
        "location": "서울 성동구",
        "region": "서울",
        "styles": ["미니멀", "스몰웨딩", "프라이빗"],
        "seasons": ["봄", "여름", "가을", "겨울"],
        "amenities": [
            "소규모 특화",
            "주차 30대",
            "프라이빗 공간",
            "커스텀 가능"
        ],
        "features": [
            "아늑한 분위기",
            "가족 중심 구성",
            "유연한 시간",
            "맞춤형 서비스"
        ],
        "food_style": ["뷔페", "케이터링"],
        "pros": [
            "저렴한 비용",
            "친밀한 분위기",
            "자유로운 구성"
        ],
        "cons": [
            "소규모만 가능",
            "시설 간소함"
        ],
        "suitable_for": {
            "guest_count": ["소규모"],
            "budget": ["저", "중"],
            "style": ["미니멀", "스몰웨딩"]
        }
    },

    "리버사이드 가든": {
        "description": "강변 조망과 정원이 어우러진 프리미엄 야외 웨딩홀",
        "capacity": {"min": 100, "max": 250},
        "price_range": "고",
        "location": "경기 하남시",
        "region": "경기",
        "styles": ["자연친화", "야외정원", "럭셔리"],
        "seasons": ["봄", "가을"],
        "amenities": [
            "강변 조망",
            "야외 정원",
            "주차 150대",
            "포토존"
        ],
        "features": [
            "한강뷰",
            "야외 세레모니",
            "정원 산책로",
            "선셋 뷰"
        ],
        "food_style": ["뷔페", "바비큐", "코스"],
        "pros": [
            "아름다운 경관",
            "사진 명소",
            "넓은 공간"
        ],
        "cons": [
            "날씨 영향",
            "계절 제한",
            "접근성 보통"
        ],
        "suitable_for": {
            "guest_count": ["중규모", "대규모"],
            "budget": ["고"],
            "style": ["자연친화", "럭셔리"]
        }
    },

    "호텔 그랜드볼룸": {
        "description": "5성급 호텔의 최상급 연회장",
        "capacity": {"min": 200, "max": 600},
        "price_range": "고",
        "location": "서울 중구",
        "region": "서울",
        "styles": ["럭셔리", "클래식", "그랜드"],
        "seasons": ["봄", "여름", "가을", "겨울"],
        "amenities": [
            "호텔 부대시설",
            "발렛파킹",
            "럭셔리 대기실",
            "프리미엄 서비스"
        ],
        "features": [
            "초대형 샹들리에",
            "높은 천장",
            "최고급 음향",
            "VIP 서비스"
        ],
        "food_style": ["코스", "파인다이닝"],
        "pros": [
            "최고급 서비스",
            "브랜드 가치",
            "완벽한 시설"
        ],
        "cons": [
            "매우 높은 비용",
            "형식적 분위기"
        ],
        "suitable_for": {
            "guest_count": ["대규모"],
            "budget": ["고"],
            "style": ["럭셔리", "클래식"]
        }
    },

    "아트갤러리 웨딩": {
        "description": "예술 작품이 있는 갤러리형 웨딩 공간",
        "capacity": {"min": 50, "max": 120},
        "price_range": "중",
        "location": "서울 종로구",
        "region": "서울",
        "styles": ["모던", "아트", "유니크"],
        "seasons": ["봄", "여름", "가을", "겨울"],
        "amenities": [
            "예술 작품 전시",
            "주차 60대",
            "독특한 분위기",
            "포토존"
        ],
        "features": [
            "갤러리 공간",
            "예술 작품",
            "화이트 큐브",
            "창의적 연출"
        ],
        "food_style": ["뷔페", "케이터링"],
        "pros": [
            "독특한 분위기",
            "세련된 공간",
            "사진 잘 나옴"
        ],
        "cons": [
            "공간 제약",
            "소규모만 가능"
        ],
        "suitable_for": {
            "guest_count": ["소규모", "중규모"],
            "budget": ["중"],
            "style": ["모던", "유니크"]
        }
    },

    "하우스 웨딩 빌라": {
        "description": "단독 빌라를 통째로 빌려 쓰는 프라이빗 웨딩",
        "capacity": {"min": 30, "max": 100},
        "price_range": "중",
        "location": "경기 용인시",
        "region": "경기",
        "styles": ["프라이빗", "자연친화", "하우스웨딩"],
        "seasons": ["봄", "여름", "가을"],
        "amenities": [
            "독채 사용",
            "정원",
            "주차 50대",
            "BBQ 시설"
        ],
        "features": [
            "프라이빗 공간",
            "정원 파티",
            "자유로운 구성",
            "홈파티 느낌"
        ],
        "food_style": ["케이터링", "바비큐"],
        "pros": [
            "완전 프라이빗",
            "자유로운 분위기",
            "맞춤형 진행"
        ],
        "cons": [
            "소규모만 가능",
            "날씨 영향",
            "준비 번거로움"
        ],
        "suitable_for": {
            "guest_count": ["소규모"],
            "budget": ["중"],
            "style": ["프라이빗", "자연친화"]
        }
    }
}


def get_venue_details(venue_names: list[str]) -> list[dict]:
    """
    Get detailed information for given venue names

    Args:
        venue_names: List of venue names from GPT

    Returns:
        List of detailed venue information
    """
    results = []
    for venue_name in venue_names:
        if venue_name in WEDDING_VENUES:
            venue_info = WEDDING_VENUES[venue_name].copy()
            venue_info["venue_name"] = venue_name
            results.append(venue_info)
        else:
            # Fallback for unknown venues
            results.append({
                "venue_name": venue_name,
                "description": f"{venue_name} 웨딩홀입니다.",
                "capacity": {"min": 100, "max": 200},
                "price_range": "중",
                "location": "정보 없음",
                "amenities": [],
                "pros": [],
                "cons": ["상세 정보를 확인하세요."]
            })

    return results


def get_all_venue_names() -> list[str]:
    """Get list of all available venue names"""
    return list(WEDDING_VENUES.keys())


def get_venues_with_suitability() -> str:
    """Get formatted list of venues with their suitability information"""
    lines = []
    for venue_name, venue_info in WEDDING_VENUES.items():
        suitable = venue_info["suitable_for"]
        guest_count = ", ".join(suitable.get("guest_count", []))
        budget = ", ".join(suitable.get("budget", []))
        style = ", ".join(suitable.get("style", []))

        lines.append(
            f"- {venue_name}: "
            f"하객수({guest_count}), "
            f"예산({budget}), "
            f"스타일({style}), "
            f"지역({venue_info['region']})"
        )
    return "\n".join(lines)


def filter_venues(
    guest_count: str,
    budget: str,
    region: str,
    style_preference: str,
    season: str,
    num_recommendations: int = 3
) -> list[dict]:
    """
    Filter venues based on criteria and return top matches by score

    Args:
        guest_count: 소규모/중규모/대규모
        budget: 저/중/고
        region: 서울/경기/인천/상관없음
        style_preference: 럭셔리/모던/클래식/자연친화/야외정원/미니멀/유니크
        season: 봄/여름/가을/겨울
        num_recommendations: Number of results to return

    Returns:
        List of venue dicts sorted by match score
    """
    scored_venues = []

    for venue_name, venue_info in WEDDING_VENUES.items():
        score = 0
        suitable = venue_info["suitable_for"]

        # 하객 수 매칭 (필수 조건, 가중치 높음)
        if guest_count in suitable.get("guest_count", []):
            score += 3

        # 예산 매칭 (필수 조건, 가중치 높음)
        if budget in suitable.get("budget", []):
            score += 3

        # 지역 매칭
        if region == "상관없음" or venue_info.get("region") == region:
            score += 2

        # 스타일 매칭
        if style_preference in suitable.get("style", []):
            score += 2

        # 시즌 매칭
        if season in venue_info.get("seasons", []):
            score += 1

        # 최소 점수 이상만 추가 (하객수 + 예산 매칭 필수)
        if score >= 6:
            venue_data = venue_info.copy()
            venue_data["venue_name"] = venue_name
            venue_data["match_score"] = score
            scored_venues.append(venue_data)

    # 점수순 정렬
    scored_venues.sort(key=lambda x: x["match_score"], reverse=True)

    return scored_venues[:num_recommendations]
