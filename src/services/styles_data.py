"""Wedding dress styles database"""

WEDDING_DRESS_STYLES = {
    "A라인": {
        "description": "상체는 슬림하게, 허리부터 A자 형태로 퍼지는 클래식한 스타일. 가장 보편적이고 다양한 체형에 어울리는 만능 실루엣입니다.",
        "characteristics": [
            "상체 피팅, 하체 플레어",
            "자연스러운 허리 라인 강조",
            "우아하고 시간을 초월하는 디자인",
            "움직임이 편안함"
        ],
        "styling_tips": [
            "하이힐로 다리 라인을 더욱 길어 보이게 연출",
            "심플한 목걸이나 귀걸이로 포인트",
            "업스타일 헤어로 목선 강조",
            "베일은 미디엄 길이가 조화로움",
            "허리 라인에 벨트나 새시로 포인트 가능"
        ],
        "suitable_for": ["medium", "짧은 다리", "보통 팔", "짧은 목", "보통 목", "oval", "wide"]
    },

    "볼가운": {
        "description": "프린세스 같은 풍성한 스커트가 특징. 동화 속 공주님 같은 화려하고 드라마틱한 느낌을 연출합니다.",
        "characteristics": [
            "타이트한 보디스와 풍성한 스커트",
            "극적인 볼륨감",
            "로맨틱하고 화려한 분위기",
            "정통 웨딩 드레스 스타일"
        ],
        "styling_tips": [
            "티아라나 크라운으로 프린세스 분위기 연출",
            "롱 베일로 드라마틱한 효과",
            "심플한 액세서리로 드레스가 주인공이 되도록",
            "하이힐 필수 (스커트 길이 고려)",
            "볼륨있는 헤어스타일이나 우아한 업스타일"
        ],
        "suitable_for": ["thin", "medium", "heavy", "짧은 다리", "보통 다리", "긴 목", "보통 목", "넓은 어깨", "짧은 팔", "보통 팔", "oval", "long", "wide"]
    },

    "머메이드": {
        "description": "인어의 꼬리처럼 무릎 아래부터 퍼지는 섹시한 실루엣. 몸매를 그대로 드러내는 글래머러스한 스타일입니다.",
        "characteristics": [
            "신체 라인을 따라 밀착",
            "무릎 아래부터 플레어",
            "섹시하고 세련된 분위기",
            "곡선미 강조"
        ],
        "styling_tips": [
            "자신감 있는 포즈와 워킹 연습 필수",
            "심플한 귀걸이와 팔찌로 우아함 더하기",
            "다운 헤어나 웨이브로 여성스러움 강조",
            "누드톤 하이힐로 다리 라인 연장",
            "보정 속옷으로 완벽한 실루엣 완성"
        ],
        "suitable_for": ["thin", "medium", "긴 다리", "보통 다리", "긴 목", "보통 목", "긴 팔", "보통 팔", "oval", "wide", "angular", "long"]
    },

    "엠파이어": {
        "description": "가슴 바로 아래에서 시작되는 하이 웨이스트 라인이 특징. 편안하면서도 우아한 느낌을 줍니다.",
        "characteristics": [
            "가슴 아래 높은 허리선",
            "흐르는 듯한 스커트",
            "편안한 착용감",
            "로맨틱하고 여성스러운 분위기"
        ],
        "styling_tips": [
            "롱 베일로 로맨틱한 분위기 강조",
            "섬세한 헤어 액세서리나 화관",
            "자연스러운 웨이브 헤어",
            "심플한 샌들이나 로우힐도 어울림",
            "목선 강조하는 목걸이"
        ],
        "suitable_for": ["thin", "medium", "heavy", "짧은 다리", "보통 다리", "긴 다리", "긴 목", "보통 목", "짧은 팔", "보통 팔", "긴 팔", "oval", "long", "wide"]
    },

    "시스": {
        "description": "몸에 자연스럽게 떨어지는 슬림한 실루엣. 미니멀하고 모던한 느낌의 세련된 스타일입니다.",
        "characteristics": [
            "일자형 실루엣",
            "심플하고 깔끔한 라인",
            "모던하고 세련된 분위기",
            "움직임이 자유로움"
        ],
        "styling_tips": [
            "볼드한 액세서리로 포인트",
            "스트레이트 헤어나 세련된 업스타일",
            "스테이트먼트 귀걸이나 목걸이",
            "미니멀한 부케",
            "샤프한 하이힐로 스타일 완성"
        ],
        "suitable_for": ["thin", "긴 다리", "보통 다리", "긴 목", "보통 목", "짧은 팔", "보통 팔", "긴 팔", "oval", "wide", "angular", "long"]
    },

    "트럼펫": {
        "description": "머메이드와 유사하지만 무릎 위 허벅지 중간부터 퍼지는 스타일. 머메이드보다 움직임이 편안합니다.",
        "characteristics": [
            "허벅지 중간까지 밀착",
            "부드러운 플레어",
            "우아하고 세련된 실루엣",
            "머메이드보다 편안한 착용감"
        ],
        "styling_tips": [
            "미디엄 길이 베일로 균형감",
            "세련된 업스타일 헤어",
            "우아한 목걸이와 귀걸이",
            "하이힐로 다리 라인 연장",
            "클래식한 부케"
        ],
        "suitable_for": ["thin", "medium", "긴 다리", "보통 다리", "긴 목", "보통 목", "짧은 팔", "보통 팔", "긴 팔", "oval", "wide", "angular", "long"]
    },

    "프린세스": {
        "description": "볼가운과 유사하지만 더 풍성하고 화려한 스타일. 최고의 드라마틱함을 원하는 신부에게 완벽합니다.",
        "characteristics": [
            "극도로 풍성한 스커트",
            "화려한 장식",
            "동화 속 공주 분위기",
            "최대한의 볼륨"
        ],
        "styling_tips": [
            "티아라나 왕관으로 공주님 컨셉 완성",
            "카테드럴 베일로 웅장함 더하기",
            "화려한 헤어 업스타일",
            "심플한 액세서리로 밸런스",
            "드라마틱한 부케"
        ],
        "suitable_for": ["thin", "medium", "heavy", "짧은 다리", "보통 다리", "긴 다리", "긴 목", "보통 목", "짧은 팔", "보통 팔", "oval", "long", "wide"]
    },

    "슬립드레스": {
        "description": "속옷에서 영감을 받은 미니멀한 스타일. 실크 같은 소재로 흘러내리는 듯한 우아함이 특징입니다.",
        "characteristics": [
            "얇고 가벼운 소재",
            "심플한 라인",
            "섹시하고 모던함",
            "편안한 착용감"
        ],
        "styling_tips": [
            "섬세한 레이어드 목걸이",
            "자연스러운 웨이브 헤어",
            "미니멀한 귀걸이",
            "누드톤 스트랩 샌들",
            "작고 심플한 부케"
        ],
        "suitable_for": ["thin", "긴 다리", "보통 다리", "긴 목", "보통 목", "짧은 팔", "보통 팔", "긴 팔", "oval", "wide", "angular", "long"]
    },

    "티어드": {
        "description": "여러 겹의 레이어가 층층이 쌓인 로맨틱한 스타일. 움직일 때마다 풍성하게 펼쳐지는 매력이 있습니다.",
        "characteristics": [
            "여러 층의 러플",
            "볼륨감과 움직임",
            "로맨틱하고 여성스러움",
            "보헤미안 느낌"
        ],
        "styling_tips": [
            "자연스러운 웨이브나 반묶음 헤어",
            "빈티지 액세서리",
            "화관이나 꽃 헤어핀",
            "레이스 베일",
            "와일드 플라워 부케"
        ],
        "suitable_for": ["thin", "medium", "heavy", "긴 다리", "보통 다리", "짧은 다리", "짧은 목", "보통 목", "긴 목", "짧은 팔", "보통 팔", "긴 팔", "oval", "wide", "angular"]
    },

    "하이-로우": {
        "description": "앞은 짧고 뒤는 긴 비대칭 헴라인. 다리를 드러내면서도 드레스의 우아함을 유지하는 독특한 스타일입니다.",
        "characteristics": [
            "비대칭 스커트 길이",
            "앞쪽 다리 노출",
            "모던하고 독특한 디자인",
            "움직임이 자유로움"
        ],
        "styling_tips": [
            "스테이트먼트 슈즈로 포인트 (발목이 보이니까)",
            "세련된 업스타일로 균형",
            "볼드한 귀걸이",
            "짧은 베일이나 베일 없이",
            "컴팩트한 부케"
        ],
        "suitable_for": ["thin", "medium", "긴 다리", "보통 다리", "긴 목", "보통 목", "짧은 팔", "보통 팔", "긴 팔", "oval", "wide", "angular", "long"]
    },

    "오프숄더": {
        "description": "어깨를 드러내는 네크라인으로 우아하고 로맨틱한 분위기. 쇄골과 목선을 아름답게 강조합니다.",
        "characteristics": [
            "어깨 라인 노출",
            "로맨틱한 네크라인",
            "우아하고 여성스러움",
            "쇄골 강조"
        ],
        "styling_tips": [
            "목걸이보다는 귀걸이로 포인트",
            "다운 헤어나 한쪽으로 넘긴 헤어",
            "쇄골라인 강조하는 메이크업",
            "어깨 라인 관리 중요",
            "심플한 팔찌나 링"
        ],
        "suitable_for": ["thin", "medium", "heavy", "긴 다리", "보통 다리", "짧은 다리", "긴 목", "보통 목", "짧은 팔", "보통 팔", "oval", "wide", "angular", "long"]
    },

    "홀터넥": {
        "description": "목 뒤에서 묶이는 스타일로 등과 어깨를 드러냅니다. 섹시하면서도 우아한 느낌을 줍니다.",
        "characteristics": [
            "목 뒤 스트랩",
            "등 노출",
            "어깨와 팔 강조",
            "세련되고 섹시함"
        ],
        "styling_tips": [
            "업스타일 헤어 필수",
            "스테이트먼트 귀걸이",
            "목걸이는 생략 (네크라인 방해)",
            "등 라인 관리 중요",
            "하이힐로 전체 비율 맞추기"
        ],
        "suitable_for": ["thin", "medium", "긴 다리", "보통 다리", "긴 목", "보통 목", "넓은 어깨", "긴 팔", "보통 팔", "angular", "oval", "wide"]
    }
}


def get_style_details(style_names: list[str]) -> list[dict]:
    """
    Get detailed information for given style names

    Args:
        style_names: List of style names from GPT-4

    Returns:
        List of detailed style information
    """
    results = []
    for style_name in style_names:
        if style_name in WEDDING_DRESS_STYLES:
            style_info = WEDDING_DRESS_STYLES[style_name].copy()
            style_info["style_name"] = style_name
            results.append(style_info)
        else:
            # Fallback for unknown styles
            results.append({
                "style_name": style_name,
                "description": f"{style_name} 스타일의 웨딩 드레스입니다.",
                "characteristics": [],
                "styling_tips": ["전문 스타일리스트와 상담하시기 바랍니다."],
                "suitable_for": []
            })

    return results


def get_all_style_names() -> list[str]:
    """Get list of all available style names"""
    return list(WEDDING_DRESS_STYLES.keys())


def get_styles_with_suitability() -> str:
    """Get formatted list of styles with their suitability information"""
    lines = []
    for style_name, style_info in WEDDING_DRESS_STYLES.items():
        suitable = ", ".join(style_info["suitable_for"])
        lines.append(f"- {style_name}: {suitable}")
    return "\n".join(lines)
