from tourist_attraction import get_tourist_sites, save_tourist_sites_to_db
from food_location import get_Cheongju, get_Chungju  # 음식 데이터 처리 모듈


def get_results():
    """
    관광지 데이터와 음식 데이터 모두를 가져옵니다.
    """
    # 1. 관광지 데이터 가져오기 및 DB 저장
    print("관광지 데이터를 가져오는 중...")
    tourist_sites = get_tourist_sites()
    save_tourist_sites_to_db(tourist_sites)

    # 2. 음식 데이터를 가져오기
    print("청주와 충주의 음식 데이터를 가져오는 중...")
    food_locations_cheongju = get_Cheongju()
    food_locations_chungju = get_Chungju()

    # 모든 데이터를 반환
    return {
        "tourist_sites": tourist_sites,
        "food_locations_cheongju": food_locations_cheongju,
        "food_locations_chungju": food_locations_chungju
    }


if __name__ == "__main__":
    results = get_results()
    print(f"결과: {results}")
