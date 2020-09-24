# 기말 프로젝트

**20년 2학기 2D게임프로그래밍** 기말 프로젝트입니다.


# 게임 소개

### 제목
 머쉬런(Mushrun)

### 원 게임에 대한 정보
 기말 프로젝트의 모티브가 되는 게임은 Devsisters가 개발한 **쿠키런**이다.

<img src="https://i.ytimg.com/vi/cU1SCXHKmLs/maxresdefault.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="CookieRun"></img>

### 게임의 목적과 방법
 기말 프로젝트로 만들 '머쉬런'은 끝없이 진행되는 횡스크롤 러닝 게임이다. 플레이어는 점프와 슬라이드를 이용해 장애물을 피하고 젤리를 먹어 점수를 올릴 수 있다. 플레이어의 체력이 소진될 때까지 게임은 진행되며 게임이 끝난 시점의 점수를 기록해 순위표를 만들 예정이다.

# Game scene

### Scene 설명
graph LR
A[Title] -- Press any key --> B[Setting]
B -- Choose character and pet --> C[Game]
C -- Select menu --> B
C -- Game over--> D[Score]
D -- Press retry button --> B


### 화면에 표시할 객체들의 목록

### 처리할 이벤트
1. ESC 버튼: 게임을 정지하고 **메뉴**를 띄운다.
1. 스페이스 버튼: 게임 씬에서 **캐릭터를 점프**하게 한다.
1. 화살표 버튼: 메뉴 창이 팝업 됐을 때에는 위아래 방향키로 메뉴를 선택할 수 있다. 게임 씬에선 아래 화살표로 캐릭터를 **슬라이딩**하게 만든다.

### 다른 Scene으로의 이동 조건 및 방법


# 필요한 기술

## 다른 과목에서 배운 기술

## 이 과목에서 배울 것으로 기대되는 기술

## 수업에 다루어 달라고 요청할 기술
