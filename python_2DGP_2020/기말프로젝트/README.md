---


---

<h1 id="기말-프로젝트">기말 프로젝트</h1>
<p><strong>20년 2학기 2D게임프로그래밍</strong> 기말 프로젝트입니다.</p>
<h1 id="게임-소개">게임 소개</h1>
<h3 id="제목">제목</h3>
<p>머쉬런(Mushrun)</p>
<h3 id="원-게임에-대한-정보">원 게임에 대한 정보</h3>
<p>기말 프로젝트의 모티브가 되는 게임은 Devsisters가 개발한 <strong>쿠키런</strong>이다.</p>
<p><img src="https://i.ytimg.com/vi/cU1SCXHKmLs/maxresdefault.jpg" width="40%" height="30%" title="px(픽셀) 크기 설정" alt="CookieRun"></p>
<h3 id="게임의-목적과-방법">게임의 목적과 방법</h3>
<p>기말 프로젝트로 만들 '머쉬런’은 끝없이 진행되는 <strong>횡스크롤 러닝 게임</strong>이다. 플레이어는 점프와 슬라이드를 이용해 장애물을 피하고 젤리를 먹어 점수를 올릴 수 있다. 플레이어의 체력이 소진될 때까지 게임은 진행되며 게임이 끝난 시점의 점수를 기록해 순위표를 만들 예정이다.</p>
<h1 id="game-scene">Game scene</h1>
<h3 id="scene-설명">Scene 설명</h3>
<div class="mermaid"><svg xmlns="http://www.w3.org/2000/svg" id="mermaid-svg-aVqjHqvDV7QKFoj7" width="100%" style="max-width: 844.0625px;" viewBox="0 0 844.0625 204"><g transform="translate(-12, -12)"><g class="output"><g class="clusters"></g><g class="edgePaths"><g class="edgePath" style="opacity: 1;"><path class="path" d="M71.203125,114L143.4765625,114L215.75,114" marker-end="url(#arrowhead11433)" style="fill:none"></path><defs><marker id="arrowhead11433" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M284.921875,97.59172060973063L399.9921875,43L549.1953125,43" marker-end="url(#arrowhead11434)" style="fill:none"></path><defs><marker id="arrowhead11434" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M610.3984375,43L715.84375,43L788.03125,68.18194380469829" marker-end="url(#arrowhead11435)" style="fill:none"></path><defs><marker id="arrowhead11435" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M788.03125,88.81805619530171L715.84375,114L579.796875,114L399.9921875,114L284.921875,114" marker-end="url(#arrowhead11436)" style="fill:none"></path><defs><marker id="arrowhead11436" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M609.8841646634615,66L715.84375,147L787.15625,169.0736987563335" marker-end="url(#arrowhead11437)" style="fill:none"></path><defs><marker id="arrowhead11437" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M787.15625,183.43758636573008L715.84375,195L579.796875,195L399.9921875,195L284.921875,132.7193046565045" marker-end="url(#arrowhead11438)" style="fill:none"></path><defs><marker id="arrowhead11438" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g></g><g class="edgeLabels"><g class="edgeLabel" transform="translate(143.4765625,114)" style="opacity: 1;"><g transform="translate(-47.2734375,-13)" class="label"><foreignObject width="94.546875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Press any key</span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(399.9921875,43)" style="opacity: 1;"><g transform="translate(-90.0703125,-13)" class="label"><foreignObject width="180.140625" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Choose character and pet</span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(715.84375,43)" style="opacity: 1;"><g transform="translate(-38.2265625,-13)" class="label"><foreignObject width="76.453125" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Game over</span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(579.796875,114)" style="opacity: 1;"><g transform="translate(-62.9609375,-13)" class="label"><foreignObject width="125.921875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Press retry button</span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(715.84375,147)" style="opacity: 1;"><g transform="translate(-46.3125,-13)" class="label"><foreignObject width="92.625" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Press esc key</span></div></foreignObject></g></g><g class="edgeLabel" transform="translate(579.796875,195)" style="opacity: 1;"><g transform="translate(-64.734375,-13)" class="label"><foreignObject width="129.46875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel">Select retart menu</span></div></foreignObject></g></g></g><g class="nodes"><g class="node" id="A" transform="translate(45.6015625,114)" style="opacity: 1;"><rect rx="0" ry="0" x="-25.6015625" y="-23" width="51.203125" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-15.6015625,-13)"><foreignObject width="31.203125" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Title</div></foreignObject></g></g></g><g class="node" id="B" transform="translate(250.3359375,114)" style="opacity: 1;"><rect rx="0" ry="0" x="-34.5859375" y="-23" width="69.171875" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-24.5859375,-13)"><foreignObject width="49.171875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Setting</div></foreignObject></g></g></g><g class="node" id="C" transform="translate(579.796875,43)" style="opacity: 1;"><rect rx="0" ry="0" x="-30.6015625" y="-23" width="61.203125" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-20.6015625,-13)"><foreignObject width="41.203125" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Game</div></foreignObject></g></g></g><g class="node" id="D" transform="translate(817.609375,78.5)" style="opacity: 1;"><rect rx="0" ry="0" x="-29.578125" y="-23" width="59.15625" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-19.578125,-13)"><foreignObject width="39.15625" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Score</div></foreignObject></g></g></g><g class="node" id="E" transform="translate(817.609375,178.5)" style="opacity: 1;"><rect rx="0" ry="0" x="-30.453125" y="-23" width="60.90625" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-20.453125,-13)"><foreignObject width="40.90625" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Menu</div></foreignObject></g></g></g></g></g></g></svg></div>
<ol>
<li>Title scene:   타이틀 화면을 출력하는 씬이다.</li>
<li>Setting scene: 플레이어가 캐릭터를 선택하는 씬이다.</li>
<li>Game scene:    실제 게임이 이루어지는 씬이다.</li>
<li>Menu scene:    게임 종료, 캐릭터 재선택을 선택하는 씬이다.</li>
<li>Score scene:   자신의 점수와 순위표를 출력하는 씬이다.</li>
</ol>
<h3 id="화면에-표시할-객체들의-목록">화면에 표시할 객체들의 목록</h3>
<ol>
<li>플레이어</li>
<li>펫</li>
<li>젤리</li>
<li>배경화면</li>
<li>플랫폼</li>
<li>점수, 체력 등을 나타내는 UI</li>
</ol>
<h3 id="처리할-이벤트">처리할 이벤트</h3>
<ol>
<li>ESC 버튼: 게임을 정지하고 <strong>메뉴</strong>를 띄운다.</li>
<li>스페이스 버튼: 게임 씬에서 <strong>캐릭터를 점프</strong>하게 한다.</li>
<li>화살표 버튼: 메뉴 창이 팝업 됐을 때에는 위아래 방향키로 메뉴를 선택할 수 있다. 게임 씬에선 아래 화살표로 캐릭터를 <strong>슬라이딩</strong>하게 만든다.</li>
</ol>
<h3 id="다른-scene으로의-이동-조건-및-방법">다른 Scene으로의 이동 조건 및 방법</h3>
<ol>
<li>Title to Setting: 아무 버튼이나 누르면 Setting 씬으로 이동한다.</li>
<li>Setting to Game: 플레이어가 캐릭터와 펫을 선택 완료하면 Game 씬으로 이동한다.</li>
<li>Game to Menu: 플레이어가 esc키를 누르면 Menu 씬으로 이동한다.</li>
<li>Game to Score: 플레이어의 체력이 모두 소진될 시 게임 오버가 되고 Score 씬으로 이동한다.</li>
<li>Menu to Setting: 플레이어가 메뉴에서 캐릭터 재선택을 선택했을 시 Setting 씬으로 이동한다.</li>
<li>Score to Setting: 플레이어가 재시작을 선택했을 시 Setting 씬으로 이동한다.</li>
</ol>
<h1 id="필요한-기술">필요한 기술</h1>
<h2 id="다른-과목에서-배운-기술">다른 과목에서 배운 기술</h2>
<p>1학년 때 배운 기본적인 수학, 물리에 관한 지식이 도움이 될 것 같다.</p>
<h2 id="이-과목에서-배울-것으로-기대되는-기술">이 과목에서 배울 것으로 기대되는 기술</h2>
<p>직접 게임을 만들어 보면서 하나의 게임이 돌아가는 구조를 자세하게 알 수 있을 것 같다.</p>
<h2 id="수업에-다루어-달라고-요청할-기술">수업에 다루어 달라고 요청할 기술</h2>
<p>프로그래밍도 프로그래밍이지만 이미지 리소스를 다루기가 적잖이 까다롭다. 어디서 배운 적도 없을 뿐더러 구글에 쳐봐도 죄다 유니티를 활용한 . <strong>스프라이트 시트를 효과적으로 다룰 수 있는 기술</strong>을 배우고 싶다.</p>

