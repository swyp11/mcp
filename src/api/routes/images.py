"""
Image serving routes
DB에 저장된 이미지 경로로 실제 이미지 파일을 제공하는 API
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
from src.config import settings

router = APIRouter(prefix="/images", tags=["Images"])


@router.get("/{table_name}/{filename}")
async def get_image(table_name: str, filename: str):
    """
    DB에 저장된 이미지 경로로 실제 이미지 파일 반환

    Args:
        table_name: 테이블 이름 (tb_dress, tb_dress_shop, tb_wedding_hall 등)
        filename: 파일명 (확장자 포함 또는 미포함)

    Returns:
        이미지 파일

    Example:
        GET /images/tb_dress/dress_1.png
        GET /images/tb_dress_shop/shop_5.png
    """
    # 파일명에 확장자가 없으면 .png 추가
    if not filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        filename = f"{filename}.png"

    # 서버의 실제 파일 경로 구성
    # 기본 경로: {image_base_path}/{table_name}/{filename}
    file_path = Path(settings.image_base_path) / table_name / filename

    # 파일 존재 여부 확인
    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail=f"Image not found: {table_name}/{filename}"
        )

    # 파일이 실제로 이미지인지 확인 (보안)
    allowed_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
    if file_path.suffix.lower() not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only image files are allowed."
        )

    # 경로 조작 방지 (보안)
    try:
        file_path = file_path.resolve()
        base_path = Path(settings.image_base_path).resolve()

        # 파일이 허용된 기본 경로 내에 있는지 확인
        if not str(file_path).startswith(str(base_path)):
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Path resolution error: {str(e)}"
        )

    # 이미지 파일 반환
    return FileResponse(
        path=file_path,
        media_type=f"image/{file_path.suffix[1:]}",
        headers={
            "Cache-Control": "public, max-age=86400",  # 24시간 캐시
            "Content-Disposition": f"inline; filename={filename}"
        }
    )
