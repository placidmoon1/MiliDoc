import styles from "../styles/components/Header.module.css";
import Image from "next/image";
import { useRouter } from "next/router";
import { MdDocumentScanner, MdUploadFile, MdSearch } from "react-icons/md";

const Header = () => {
  const router = useRouter();

  return (
    <header className={styles.container}>
      <Image src="/logo.png" width={150} height={50} alt="어플 이름" onClick={() => router.push("/")} style={{marginLeft: "-10px", cursor: "pointer"}} />
      <div className={styles.navigationContainer}>
        <div className={styles.iconTextView} style={{ marginRight: "15px" }}>
          <MdDocumentScanner style={{ marginRight: "4px" }} />
          <h2 onClick={() => router.push("/analyze")}>텍스트 분석</h2>
        </div>
        {/* <div className={styles.iconTextView} style={{ marginRight: "15px" }}>
          <MdUploadFile style={{ marginRight: "4px" }} />
          <h2 onClick={() => router.push("/upload")}>파일 업로드</h2>
        </div> */}
        <div className={styles.iconTextView}>
          <MdSearch style={{ marginRight: "4px" }} />
          <h2 onClick={() => router.push("/search")}>단어 검색</h2>
        </div>
      </div>
    </header>
  );
};

export default Header;
