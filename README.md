# ㈜세일테크노 홈페이지 (stvision.co.kr)

## 구조
| 폴더 | 내용 |
|---|---|
| `site/_products/` | 제품 1개 = 파일 1개 |
| `site/_cases/` | 적용사례 1건 = 파일 1개 |
| `site/_data/downloads.yml` | 자료실 목록 |
| `site/assets/` | 사진·영상·자료 파일 |
| `01_시안/` | 홈페이지를 만드는 프로그램 (build_preview.py → publish.py) |
| `.github/workflows/deploy.yml` | 저장하면 자동으로 홈페이지를 다시 만들어 공개 |
| `.pages.yml` | 입력 화면(Pages CMS) 설정 |

## 내용 올리는 방법
1. **입력 화면(Pages CMS)**: app.pagescms.org 에서 GitHub로 로그인 → 이 저장소 선택 → 제품 / 적용사례 / 자료실
2. **GitHub 웹**: 파일을 직접 고치거나 올리기
3. 저장 후 1~2분 뒤 홈페이지에 자동 반영 (진행 상황: 저장소 상단 Actions 탭)

## 지켜야 할 것
- 보안자료·가격표·고객 내부 자료는 올리지 않습니다. (저장소가 공개되어 있습니다)
- 파일 1개는 25MB 이하. 큰 파일은 구글 드라이브 링크로 자료실에 등록합니다.
- 고객사명·사진은 고객 동의를 받은 경우에만 공개합니다.
