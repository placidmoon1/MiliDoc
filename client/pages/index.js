import Head from "next/head";
import styles from "../styles/Home.module.css";
import Header from "../components/Header";
import Card from "../components/Card";
import { MdDocumentScanner, MdSearch } from "react-icons/md";

export default function Home() {
  return (
    <div>
      <Head>
        <title>MiliDoc</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
          <Card
            icon={<MdDocumentScanner />}
            title={"텍스트 분석"}
            description={
              "넣고 싶은 글을 넣어주세요! 밀리닥이 당신의 글을 더 완벽하고 정부 규정에 맞게 교정해드립니다."
            }
            link={"/analyze"}
          />
          <Card
            icon={<MdSearch />}
            title={"단어 검색"}
            description={
              "궁금하신 단어를 넣어주세요. 밀리닥이 당신을 위해 사전적 정의를 찾거나 번역을 도와드릴 수 있습니다."
            }
            link={"/search"}
          />
          {/* <Card icon={<MdUploadFile />} title={"텍스트 분석"} />
          <Card title={"단어 검색"} /> */}
          <div className={styles.creditsContainer}>
            <h1>API 사용 출처:</h1>
            <hr />
            <h2>국방 오픈데이터: </h2>
            <p>
              1) 국방데이터 표준단어 API{" "}
              <a href="https://opendata.mnd.go.kr/openinf/sheetview2.jsp?infId=OA-9420">
                https://opendata.mnd.go.kr/openinf/sheetview2.jsp?infId=OA-9420
              </a>
            </p>
            <br />
            <h2>정부 오픈데이터: </h2>
            <p>
              2) 국방부 병무행정 용어 순환 목록{" "}
              <a href="https://mma.go.kr/boardFileDown.do?gesipan_id=2&gsgeul_no=1494510&ilryeon_no=1">
                https://mma.go.kr/boardFileDown.do?gesipan_id=2&gsgeul_no=1494510&ilryeon_no=1
              </a>
            </p>
            <p>
              3) 병무청 용어 해설집{" "}
              <a href="https://www.mma.go.kr/www_mma3/ebook/mma_comment/mma_comment.PDF">
                https://www.mma.go.kr/www_mma3/ebook/mma_comment/mma_comment.PDF
              </a>
            </p>
            <p>
              4) 행정안전부, 공공데이터 공통표준용어{" "}
              <a href="https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000016&nttId=81609">
                https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000016&nttId=81609
              </a>
            </p>
            <p>
              5) 국립국어원 표준국어대사전 오픈 API{" "}
              <a href="https://stdict.korean.go.kr/openapi/openApiInfo.do">
                https://stdict.korean.go.kr/openapi/openApiInfo.do
              </a>
            </p>
            <br />
            <h2>민간 오픈데이터: </h2>
            <p>
              {" "}
              6) JYP엔터테인먼트 금지어 리스트 데이터 목록{" "}
              <a href="https://t.co/tNny1zeLla">
                https://t.co/tNny1zeLla
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
