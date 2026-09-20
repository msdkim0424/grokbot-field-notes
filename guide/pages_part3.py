# -*- coding: utf-8 -*-
# Pages 17 to 24 for Korean Grok Bot Guide
from pages_part1 import get_header, get_footer

def render_page_17():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">14 · CASE STUDY</div>
    <h1 class="page-title">Thursday Arena, 72시간 만에 완성된 게임</h1>
    <p class="page-intro">
      공개 마켓플레이스에 등록된 실제 봇들을 캐릭터로 소환하여 희귀도, 생성된 아바타, 스탯, 고유 능력을 부여한 오토배틀러 게임입니다. 단 세 명의 인원과 봇 팀이 개발하여, 3일차 오전 10시 프로필 사진도 없는 신규 X 계정의 트윗 하나로 공식 출시되었습니다.
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">어떻게 빌드되었는가</div>
        <ul class="custom-bullets">
          <li><strong>프로토타입 우선</strong> — 바닐라 HTML/CSS/JS, 인메모리 상태, DB 없음, 인증 없음. 유일한 질문: "이 게임 루프가 과연 재미있는가?"</li>
          <li>루프의 재미가 검증된 후 React/Next.js로 전면 재작성, 클라이언트와 서버 분리.</li>
          <li>백엔드는 Vercel Serverless 위의 Go, 데이터베이스는 PlanetScale, 인증은 Clerk (Sign in with X), 네트워크 경계 검증은 Zod.</li>
          <li>카드 아트는 Grok Imagine 생성; 캐릭터는 스프라이트 대신 코드로 제어하여 상태를 프로그래밍 방식으로 전환.</li>
          <li>초반에는 테스트 코드를 의도적으로 삭제 — "에이전트들은 일반적으로 테스트를 썩 잘 짜지 못합니다" — 코드 품질 단계는 후순위로 미룸.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">성과를 가른 핵심 설계 결정들</div>
        <ul class="custom-bullets">
          <li><strong>Pay-to-Win 전면 배제.</strong> 수없이 논의되었으나 단호히 거절됨. 광고, 스폰서 카드, 굿즈가 채택된 수익 모델.</li>
          <li><strong>가차 없는 기능 쳐내기 (Ruthless cutting).</strong> 가위바위보 상성, 복잡한 스탯 블록, 다중 전장 기획을 전부 잘라내고 가장 깔끔한 단일 루프만 남김.</li>
          <li><strong>복잡한 숫자의 은닉.</strong> 날것의 ELO 수치 대신 티어로 대체; 구체적 스탯 대신 상대적 강도로 시각화.</li>
          <li>실시간 치팅 시연 후 전면적인 <strong>서버 권한화 (Server Authority)</strong> 단행.</li>
          <li>인간뿐만 아니라 AI 에이전트도 읽을 수 있도록 기획된 <code>/rules</code> 페이지 구축.</li>
        </ul>
      </div>
    </div>

    <div class="section-label dark">출시 당일 주요 지표</div>
    <div class="grid-4col" style="margin-bottom: 7pt;">
      <div class="stat-card">
        <div class="stat-val">170</div>
        <div class="stat-desc">3일차 방송 시작 전 밤사이에 머지된 PR 수</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">1,908</div>
        <div class="stat-desc">출시 첫 1시간 동안 플레이된 경기 수 (당일 최고치)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">~6,000</div>
        <div class="stat-desc">약 2,000명의 유저가 플레이한 총 공개 매치 수</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">#1</div>
        <div class="stat-desc">출시 당일 구글 검색 결과에서 게임 이름으로 1위 등극</div>
      </div>
    </div>

    <div class="footnote">
      *피드백은 세 가지 채널을 통해 하나의 슬랙 방으로 모였습니다: 인증 기반 인앱 폼, 음성 에이전트 기반 전화번호, 그리고 X 멘션. 이 채널들의 피드백을 분류하고, 버그를 재현하며, 노션 티켓으로 자동 발행하는 작업은 출시 당일 오후에 전면 자동화되었습니다.
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">실제 퍼널 데이터가 말해주는 진실</div>
        <p class="callout-text">
          연습 모드 플레이어의 약 8%가 정식 계정 로그인으로 전환되었으며, 트래픽은 모바일과 데스크톱이 거의 5:5로 양분되었습니다(iOS 약 44%). 접수된 피드백 중 가장 큰 비중을 차지한 것은 모바일 레이아웃 이슈였습니다 — <strong>전체 피드백의 71%가 버그 리포트였고, 칭찬은 16%에 불과했습니다.</strong> 팀은 이 모바일 피드백에 대응해 당일 오후 즉시 반응형 대응 패치를 배포했습니다. 초기 유입의 거의 전부는 라이브 스트리밍 시청자로부터 나왔으며, 이는 모든 수치에 감안해야 할 전제조건입니다.
        </p>
      </div>
    </div>
    {get_footer(17)}
  </div>
    """

def render_page_18():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">15 · THE ROSTER</div>
    <h1 class="page-title">팀에 투입된 모든 봇들의 명단</h1>
    <p class="page-intro">
      Thursday Arena 제작에 실제로 투입된 봇 팀의 전체 명단입니다. 하나의 모범 템플릿으로 읽어볼 가치가 있습니다: <strong>코드를 직접 작성하는 봇은 극소수이며, 대다수의 봇이 검증, 라우팅, 피드백 수집을 위해 존재한다는 점</strong>에 주목하십시오.
    </p>

    <div class="grid-2col" style="gap:7pt; margin-bottom:7pt;">
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Dr. Eggbot <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 메타 / 봇 팩토리</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">다른 모든 봇을 생성하고 감사. 디스크립션을 작성하고, 이름을 짓고, "우리 병목이 어디지?"에 답함. 3일간 가장 많이 쓰인 봇.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Steve <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 비서실장 / 오케스트레이터</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">모든 업무가 통과하는 관문. 팀원들이 흔한 "Chief of Staff"라는 이름을 서로 놀린 후 친근한 이름으로 개명.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Cupcake Eng <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 엔지니어링 오케스트레이터</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">포테이토 모드와 클라우드 에이전트를 가동하고 결과를 감독 및 검증하여 엔지니어링 결과물을 총괄 책임짐.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Bake <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 파운딩 엔지니어</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">PR 활동을 모니터링하고 머지하며, 버그 수정을 위해 클라우드 에이전트를 소환. 데모 도중 음성으로 호출되어 실시간 머지 수행.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Chrome / Play <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 플레이테스터</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">CI 테스트를 통과한 PR을 감시하고, 코드가 머지되기 전에 실제 브라우저로 게임 전체를 직접 플레이하여 검증.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Crumble <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 버그 분류 (Triage)</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">플레이테스터 봇과 협력하여 유저가 보고한 버그를 직접 재현하고, 확인된 이슈만 노션에 정식 등록.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Hashbrown <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 검증관 (Validation)</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">오토파일럿이 수정 작업에 들어가기 전에 Crumble의 버그 분류가 정확한지 재확인하는, '검증자를 검증하는 봇'.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Comment Sicko <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 코드 위생 관리</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">불필요한 코드 주석을 삭제. 에이전트들이 근본 원인을 고치는 대신 변명을 주석으로 남기는 악습을 막아 유지보수성을 지킴.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Whisk · Crit <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 게임 디자인 & 비평</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">디자이너 겸 비평가. 출시 당일 아침 "게임이 너무 어렵다"는 Crit의 혹평이 출시 직전 밸런스 패치를 이끌어냄.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Glow · Tone <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 3D & 사운드</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">프론트엔드 애니메이션 프로토타이핑, Strudel과 Suno를 활용한 배경음악 작곡 후 팀이 들을 수 있도록 노션에 업로드.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Ping <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 슬랙 리스너</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">슬랙의 @멘션을 감시하고 진행 상황을 노션 보드에 실시간 기록. 두 사람이 각자 따로 만들었는데 에그봇이 똑같이 지어준 이름.</div>
      </div>
      <div class="card" style="padding:6.5pt 9pt;">
        <div class="card-title" style="font-size:8.8pt;">Data Scientist <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 데이터 리포팅</span></div>
        <div class="card-body" style="font-size:7.6pt; line-height:1.35;">가입자 수, 기능 사용량, 버그 리포트 대시보드를 정기 생성. 출시 당일에는 15분 간격으로 모니터링 보고.</div>
      </div>
    </div>

    <div class="card" style="padding:6.5pt 9pt; margin-bottom:6pt;">
      <div class="card-title" style="font-size:8.8pt;">Vincent · Cerebro <span style="font-size:7.2pt; color:#e4402e; font-weight:600;">· 그로스 마케팅</span></div>
      <div class="card-body" style="font-size:7.6pt; line-height:1.35;">노션 플레이북에 우선순위별 그로스 아이디어를 기록하고, FindMyICP 스킬을 통해 아웃바운드 타깃 파이프라인 리서치 수행.</div>
    </div>

    <div class="footnote">
      *참고로 팀의 명명 규칙은 전부 감자(Potato)나 베이킹(Baking) 테마였으며, 머지된 PR은 내부적으로 "MASH"라고 불렀습니다. 닥터 에그봇과의 작명 세션에서 시작된 유행어가 실제 노션 프로세스 언어로 정착된 것입니다. 유치해 보이지만 팀이 작업에 대해 훨씬 즐겁게 소통하도록 만들었습니다.
    </div>
    {get_footer(18)}
  </div>
    """

def render_page_19():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">16 · FROM THE FIELD</div>
    <h1 class="page-title">실무 현장의 6가지 봇 조합</h1>
    <p class="page-intro">
      3일간 진행된 실무 워크숍 세션들은 가장 직접적으로 복사해 쓸 수 있는 보물창고였습니다. 각 발표자가 실제로 운영하고 있는 현장 구성입니다.
    </p>

    <div class="card" style="margin-bottom: 9pt;">
      <div class="card-title">포스트세일즈 (Post-sales)</div>
      <div class="card-subtitle">블레이크(Blake) · AI 배포 매니저 (AI Deployment Manager)</div>
      <p style="font-size:8.1pt; font-weight:600; color:#111; margin-bottom:5pt;">
        "거스(Gus)는 제 최고의 친구입니다." 블레이크는 단 하나의 총괄 봇과만 대화하며, 그 아래 15~20명의 전문가 봇이 중간 관리자 없이 평평하게 일합니다.
      </p>
      <div class="grid-2col" style="margin-bottom:0; gap:8pt;">
        <div style="background:#fff; border-radius:6px; padding:7pt 9pt;">
          <div style="font-size:7.6pt; font-weight:700; color:#e4402e; margin-bottom:3pt;">팀 구성 (The Team)</div>
          <ul class="custom-bullets" style="font-size:7.8pt;">
            <li><strong>Gus</strong> — 비서실장이자 유일한 소통 창구</li>
            <li><strong>Frankie</strong> — 미팅 후속 조치(Follow-up) 전담</li>
            <li><strong>Wally</strong> — 타깃 청중별 보이스와 톤 조율</li>
            <li><strong>Trudy</strong> — 내부 지식 및 진실의 단일 출처</li>
            <li>고객 계정당 1개의 전담 봇이 해당 고객의 전체 컨텍스트를 완벽히 보유</li>
          </ul>
        </div>
        <div style="background:#fff; border-radius:6px; padding:7pt 9pt;">
          <div style="font-size:7.6pt; font-weight:700; color:#e4402e; margin-bottom:3pt;">핵심 업무 습관 (The Habits)</div>
          <ul class="custom-bullets" style="font-size:7.8pt;">
            <li>"Harbor 고객 건 어디까지 진행됐지?"라고 물으면 리스크, 블로커, 열린 약속, 다음 액션 아이템 — 그리고 필수 우주 유머를 함께 반환.</li>
            <li>주간 자기개선 스캔: 자동화할 수 있는 작업을 감사하고, 봇 초안과 블레이크의 최종본 diff를 비교해 봇의 말투를 교정.</li>
            <li>주당 제안 건수를 최대 1개로 제한 — 스팸 방지.</li>
          </ul>
        </div>
      </div>
      <p style="font-size:7.6pt; color:#666; margin-top:5pt; font-style:italic;">
        “여러분의 Grok Bot을 가로막고 있는 유일한 것은, 무엇이 실제로 가능한지에 대한 여러분 자신의 상상력 한계입니다.”
      </p>
    </div>

    <div class="card">
      <div class="card-title">마케팅 (Marketing)</div>
      <div class="card-subtitle">조시 킴(Josh Kim) · 6인조 캠페인 봇 팀</div>
      <p style="font-size:8.1pt; font-weight:600; color:#111; margin-bottom:5pt;">
        마지막에 채용된 봇이 앞선 다른 봇들을 자동화하는 구조: 시장 조사 → 프로덕트 마케터 → 웹사이트 운영 → 퍼포먼스 마케터 → 마케팅 분석 봇. 그리고 6번째 봇인 프로젝트 매니저가 전체 캠페인을 엔드투엔드로 지휘합니다.
      </p>
      <div class="grid-2col" style="margin-bottom:0; gap:8pt;">
        <div style="background:#fff; border-radius:6px; padding:7pt 9pt;">
          <div style="font-size:7.6pt; font-weight:700; color:#e4402e; margin-bottom:3pt;">역할 정의 노하우</div>
          <ul class="custom-bullets" style="font-size:7.8pt;">
            <li>"채용 공고의 직무 기술서를 작성하는 것과 거의 같습니다" — 봇마다 철저하게 분리된 전용 스윔레인 부여.</li>
            <li>포지셔닝 기획서는 실제 동료와 검토하듯 구글 닥스 댓글 피드백 루프를 거쳐 완성.</li>
          </ul>
        </div>
        <div style="background:#fff; border-radius:6px; padding:7pt 9pt;">
          <div style="font-size:7.6pt; font-weight:700; color:#e4402e; margin-bottom:3pt;">조시의 실전 조언</div>
          <ul class="custom-bullets" style="font-size:7.8pt;">
            <li>슬랙과 이메일을 초기에 연결한 뒤 "나를 위해 무엇을 해줄 수 있니?"라고 물어보십시오.</li>
            <li>"당신의 봇에 투자하십시오" — 피드백과 컨텍스트는 실제 동료와 마찬가지로 복리로 쌓여갑니다.</li>
          </ul>
        </div>
      </div>
    </div>
    {get_footer(19)}
  </div>
    """

def render_page_20():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">16 · FROM THE FIELD, CONTINUED</div>
    <h1 class="page-title">영업, 고객지원, 아웃바운드, 개인 생산성</h1>

    <div class="card" style="margin-bottom: 7pt; padding:8pt 10pt;">
      <div class="card-title" style="font-size:9pt;">영업 (Sales) <span style="font-size:7.5pt; color:#666; font-weight:normal;">· 크리스타(Krista, AE)</span></div>
      <div class="card-body" style="font-size:7.8pt; line-height:1.4;">
        <p><strong>복잡한 툴 더미를 관통하는 오케스트레이션 레이어:</strong> Olive(비서실장), PG(아웃바운드 발굴), Echo(Gong과 Granola 트랜스크립트 기반 실시간 미팅 덱 큐레이션), 고객 전문가 및 엔지니어 봇. Notion을 마스터 레코드로 삼고 Salesforce, Slack, Databricks를 가로지름 — "데이터를 한곳에 깔끔하게 유지하는 회사는 세상에 없습니다."</p>
        <p><strong>차이를 만든 요점:</strong> 자신의 센트(Sent) 메일함, 슬랙, X 활동 내역으로 봇을 학습시켜 뻔한 AI 말투를 완벽히 제거. 매일 쓰는 도구부터 연결하고, "웹세미나 대신 시청하고 이메일 초안 작성해 놔"처럼 단순 리서처가 아닌 직접 행동하는 실행자(Doer)로 대우.</p>
      </div>
    </div>

    <div class="card" style="margin-bottom: 7pt; padding:8pt 10pt;">
      <div class="card-title" style="font-size:9pt;">고객 지원 (Support) <span style="font-size:7.5pt; color:#666; font-weight:normal;">· 데이비드(David, User Ops)</span></div>
      <div class="card-body" style="font-size:7.8pt; line-height:1.4;">
        <p><strong>4개의 봇과 정량 평가(Evals) 테이블:</strong> Build(인프라), Reply(티켓 및 슬랙 응대), Alert(이탈 위험 및 계정 잠김 감지), Tune(자기 개선 및 지식창고 업데이트). 티켓 시스템, Stripe, Notion, Slack을 실시간 연동: 단순 리셋 자동 처리, 복잡한 SSO 장애는 낮은 신뢰도 경고와 함께 사람에게 안전하게 에스컬레이션, 환불 정책에 따른 정당한 거절, 지식창고 공백 식별 후 사람 승인 요청.</p>
        <p><strong>인프라 및 가드레일:</strong> 평가 실행 결과 테이블과 실행별 상세 추적(Trace) 테이블 분리. PR 브랜치 단위 평가 실행. 비기술자를 위해 날것의 설정 대신 템플릿을 제공하고, 지식창고 수정은 코드 오너와의 PR 리뷰를 거치도록 하여 git 프리미티브를 안전장치로 재활용.</p>
      </div>
    </div>

    <div class="card" style="padding:8pt 10pt;">
      <div class="card-title" style="font-size:9pt;">아웃바운드 및 개인 생산성 <span style="font-size:7.5pt; color:#666; font-weight:normal;">· 사이먼(SDR) & 카렌 청(크리에이터)</span></div>
      <div class="card-body" style="font-size:7.8pt; line-height:1.4;">
        <p><strong>사이먼의 아웃바운드 군단:</strong> 비서실장, Shakespeare(이메일 톤앤매너 전담), 저비용 군단 봇들을 지휘하는 웹 검색 봇, 고객 봇 — 매일 50개 신규 리드 발굴, 아침마다 상위 5개 집중 공략. "단 하나의 이메일도 템플릿처럼 보여서는 안 됩니다." 기능별 색상 코딩.</p>
        <p><strong>카렌 청의 소싱 규칙:</strong> 극단적으로 단순하고 지루한 단일 목적 봇 12개 운영 — 택배 추적, 재입고 알림, 그리고 집안 와이파이에서 프린터를 알아서 찾아 아침 뉴스를 자동 인쇄하는 모닝 페이퍼 봇. "일상에서 느끼는 문제나 불편을 찾아서, 그냥 해결해 버리세요."</p>
        <p style="font-style:italic; color:#e4402e; font-weight:600; margin-top:4pt;">“이제는 바이브 코딩(Vibe Coding)의 시대가 아닙니다. 그냥 바이브(Vibing) 그 자체입니다.”</p>
      </div>
    </div>
    {get_footer(20)}
  </div>
    """

def render_page_21():
    fails = [
        ("에이전트가 자신만의 규칙에 과적합됨", "Day 2", 
         "한 번의 장애를 겪은 후 작성된 봇 디스크립션이 그 사건을 영구적인 정체성으로 하드코딩함.",
         "실패 세션으로부터 규칙을 만들 때는 사건의 스토리를 제거하고 일반 원칙만 남겨라."),
        ("쉬머(Shimmer) 이펙트가 카드 전체를 뒤덮음", "Day 2",
         "희귀도를 나타내는 CSS 반짝임 효과가 너무 과하게 적용되어 모든 카드가 똑같아 보임. 봇이 목적이 아니라 효과 자체에만 매몰됨.",
         "시각적 기교가 아니라 차별화된 결과 목적을 명시하라."),
        ("실제 랜딩 페이지에 가짜 데이터가 노출됨", "Day 2",
         "에이전트가 실제 마켓플레이스를 조회하는 대신 그럴듯한 가짜 예시 봇을 날조하고 내부 프로토타이핑 용어를 카피에 유출시킴.",
         "신뢰할 수 있는 데이터 출처를 지정하고 '실제로 직접 찾아볼 것'을 명시하라."),
        ("3D가 아닌 2.5D 프로토타입 생성", "Day 2",
         "3D 애니메이션을 요구받았으나 3D 라이브러리를 쓰라는 지시가 없었기에 2.5D를 만들어냄.",
         "잘 알려진 라이브러리가 존재하는 작업이라면 라이브러리 이름을 명시하라."),
        ("개발자 도구를 통한 실시간 치팅", "Day 2",
         "게임 로직이 클라이언트에 남아있어 브라우저 콘솔 창에서 스탯을 실시간으로 조작함.",
         "경쟁이 있는 모든 기능은 서버 권한이어야 하며, 피처 플래그는 보안이 아니다."),
        ("봇이 팀의 배포 정책을 무시함", "Day 1",
         "팀이 main 브랜치에 직접 머지하기로 합의한 단계에서 봇이 멋대로 PR을 열어버림.",
         "말하지 않은 암묵적 규칙은 규칙이 아니다. 봇이 읽을 수 있는 곳에 명문화하라."),
        ("VM에서 로그인 세션이 끊김", "Day 2",
         "로컬 브라우저와 달리 VM 브라우저 세션이 자꾸 풀려 카렌 청의 자동화가 중단됨.",
         "무인 자동화가 필요한 작업에는 브라우저 세션보다 커넥터(API/MCP)를 우선하라."),
        ("팩토리가 프로덕션 서버를 다운시킴", "Day 3",
         "자율 버그 수정 루프가 잘못된 SQL 쿼리를 날려 실시간 게임 서버를 마비시킴.",
         "아무리 루프가 뛰어나도 마이그레이션과 프로덕션 배포에는 사람의 승인 관문을 유지하라."),
        ("화면에 실제 라이브 API 토큰 노출", "Day 3",
         "몇 초 만에 감지되어 폐기되었으나 방송 화면에 노출됨.",
         "시크릿 관리에서 가장 취약한 연결고리는 보안 볼트가 아니라 인간이다."),
        ("출시 직후 피드백 파이프라인에 스팸 폭탄", "Day 3",
         "출시 몇 시간 만에 발생. 20자 최소 길이, 욕설 필터링, 살균, 모델 가드, 레이트 리밋을 사후에 급조해야 했음.",
         "폼을 배포할 때 모더레이션(검증) 로직을 사후가 아니라 반드시 함께 배포하라."),
    ]

    items_html = ""
    for title, day, desc, rule in fails:
        items_html += f"""
      <div class="fail-item">
        <div class="fail-head">
          <span>{title}</span>
          <span class="fail-day">{day}</span>
        </div>
        <div class="fail-desc">{desc}</div>
        <div class="fail-rule">규칙: {rule}</div>
      </div>
        """

    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">17 · FAILURE LOG</div>
    <h1 class="page-title">라이브 방송 중에 터진 사고들</h1>
    <p class="page-intro">
      편집되지 않은 생방송은 잔인할 만큼 정직합니다. 수많은 시청자가 지켜보는 가운데 실제로 발생했던 실패들과, 그 실패가 만들어낸 영구적인 원칙들입니다.
    </p>

    <div style="margin-bottom:auto;">
      {items_html}
    </div>
    {get_footer(21)}
  </div>
    """

def render_page_22():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">18 · LIMITS AND ROADMAP</div>
    <h1 class="page-title">아직 동작하지 않는 것들</h1>
    <p class="page-intro">
      생방송 중, 주로 Q&A 세션에서 가감 없이 솔직하게 밝혀진 내용들입니다. 아직 존재하지도 않는 기능 위에 헛된 워크플로우를 설계하는 우를 범하지 않기 위해 반드시 알아두어야 합니다.
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">현재의 명확한 기술적 한계</div>
        <ul class="custom-bullets">
          <li><strong>오직 Linux만 지원.</strong> Linux와 호환되지 않거나 MCP로 노출되지 않는 도구는 절대 사용할 수 없습니다 (Q&A에서 단호하게 "No"로 답변).</li>
          <li><strong>캡차(CAPTCHA)가 봇을 차단함.</strong> 마땅한 범용 우회책이 없으며, 감지를 회피하려 애쓰기보다 봇이 가지 말아야 할 사이트를 차단하는 것이 공식 권장사항입니다.</li>
          <li><strong>계정 간(Cross-account) 봇 메시징 불가.</strong> 내 봇이 다른 사용자의 봇과 직접 대화할 수 없습니다. "매우 멋진 유즈케이스이며 기대하고 있지만" 현재는 미지원입니다.</li>
          <li><strong>VM 세션 만료 문제.</strong> 브라우저 로그인이 로컬 세션과 무관하게 주기적으로 만료되어 무인 자동화가 중단될 수 있습니다.</li>
          <li><strong>타 에이전트 스택에서의 마이그레이션 경로 부재.</strong> 템플릿을 불러오거나 기존 컨텍스트를 지정하는 것 외에 공식적인 마이그레이션 도구는 없습니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">곧 출시될 것으로 예고된 기능들</div>
        <ul class="custom-bullets">
          <li><strong>양방향 음성 모드 (Two-way voice mode)</strong> — 3일차 방송에서 실시간 공개되었으며 순차 롤아웃 예정. 음성 통화로 봇에게 PR 검토 및 머지를 지시하는 시연 완료.</li>
          <li><strong>멀티플레이어 (Multiplayer)</strong> — 사람과 여러 봇이 한 대화방에 참여. 현재는 슬랙에서 봇을 @태그하는 방식으로만 가능. 방송 중 가장 많은 요청을 받은 기능.</li>
          <li><strong>다중 머신 관리 (Multi-machine)</strong> — 여러 VM을 동시에 다룰 때 봇이 혼란을 겪는 문제로, 집중적으로 개선 작업 진행 중.</li>
          <li><strong>직무 기반 맞춤형 온보딩</strong> — 신규 유저에게 직무를 묻고 그에 맞는 맞춤형 스타터 템플릿 세트를 제공.</li>
          <li><strong>컴퓨터 유즈 속도 개선</strong> — "가장 뜨거운 관심사"로, 향후 몇 주에 걸쳐 비약적인 속도 개선이 예정되어 있음.</li>
        </ul>
      </div>
    </div>

    <div class="footnote">
      *수치와 기능은 스트리밍 당시 기준이며 지속적으로 업데이트됩니다. 한계 섹션은 불변의 스펙이 아니라 현재의 윤곽으로 받아들이고, 중요한 의사결정 전 최신 공식 문서를 반드시 확인하십시오.
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">아무도 뾰족한 답을 내놓지 못한 근본적 난제</div>
        <p class="callout-text">
          <strong>결정론성(Determinism).</strong> LLM 모델은 근본적으로 비결정론적이며, 이는 봇이 일관된 정책을 집행해야 하는 순간 치명적인 문제가 됩니다. 제시된 해결책은 마법 같은 프롬프트가 아니라 구조적 접근이었습니다: 봇에게 코드(의사결정 트리나 검증 함수)를 직접 작성하게 하고, 정책 판단이 필요할 때마다 매번 새롭게 추론하는 대신 해당 코드를 호출하게 만드는 것입니다. 이는 검증 CLI의 철학과 일맥상통합니다: 같은 질문에 언제나 같은 답이 나와야 하는 곳이라면, 주관적 판단을 결정론적 도구로 대체하십시오.
        </p>
      </div>
    </div>
    {get_footer(22)}
  </div>
    """

def render_page_23():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">19 · THE RETROSPECTIVE</div>
    <h1 class="page-title">스트리밍 말미에 인정한 솔직한 이야기</h1>
    <p class="page-intro">
      3일차 마지막 30분은 72시간 전체 스트리밍 통틀어 가장 값진 시간이었습니다. 팀이 화려한 데모를 멈추고, 자신들이 무엇을 겪었는지 냉정하게 평가하기 시작했기 때문입니다.
    </p>

    <div class="quote-box">
      <p class="quote-text">“아무리 무제한의 AI 역량을 쥐고 있다 한들, 무언가를 만들 때 가장 어려운 부분은 여전히 ‘사람들의 관심을 이끌어내는 일’입니다.”</p>
      <p class="quote-author">로샨(Roshan) · 마무리 회고 세션</p>
    </div>

    <div class="section-label">팀이 도출한 5가지 핵심 결론</div>
    <div style="margin-bottom: 8pt;">
      <div class="num-item" style="padding:4.5pt 0;">
        <div class="num-badge">1</div>
        <div class="num-content"><strong>배포(유통) 파워가 유일한 성공 이유였다.</strong> 제품 자체의 본질적 매력 때문이 아니라, 실시간 라이브 스트리밍의 화제성 덕분에 유저 유입이 일어났습니다. 14장의 모든 성공 지표에는 이 전제조건이 붙습니다.</div>
      </div>
      <div class="num-item" style="padding:4.5pt 0;">
        <div class="num-badge">2</div>
        <div class="num-content"><strong>이미 잘 알고 있는 영역에서 비즈니스를 시작하라.</strong> "모델을 잘 구슬려 돈을 벌어보겠다"는 순진한 접근은 처참히 실패했습니다. 하루 종일 돌아간 전담 수익화 에이전트의 매출은 정확히 $0였습니다.</div>
      </div>
      <div class="num-item" style="padding:4.5pt 0;">
        <div class="num-badge">3</div>
        <div class="num-content"><strong>아이디어에 합의하는 것이 제품을 만드는 것보다 훨씬 어렵다.</strong> 첫날 하루 종일 4번의 피벗을 거치며 완성된 제품은 0개였습니다. 개발팀의 발목을 잡은 것은 코딩 소프트웨어가 아니었습니다.</div>
      </div>
      <div class="num-item" style="padding:4.5pt 0;">
        <div class="num-badge">4</div>
        <div class="num-content"><strong>절제(Restraint)는 이제 필수적인 엔지니어링 역량이다.</strong> 로렌: "이제는 누구나 무엇이든 만들 수 있습니다 — 아무도 안 쓸 100만 개 기능의 조잡한 제품까지도요. 이제는 무엇을 만들지 않을지 절제하는 규율이 필수입니다." 수많은 게임 메커니즘을 과감히 쳐냈기에 비로소 출시할 수 있었습니다.</div>
      </div>
      <div class="num-item" style="padding:4.5pt 0;">
        <div class="num-badge">5</div>
        <div class="num-content"><strong>문제 발견은 온전히 인간의 몫으로 남는다.</strong> "인간인 당신이 직접 현장으로 나가 유기적으로 진짜 문제들을 발견해야 합니다. 일단 해결책을 찾아내고 나면, 그것을 봇으로 만들어 영원히 자율 실행되게 둘 수 있습니다."</div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">봇들이 진정으로 탁월했던 영역</div>
        <ul class="custom-bullets">
          <li>팀원 누구도 몰랐던 도메인의 지식 공백 메우기</li>
          <li>사람이 하기 싫어하는 반복적이고 지루한 검증 작업</li>
          <li>인간 두뇌 용량을 초과하는 3일치 프로젝트 맥락 유지</li>
          <li>말로 던진 아이디어를 정렬된 목록으로 즉각 변환</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">여전히 인간의 몫으로 남은 영역</div>
        <ul class="custom-bullets">
          <li>애초에 무엇이 만들 가치가 있는지를 결정하는 일</li>
          <li>새로운 기능 추가 요구에 단호하게 "No"라고 거절하는 일</li>
          <li>게임이 아직 재미없다는 사실을 본능적으로 알아차리는 감각</li>
          <li>인간 대 인간의 신뢰 구축, 관계 형성, 모호한 정성적 판단</li>
        </ul>
      </div>
    </div>

    <div class="footnote">
      *훔쳐 올 만한 가치가 있는 로샨의 셀프 체크 질문: 주기적으로 "내가 지금 루프에 너무 깊이 개입해 있는가? 이 과정을 어떻게 더 자율화할 수 있을까?"라고 자문하십시오 — 그리고 봇에게 이 질문을 주기적으로 던지는 루틴을 걸어두십시오.
    </div>
    {get_footer(23)}
  </div>
    """

def render_page_24():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">20 · START HERE</div>
    <h1 class="page-title">첫 번째 주 실천 체크리스트</h1>
    <p class="page-intro">
      앞선 단계가 다음 단계를 더 쉽고 저렴하게 만들도록 순서대로 정렬되었습니다. 무엇이 가장 중요하냐는 질문에 로렌이 내놓은 우선순위는 일반적인 예상을 깨뜨렸습니다: <strong>"Grok Bot에서 가장 중요한 것은 봇을 세팅하는 게 아닙니다. 이미 쓰고 있는 다양한 도구와 플러그인을 연결하는 것입니다."</strong>
    </p>

    <div style="margin-bottom: 7pt;">
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">1</div>
        <div class="num-content"><strong>매일 쓰는 기존 툴 스택부터 연결하라.</strong> 봇을 만들기 전 먼저 하십시오. Slack, 이메일, 캘린더, 이슈 트래커, 코드 저장소. 커넥터는 속도, 비용, 신뢰성 모든 면에서 브라우저를 압도합니다.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">2</div>
        <div class="num-content"><strong>15분짜리 음성 메모를 녹음하라.</strong> 내가 누구인지, 내 업무가 무엇인지, 지금 어디가 고장 나 있고 무엇을 자동화하고 싶은지. 그 트랜스크립트를 첫 봇에게 던지고 시스템 설계를 맡기십시오.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">3</div>
        <div class="num-content"><strong>하루 중 가장 짜증 나는 작업 하나를 골라라.</strong> 암리타와 카렌 청의 공통 조언: 가장 화려해 보이는 일이 아니라, 가장 짜증 나고 귀찮은 작업부터 고르십시오.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">4</div>
        <div class="num-content"><strong>단 하나의 좁은 전문가 봇을 만들고 읽기 전용으로 시작하라.</strong> 먼저 문서를 읽고 요약하게 하고, 내부 메모로 초안만 쓰게 하십시오. 충분히 신뢰가 쌓인 뒤에야 행동 권한을 부여하십시오.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">5</div>
        <div class="num-content"><strong>봇이 지켜보는 가운데 작업을 직접 손으로 한 번 수행하라.</strong> "태스크 가르치기(Teach a task)"를 쓰십시오. 그런 다음 판단 로직, 에러 처리, 승인 단계를 손으로 덧붙이십시오.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">6</div>
        <div class="num-content"><strong>두 번째 봇을 만들기 전에 검증 루프부터 구축하라.</strong> 아무리 조잡해도 상관없습니다. 봇이 자신의 작업물을 실제 환경과 대조해 스스로 검증할 수 있다면 이후 모든 작업이 빨라집니다.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">7</div>
        <div class="num-content"><strong>이제야 비로소 비서실장(Chief of Staff) 봇을 도입하라.</strong> 그리고 이후의 모든 추가 봇은 비서실장을 통해 생성하십시오. 그래야 비서실장이 각 봇의 쓰임새를 온전히 이해합니다.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">8</div>
        <div class="num-content"><strong>교정 내용을 일반 원칙으로 축적하라.</strong> 봇이 잘못 생각할 때마다, 특정 사건이 아닌 일반화된 원칙을 작성하십시오. 이 배움의 누적이 1주 차와 3개월 차의 격차를 만듭니다.</div>
      </div>
      <div class="num-item" style="padding:3.5pt 0;">
        <div class="num-badge">9</div>
        <div class="num-content"><strong>금요일마다 등록된 루틴들을 감사하라.</strong> 빈번한 실행 주기는 돈이 새어 나가는 주범입니다. 정기 스케줄로 돌아가는 것 중 이벤트 트리거로 바꿀 수 있는 것은 전부 전환하십시오.</div>
      </div>
    </div>

    <div class="quote-box" style="margin:5pt 0 7pt 0;">
      <p class="quote-text" style="font-size:11pt;">“오늘 하지 않을 이유가 있는가? (Why not today?)”</p>
      <p class="quote-author">로샨의 고정 슬랙 상태 메시지이자, 이 가이드를 맺기에 더없이 완벽한 한마디</p>
    </div>

    <div class="callout" style="margin-top:0;">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">그리고 절대로 하지 말아야 할 단 한 가지</div>
        <p class="callout-text">
          재미있다는 이유만으로 봇을 마구 찍어내지 마십시오. 만드는 게 재미있다는 것, 바로 그것이 문제입니다. 새 봇을 뽑을 때마다 컨텍스트, 루틴, 주의 집중 비용이 청구되며, 방송에서 가장 큰 봇 팀을 굴렸던 이들일수록 팀을 작게 유지해야 한다고 가장 격렬하게 목소리를 높였습니다. 봇을 더 만들고 싶은 충동이 들 때마다, 기존 전문가 봇에게 새 스킬을 가르치는 것으로 해결할 수 없는지 먼저 자문하십시오.
        </p>
      </div>
    </div>
    {get_footer(24)}
  </div>
    """
