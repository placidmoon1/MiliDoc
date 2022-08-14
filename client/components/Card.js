import styles from "../styles/components/Card.module.css";
import { useRouter } from "next/router";

const Card = (props) => {
  const router = useRouter();

  return (
    <div
      className={styles.cardContainer}
      onClick={() => router.push(props.link)}
    >
      <div className={styles.titleContainer}>
        <h1>{props.title}</h1>
      </div>
      <hr />
      <h3>{props.description}</h3>
    </div>
  );
};

export default Card;
