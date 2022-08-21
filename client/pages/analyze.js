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
      } else {
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
              당신의 텍스트를 넣어주세요. Milidoc이 당신만의 가이드가
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
