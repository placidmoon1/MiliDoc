import styles from "../styles/components/Header.module.css";
import Image from "next/image";

const Header = (props) => {
  return (
    <header className={styles.container}>
      <Image
        src="/bg_logo.png"
        width={200}
        height={50}
        alt="어플 이름"
      />
    </header>
  );
};

export default Header;
