import Head from "next/head";
import styles from "../styles/Analyze.module.css";
import { Formik, Form, Field } from "formik";
import { Textarea, Button, FormControl } from "@chakra-ui/react";
import { Tooltip } from "@chakra-ui/react";
import Header from "../components/Header";
import axios from "axios";
import Loader from "../components/Loader";
import { useState } from "react";

export default function Analyze() {
  const [isLoading, setIsLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [originalText, setOriginalText] = useState("");
  const [textData, setTextData] = useState([]);

  const reset = () => {
    setOriginalText("");
    setSubmitted(false);
    return;
  };

  const styleTextResult = (textList) => {
    var result = textList.map((wordData) => {
      if (wordData.abandon_exist) {
        return (
          <span key={wordData.word_ind}>
            <Tooltip label={"금칙어"} aria-label="Restricted Tooltip">
              <span className={styles.restrictedWord}>{wordData.word}</span>
            </Tooltip>
          </span>
        );
      } else if (wordData.forbidden !== "") {
        return (
          <span key={wordData.word_ind}>
            <Tooltip
              label={"권고사항: " + wordData.forbidden}
              aria-label="Limited Tooltip"
            >
              <span className={styles.limitedWord}>{wordData.word}</span>
            </Tooltip>
          </span>
        );
      }  else {
        return <span key={wordData.word_ind}>{wordData.word}</span>;
      }
    });
    return result;
  };

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
        ) : submitted ? (
          <div className={styles.resultContainer}>
            <div className={styles.textResultContainer}>
              <p>{styleTextResult(textData)}</p>
              <div className={styles.buttonContainer}>
                <Button
                  onClick={reset}
                  variant="solid"
                  style={{ marginTop: "1rem" }}
                >
                  다시하기
                </Button>
              </div>
            </div>
          </div>
        ) : (
          <div className={styles.inputContainer}>
            <h2 style={{ fontWeight: 600, fontSize: "1.5rem" }}>
              당신의 텍스트를 넣어주세요. MiliDoc이 당신만의 가이드가
              되어줍니다.
            </h2>
            <br />
            <Formik
              initialValues={{ body: "" }}
              onSubmit={(values, actions) => {
                setIsLoading(true);
                var bodyFormData = new FormData();
                bodyFormData.append("text", values.body);
                setOriginalText(values.body);
                axios({
                  method: "post",
                  url: process.env.NEXT_PUBLIC_API_ROUTE + "check/text2",
                  data: bodyFormData,
                  headers: {
                    "Content-Type": "multipart/form-data",
                  },
                }).then((res) => {
                  console.log(res);
                  setTextData(res.data);
                  setIsLoading(false);
                  setSubmitted(true);
                  actions.setSubmitting(false);
                });
              }}
            >
              {(props) => (
                <Form>
                  <Field name="body">
                    {({ field, form }) => (
                      <FormControl>
                        <Textarea
                          {...field}
                          id="body"
                          resize="none"
                          style={{
                            height: "400px",
                            width: "100%",
                            backgroundColor: "white",
                          }}
                          placeholder={`예시) 정부가 K2 전차, K9 자주포, FA-50 경공격기 등 20조원대 국산 무기 수출 본 계약을 앞두고 있는 폴란드 등 국산 무기 수입을 추진 중인 주요 8개국에서 방산 중점공관 운영을 추진한다.

박진 외교부 장관은 18일 국회 외교통일위원회 전체회의에 서면으로 제출한 업무보고에서 방산 세일즈 외교를 국가별 맞춤형으로 강화하겠다며 이같이 밝혔다.

박 장관이 이날 언급한 방산 중점공관 운영 대상국은 폴란드를 비롯해 사우디 아라비아‧호주‧노르웨이‧미국‧말레이시아‧인도네시아 등이다.

정부는 지난달 말 주폴란드 한국대사관에 국산 무기체계 수출입 계약 체결 관련 업무를 맡는 방산 전담 무관 파견 방침을 밝힌 바 있다.

박 장관의 중점공관 운영 방침은 이를 확대해 상시 운영 체제로 바꾸겠다는 뜻으로 풀이된다.

출처 : 국방신문(http://www.gukbangnews.com)`}
                        />
                      </FormControl>
                    )}
                  </Field>
                  <div className={styles.buttonContainer}>
                    <Button
                      variant="solid"
                      isDisabled={props.values.body === ""}
                      isLoading={props.isSubmitting}
                      type="submit"
                    >
                      검사하기
                    </Button>
                    <p style={{ fontWeight: 600 }}>
                      단어 수:{" "}
                      {props.values.body === ""
                        ? 0
                        : props.values.body.trim().split(/\s+/).length}
                    </p>
                  </div>
                </Form>
              )}
            </Formik>
          </div>
        )}
      </div>
    </div>
  );
}
