import { useState, useEffect } from "react";
import Head from "next/head";
import styles from "../../styles/Result.module.css";
import Header from "../../components/Header";
import { useRouter } from "next/router";
import axios from "axios";
import Loader from "../../components/Loader";
import { Tag } from "@chakra-ui/react";

const Result = () => {
  const router = useRouter();
  const { q, l } = router.query;
  const [isLoading, setIsLoading] = useState(true);
  const [isError, setIsError] = useState(false);
  const [wordData, setWordData] = useState({});

  useEffect(() => {
    axios({
      method: "get",
      url:
        process.env.NEXT_PUBLIC_API_ROUTE +
        "search/word?lang=" +
        l +
        "&query=" +
        q,
    })
      .then((res) => {
        setWordData(res.data);
        setIsLoading(false);
        // if (res.status === 201) router.push("/results");
        // else actions.setSubmitting(false);
      })
      .catch((res) => {
        setIsError(true);
        setIsLoading(false);
      });
  }, []);

  return (
    <div>
      <Head>
        <title>MiliDoc</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        {isLoading ? (
          <Loader />
        ) : isError ? (
          <div className={styles.inputContainer}>
            <div>
              <div className={styles.titleContainer}>
                <h1>{q}</h1>
              </div>
              <hr />
              <div>
                <h3>죄송합니다. 단어를 못 찾았습니다.</h3>
              </div>
            </div>
          </div>
        ) : (
          <div className={styles.inputContainer}>
            <div>
              <div className={styles.titleContainer}>
                {l == "ko" ? (
                  wordData.english !== "" ? (
                    <h1>
                      {q} | {wordData.english}
                    </h1>
                  ) : (
                    <h1>{q}</h1>
                  )
                ) : wordData.korean !== "" ? (
                  <h1>
                    {q} | {wordData.korean}
                  </h1>
                ) : (
                  <h1>{q}</h1>
                )}
                <div style={{display: "flex", flexDirection: "row"}}>
                  {wordData.abandon !== 1 && wordData.forbidden === "" ? (
                    <Tag
                      size={"lg"}
                      key={"lg"}
                      variant="solid"
                      colorScheme="green"
                      style={{ height: "1rem" }}
                    >
                      금칙어/금지어 아님
                    </Tag>
                  ) : (
                    ""
                  )}
                  {wordData.abandon === 1 ? (
                    <Tag
                      size={"lg"}
                      key={"lg"}
                      variant="solid"
                      colorScheme="red"
                      style={{ height: "1rem" }}
                    >
                      금칙어
                    </Tag>
                  ) : (
                    ""
                  )}
                  {wordData.forbidden !== "" ? (
                    <Tag
                      size={"lg"}
                      key={"lg"}
                      variant="solid"
                      colorScheme="yellow"
                      style={{ height: "1rem" }}
                    >
                      권고사항: {wordData.forbidden}
                    </Tag>
                  ) : (
                    ""
                  )}
                  {wordData.acronym !== "" ? (
                    <Tag
                      size={"lg"}
                      key={"lg"}
                      variant="solid"
                      colorScheme="gray"
                      style={{ height: "1rem", marginLeft: "0.5rem" }}
                    >
                      약어: {wordData.acronym}
                    </Tag>
                  ) : (
                    ""
                  )}
                </div>
              </div>
              <hr />
              {wordData.def1 === "" ? (
                <div>
                  <h3>죄송합니다. 단어/뜻을 못 찾았습니다.</h3>
                </div>
              ) : (
                <div className={styles.defContainer}>
                  {wordData.def1 !== "" ? <h3>1. {wordData.def1}</h3> : ""}
                  {wordData.def2 !== "" ? <h3>2. {wordData.def2}</h3> : ""}
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Result;
