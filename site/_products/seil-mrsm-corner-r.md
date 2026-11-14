---
title: MRSm Corner R
subtitle: 인서트 코너 R 자동 측정 모듈 · 버튼 한 번으로 코너 반경(Rε) 측정
category: 머신비전
subcategory: Software
brand: SEIL TECHNO
order: 421
posted: 2026-11-14
published: true
image: /assets/img/software/mrsm-corner-r/main.jpg
summary: 절삭 인서트(CNMG·SNMG 등)의 코너 반경을 역광 실루엣에서 완전 자동으로 측정하는 MRSm 모듈입니다. 측정 영역을 따로 지정할 필요 없이 버튼 한 번이면 약 0.5초 안에 R 값과 OK/NG 판정이 나옵니다.
tags: [자체 개발, 인서트 코너 R 자동 측정, ISO 형번 21종 내장]
keywords: [인서트 코너 R 측정, 코너 반경 측정, 노즈 R 측정, 절삭공구 측정, CNMG, SNMG, DNMG, 인서트 검사 소프트웨어, 현미경 측정 소프트웨어]
highlights:
  - title: 버튼 한 번, 완전 자동
    text: 작업자가 측정 영역(ROI)을 정하지 않습니다. Measure 버튼을 누르면 약 0.3~0.5초 뒤 R 값이 표시되고 아래 측정 목록에 자동으로 기록됩니다.
  - title: 작업자에 따라 달라지지 않는 반복성
    text: 같은 인서트를 5회 반복 측정했을 때 측정값 범위가 약 5 µm로, 3점 수동·엣지 호 측정(37~64 µm)보다 훨씬 좁습니다. 항상 같은 알고리즘으로 계산합니다.
  - title: 오측정 자동 거부
    text: 기하학적 교차 검증(Cross-val)과 R 값 상한 검사로 명백히 잘못된 결과는 출력하지 않고 'No result'로 표시합니다. 피팅 잔차(RMS)와 사용 포인트 수도 함께 보여 줍니다.
  - title: ISO 형번 내장 · OK/NG 판정
    text: CNMG·DNMG·VNMG·SNMG·TNMG·WNMG 21개 형번을 고르면 형상과 명목 R이 자동 입력되고, 허용 오차 기준으로 OK/NG를 판정합니다. 형번 없이 AUTO로도 측정합니다.
shots_desc: 실제 프로그램 화면입니다. (배율 X0.7, 194.053 px/mm, 역광 조명)
shots:
  - {src: /assets/img/software/mrsm-corner-r/main.jpg, title: "코너 R 측정 결과", desc: "피팅된 원(초록)과 접점(주황), 두 직선 엣지(파선)를 영상 위에 겹쳐 보여 줍니다. 왼쪽에 R 측정값·교차 검증 오차·각도·RMS가 표시됩니다.", wide: true}
  - {src: /assets/img/software/mrsm-corner-r/guide-ready.jpg, title: "측정 전 — 가이드 오버레이", desc: "Corner R 탭을 고르면 라이브 화면에 코너 위치(십자)와 직선 엣지·호 가이드가 나타납니다."}
  - {src: /assets/img/software/mrsm-corner-r/measured-1.jpg, title: "반복 측정", desc: "인서트 위치가 바뀌어도 같은 R 값이 나옵니다. 결과는 아래 Measurements 표에 쌓입니다."}
stats:
  title: 반복 측정 비교
  sub: "같은 인서트 코너를 방법별로 5회씩 반복 측정해 측정값 범위(최대 − 최소)를 비교했습니다. (세일테크노 사내 시험, 2026년 11월)"
  items:
    - {num: "~5", unit: "µm", label: "Corner R 자동 측정 — 5회 측정값 범위"}
    - {num: "37~64", unit: "µm", label: "기존 방법(3점 수동 · 엣지 호 24스캔) 범위"}
    - {num: "0.5", unit: "초 이내", label: "버튼을 누른 뒤 결과 표시까지"}
    - {num: "300+", unit: "pts", label: "원 피팅에 쓰는 호(arc) 포인트 수"}
  note: "기존 엣지 호 측정은 밝기 변화가 가장 큰 지점을, Corner R 자동 측정은 실루엣 경계를 기준으로 하므로 절댓값은 수십 µm 다를 수 있습니다. 이는 측정 기준의 차이이며, 비교 항목은 반복 정밀도입니다. 배율을 높이면 반복 측정 범위는 더 좁아집니다."
guide_title: 사용 가이드
guide_tab: 사용 가이드
guide_desc: "측정 원리부터 배치 방법, 옵션, 결과 읽는 법, 측정 절차까지 순서대로 정리했습니다. 그림을 누르면 크게 볼 수 있습니다."
guide:
  - title: "측정 원리"
    text: "카메라 영상에서 인서트 외곽선을 픽셀 단위로 추출한 뒤, 두 직선 엣지를 피팅하고 그 교점(가상 꼭짓점)을 기준으로 호(arc) 구간만 골라냅니다. 골라낸 300~500개 포인트에 RANSAC + 최소제곱 원 피팅을 적용해 R을 계산합니다."
    points:
      - "실루엣 외곽선 추출 → 직선 엣지 피팅 → 호 포인트 필터링 → RANSAC 원 피팅 → 교차 검증 → R 값 출력"
      - "전체 처리 약 0.5초 이내"
      - "교차 검증으로 오측정을 자동으로 걸러 냄"
    images:
      - {src: /assets/img/software/mrsm-corner-r/diagram-flow.png, cap: "측정 알고리즘 처리 흐름"}
  - title: "화면 가이드 오버레이"
    text: "Corner R 탭을 선택하면 라이브 화면에 반투명 배치 가이드가 자동으로 나타납니다. 측정이 끝나면 가이드는 사라지고 측정 결과(원·접점·직선)가 표시됩니다."
    points:
      - "① 십자 — 코너(꼭짓점) 목표 위치. 화면 왼쪽 가운데에 두는 것을 권장"
      - "② 대각선 파선 — 인서트 직선 엣지의 예상 방향. 두 선이 V자로 만나는 곳이 코너"
      - "③ 호 파선 — R nominal을 넣으면 실제 크기로, AUTO에서는 비례 크기로 표시"
    images:
      - {src: /assets/img/software/mrsm-corner-r/guide-ready.jpg, cap: "측정 전 — 가이드 오버레이 표시 중"}
  - title: "인서트 배치 방향"
    text: "인서트 코너가 왼쪽을 향하고, 밝은 배경(역광 광원)이 왼쪽에 오도록 놓습니다. 인서트는 어두운 실루엣으로 보여야 합니다."
    points:
      - "코너가 왼쪽 · 배경이 왼쪽 — 측정 가능"
      - "코너가 오른쪽을 향하면 측정 불가 → 인서트를 돌려 놓기"
      - "양쪽 직선 엣지가 모두 화면 안에 있어야 함 — 한쪽이 잘리면 직선 피팅 실패"
      - "가이드의 V자 꼭짓점(십자)에 코너를 맞추면 안정적으로 측정"
  - title: "측정 옵션"
    text: "Insert 패널에서 형번·형상·명목 R·허용 오차를 정합니다. 옵션을 비워 두고 AUTO로도 측정할 수 있으며, 명목 R을 넣으면 편차(ΔR)와 OK/NG 판정이 켜집니다."
    points:
      - "Designation (ISO) — 형번을 고르면 Shape·R nominal 자동 입력. '— manual —'은 직접 입력"
      - "Shape — AUTO는 영상에서 각도 자동 감지. CNMG 80° · DNMG 55° · VNMG 35° · SNMG 90° · TNMG 60° · WNMG 80° 선택 시 각도 고정"
      - "R nominal (mm) — 입력하면 가이드에 실제 크기로 표시되고 ΔR · OK/NG 활성화"
      - "Tolerance ±mm — |R 측정값 − R nominal| ≤ 허용 오차이면 OK (기본값 ±0.025 mm)"
    images:
      - {src: /assets/img/software/mrsm-corner-r/diagram-options.png, cap: "측정 옵션 패널 — 각 항목의 역할"}
      - {src: /assets/img/software/mrsm-corner-r/shape-menu.jpg, cap: "Shape 목록 — AUTO와 6가지 형상"}
  - title: "등록된 ISO 형번"
    text: "Designation 목록에서 고를 수 있는 형번은 21종입니다. 목록에 없는 형번은 세일테크노에 요청하시면 추가 등록해 드립니다."
    points:
      - "CNMG — 120404 · 120408 · 120412 · 120416 · 160612"
      - "DNMG — 110404 · 110408 · 150604 · 150608 · 150612"
      - "TNMG — 160404 · 160408 · 160412 · 220408"
      - "SNMG — 090308 · 120408 · 120412"
      - "VNMG — 160404 · 160408"
      - "WNMG — 080408 · 080412"
      - "형번 끝 두 자리가 명목 R (예: 08 → 0.8 mm, 12 → 1.2 mm)"
    images:
      - {src: /assets/img/software/mrsm-corner-r/iso-menu.jpg, cap: "Designation (ISO) 형번 목록"}
  - title: "결과 항목 읽는 법"
    text: "R 측정값과 함께 신뢰도를 판단할 수 있는 값들이 표시됩니다. R 값 색은 명목값 미설정이면 파랑, OK면 초록, NG면 빨강입니다."
    points:
      - "R measured — 최종 측정값 (RANSAC 원 피팅 결과)"
      - "ΔR — 명목 R 대비 편차와 OK/NG (명목 R 미입력 시 표시 안 됨)"
      - "Cross-val — 기하학적 교차 검증 오차. 낮을수록 신뢰도 높음, 보통 50 µm 미만이면 양호"
      - "θ measured — 자동 감지한 인서트 각도 (CNMG 약 80°, SNMG 약 90°)"
      - "RMS / Arc pts — 피팅 잔차와 사용 포인트 수. RMS 2 µm 미만, 100 pts 이상이면 신뢰할 수 있는 측정"
    images:
      - {src: /assets/img/software/mrsm-corner-r/diagram-results.png, cap: "결과 패널 각 항목의 의미 (예시: R 1.1897 mm, OK)"}
      - {src: /assets/img/software/mrsm-corner-r/measured-2.jpg, cap: "실제 측정 화면 — R 1.1960 mm, Cross-val 1.93 µm, RMS 0.78 µm / 314 pts"}
  - title: "측정 절차"
    text: "역광 조명과 캘리브레이션만 맞춰 두면, 인서트를 놓고 버튼을 누르는 것으로 측정이 끝납니다."
    points:
      - "1. 역광 조명 설정 — 광원이 인서트 뒤쪽에 오도록, 인서트가 어두운 실루엣으로 보이게"
      - "2. 캘리브레이션 확인 — 화면 오른쪽 위 배율 표시(예: X0.7 / 194.053 px/mm)"
      - "3. 왼쪽 도구 패널에서 Corner R 탭 선택 → 가이드 오버레이 표시"
      - "4. 십자 위치에 절삭 코너가 오도록 인서트 배치 (코너는 왼쪽, 양쪽 직선 엣지는 화면 안)"
      - "5. (선택) Shape · R nominal · Tolerance 설정"
      - "6. Measure 클릭 — 약 0.3~0.5초 후 결과와 측정 오버레이 표시"
      - "7. R 값과 Cross-val · RMS 확인 — 결과는 Measurements 표에 자동 기록"
      - "8. Clear로 초기화 후 다음 코너 측정 (Clear all로 표 전체 초기화)"
    images:
      - {src: /assets/img/software/mrsm-corner-r/measured-1.jpg, cap: "측정 완료 — 원·접점·직선 오버레이와 Measurements 표"}
  - title: "적용 범위와 제한사항"
    text: "역광 실루엣으로 보이는 표준 형상 인서트의 절삭 코너를 대상으로 합니다."
    points:
      - "적용 — 역광 조명의 인서트 실루엣, 절삭 코너(예각), CNMG·SNMG·DNMG 등 표준 형상"
      - "적용 — 배율 X0.7~X2.0 (약 190~580 px/mm), R 0.4~2.4 mm"
      - "제한 — 코너가 오른쪽을 향하면 측정 불가 (인서트를 돌려 놓기)"
      - "제한 — 100° 이상 둔각 코너, 직선 엣지 한쪽이 화면 밖으로 잘린 경우"
      - "제한 — 반사광(위에서 비추는) 조명 조건에서는 사용 불가"
      - "제한 — R 0.2 mm 미만 초미세 코너는 픽셀 해상도 한계로 부정확할 수 있음"
specs:
  - {label: 개발, value: "㈜세일테크노 (자체 개발) — MRSm 측정 모듈"}
  - {label: 측정 대상, value: "절삭 인서트 코너 반경(Rε), 코너 각도"}
  - {label: 측정 방식, value: "역광 실루엣 외곽선 → 직선 엣지 피팅 → 호 포인트 필터링 → RANSAC + 최소제곱 원 피팅"}
  - {label: 측정 시간, value: "약 0.3~0.5초 (버튼 1회)"}
  - {label: 반복성, value: "5회 측정값 범위 약 5 µm (사내 시험, 배율이 높을수록 좁아짐)"}
  - {label: 측정 범위, value: "R 0.4~2.4 mm, 배율 X0.7~X2.0 (약 190~580 px/mm)"}
  - {label: 내장 형상, value: "AUTO, CNMG, DNMG, VNMG, SNMG, TNMG, WNMG"}
  - {label: 내장 형번, value: "ISO 형번 21종 (추가 등록 가능)"}
  - {label: 판정, value: "명목 R 대비 ΔR, 허용 오차 OK/NG (기본 ±0.025 mm)"}
  - {label: 결과 기록, value: "Measurements 표 자동 기록 (R, 각도, 교차 검증, RMS, 포인트 수, 배율)"}
  - {label: 운영 환경, value: "Windows 10 / 11 (64-bit), MRSm v1.0"}
applications: [인서트 코너 R 측정, 절삭공구 입고·출하 검사, 인서트 연삭·재연마 품질 확인, 공구 제조 공정 검사]
---
**MRSm Corner R**은 세일테크노의 현미경 측정 소프트웨어 MRSm에 들어 있는 인서트 코너 R 자동 측정 모듈입니다. 코너 R은 직선과 원호의 경계가 뚜렷하지 않아, 사람이 점을 찍거나 측정 영역을 정하면 그때마다 값이 흔들립니다.

MRSm Corner R은 작업자의 선택 없이 **외곽선 추출 → 직선 엣지 피팅 → 호 구간 선별 → 원 피팅 → 교차 검증**을 항상 같은 순서로 계산합니다. 그래서 누가 측정해도 결과가 같고, 반복 측정 범위가 기존 방법보다 훨씬 좁습니다.

> 측정할 인서트와 사용 중인 현미경·카메라를 알려 주시면 샘플 이미지로 먼저 측정해 보여 드립니다.
