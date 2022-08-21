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
            description={"넣고 싶은 글을 넣어주세요! 밀리닥이 당신의 글을 더 완벽하고 정부 규정에 맞게 교정해드립니다."}
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
        </div>
      </div>
    </div>
  );
}
