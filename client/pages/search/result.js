import { useState, useEffect } from "react";
import Head from "next/head";
import styles from "../../styles/Result.module.css";
import Header from "../../components/Header";
import { useRouter } from "next/router";
import axios from "axios";

const Result = () => {
  const router = useRouter();
  const { q, l } = router.query;
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    var bodyFormData = new FormData();
    bodyFormData.append("text", q);
    bodyFormData.append("language", l);
    axios({
      method: "post",
      url: process.env.NEXT_PUBLIC_API_ROUTE + "check/text",
      data: bodyFormData,
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }).then((res) => {
      setIsLoading(false);
      console.log(res);
      // if (res.status === 201) router.push("/results");
      // else actions.setSubmitting(false);
    });
  }, [{ q, l }]);

  return (
    <div>
      <Head>
        <title>MiliDoc</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <div className={styles.container}>
        <div className={styles.inputContainer}>
          <div>
            <h1>{q}</h1>
            <hr />
            <h3>
              1. 컴퓨터에서, 프로그램을 새로 개발하였을 때에 오류가 없는지
              최종적으로 검사하는 일2. 문자 대신에 그림이나 부호를 사용하여
              지능을 재는 검사
            </h3>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Result;
