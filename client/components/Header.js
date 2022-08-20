import styles from "../styles/components/Header.module.css";
import Image from "next/image";
import { useRouter } from "next/router";
import { MdDocumentScanner, MdSearch } from "react-icons/md";
import { Button, ButtonGroup } from "@chakra-ui/react";

const Header = () => {
  const router = useRouter();

  return (
    <header className={styles.container}>
      <div className={styles.leftContainer}>
        <Image
          src="/logo.png"
          width={150}
          height={50}
          alt="MiliDoc"
          onClick={() => router.push("/")}
          style={{ marginLeft: "-10px", cursor: "pointer" }}
        />
        <div className={styles.iconTextView} style={{ marginRight: "15px" }}>
          <MdDocumentScanner style={{ marginRight: "4px" }} />
          <h2 onClick={() => router.push("/analyze")}>텍스트 분석</h2>
        </div>
        <div className={styles.iconTextView}>
          <MdSearch style={{ marginRight: "4px" }} />
          <h2 onClick={() => router.push("/search")}>단어 검색</h2>
        </div>
      </div>
      <div className={styles.navigationContainer}>
        <Button
          onClick={() => router.push("/login")}
          variant="ghost"
        >
          로그인
        </Button>
        <Button
          onClick={() => router.push("/signup")}
          variant="ghost"
        >
          회원가입
        </Button>
      </div>
    </header>
  );
};

export default Header;
